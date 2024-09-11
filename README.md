# Resume Processor API

This project provides an API endpoint for processing resumes and extracting candidate information.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Inferno2211/ResumeProcessor
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up PostgreSQL and configure the database in settings.py.

4. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```

6. Test the API by sending a POST request to /api/extract_resume/ with a resume file.

# API Example
- Endpoint: /api/extract_resume/
- Method: POST
- Payload: resume file (PDF or DOC)