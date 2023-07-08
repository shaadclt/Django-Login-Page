# Django - User Login and Authentication System

This project implements a user login and authentication system using Django, allowing users to sign in, sign out, and access protected views.

## Features

- User authentication: Users can sign in using their username and password.
- Protected views: Certain views are restricted to authenticated users only.
- Sign out: Users can sign out and end their session.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/shaadclt/Django-Login-Page.git
```

2. Change into the project directory:

```bash
cd Django-Login-Page
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Django development server:

```bash
python manage.py runserver
```

5. Open your browser and access the application at `http://localhost:8000`.

## Usage

1. Sign in: Access the sign-in page by visiting `http://localhost:8000/signin`. Enter your username and password to sign in.
2. Access protected views: Once signed in, you can access the protected views by visiting `http://localhost:8000/home`.
3. Sign out: To sign out, click the "Sign out" button or visit `http://localhost:8000/signout`.

## Customization

You can customize the project by modifying the views, templates, or adding additional features based on your requirements. This project serves as a starting point for implementing user login and authentication in your Django application.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- This project is created for the purpose of implementing user login and authentication in Django.

## Contributing

Contributions are welcome! If you find any issues, have suggestions for improvements, or want to add more features, please open an issue or submit a pull request.
