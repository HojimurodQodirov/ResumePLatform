# Resume Platform

A platform for creating and viewing resumes. Users can register, create resumes, and view them.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/resume-platform.git
    cd resume-platform
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following:

    ```plaintext
    SECRET_KEY=your-secret-key
    ```

5. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser (admin):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000`

## Features

- User registration and authentication
- Create, view, and manage resumes
- Admin interface for managing users and resumes

## Project Structure

```plaintext
resume_platform/
    manage.py
    resume_platform/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    resumes/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        serializers.py
        views.py
        urls.py
        templates/
            resumes/
                create_resume.html
                view_resume.html
    users/
        __init__.py
        forms.py
        models.py
        views.py
        templates/
            registration/
                signup.html
                login.html
    templates/
        base.html
