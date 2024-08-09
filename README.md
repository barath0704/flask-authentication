# Flask Authentication App

A simple Flask web application featuring user authentication, secure password hashing, and session management. This project is ideal as a starter template or learning tool.

## Features

- User registration and login
- Password hashing with Werkzeug
- Session management with Flask-Login
- SQLite database for user data
- Protected routes accessible only to logged-in users
- Simple file download functionality

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask shell
    from your_module_name import db
    db.create_all()
    exit()
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Access the app in your browser:**

    Go to `http://127.0.0.1:5000/`

## Usage

- **Home**: Visit the home page to see the welcome message.
- **Register**: Create a new account using the registration form.
- **Login**: Log in with your email and password.
- **Secrets**: Access the protected content after logging in.
- **Download**: Download a file from the protected area.
- **Logout**: Log out to end your session.

![image](https://github.com/user-attachments/assets/272a2340-f83a-44ce-9e75-6f1f7bde006e)

![image](https://github.com/user-attachments/assets/f9014665-5eda-4f02-9755-02ac8315e5e9)

![image](https://github.com/user-attachments/assets/81ce9544-7dc7-43e6-b98c-0faacac1ca2f)


![image](https://github.com/user-attachments/assets/8e92e668-94fc-4abd-95a3-613ab73b591e)

![image](https://github.com/user-attachments/assets/d1b3d5e5-5c20-4717-bd64-cc9e1f862eb3)

![image](https://github.com/user-attachments/assets/4273e4bd-18c9-4c51-a8bd-6b2b25e6814e)



