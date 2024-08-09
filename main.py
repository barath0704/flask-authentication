from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key to enable session management and flash messages
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# Base class for models using SQLAlchemy's ORM system
class Base(DeclarativeBase):
    pass


# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Initialize Flask-Login manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# Define the User model inheriting from UserMixin and SQLAlchemy Base model
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key for User model
    email: Mapped[str] = mapped_column(String(100), unique=True)  # User's email (must be unique)
    password: Mapped[str] = mapped_column(String(100))  # User's hashed password
    name: Mapped[str] = mapped_column(String(1000))  # User's name


# Create all database tables within the app context
with app.app_context():
    db.create_all()


# Route for the home page
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


# Route for user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        user_password = request.form.get("password")

        # Check if a user with the same email already exists in the database
        result = db.session.execute(db.select(User).where(User.email == user_email))
        user = result.scalar()

        if user:
            # If user exists, flash a message and redirect to login page
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # Create a new user with hashed password
        new_user = User(
            name=user_name,
            email=user_email,
            password=generate_password_hash(user_password, method='pbkdf2:sha256', salt_length=8)
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Log the user in and redirect to the secrets page
        login_user(new_user)
        return redirect(url_for('secrets'))

    # Render the registration page
    return render_template("register.html", logged_in=current_user.is_authenticated)


# Route for user login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Retrieve the user from the database by email
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            # If user does not exist, flash a message and redirect to login page
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            # If password is incorrect, flash a message and redirect to login page
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            # Log the user in and redirect to the secrets page
            login_user(user)
            return redirect(url_for('secrets'))

    # Render the login page
    return render_template("login.html", logged_in=current_user.is_authenticated)


# Route for the secrets page, accessible only to logged-in users
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Render the secrets page and pass the current user's name
    return render_template("secrets.html", name=current_user.name, logged_in=True)


# Route for logging out
@app.route('/logout')
def logout():
    # Log the user out and redirect to the home page
    logout_user()
    return redirect(url_for('home'))


# Route for downloading a file, accessible only to logged-in users
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


# Run the Flask application in debug mode
if __name__ == "__main__":
    app.run(debug=True)
