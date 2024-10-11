# Job Application Tracker

A simple web application to help users track their job applications. This project allows users to add, retrieve, and manage job applications through a RESTful API built with Flask and SQLAlchemy.

## Features

- **Track Job Applications**: Add new job applications with details such as company name, position, status, and application date.
- **CRUD Operations**: Implemented Create, Read, Update, and Delete operations for job entries.
- **RESTful API**: Designed a RESTful API for seamless interaction between the frontend and backend.
- **Database Integration**: Utilized MySQL for storing job application data.

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: MySQL
- **Frontend**: HTML, JavaScript, jQuery (for AJAX calls)
- **Development Tools**: Git for version control, Postman for API testing

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Aditya19Joshi01/Job-Application-Tracker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd job-application-tracker
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database by running the following command:
   ```bash
   python -c "from app import db; db.create_all()"
   ```

7. Run the application:
   ```bash
   python app.py
   ```

8. Access the application in your web browser at:
   ```
   http://127.0.0.1:5000/api/v1/
   ```

## Usage

### Adding a Job Application

To add a job application, fill in the form with the following details:

- **Company**: Name of the company.
- **Position**: Job position applied for.
- **Status**: Current status of the application (Applied, Interviewing, Offer).

### Retrieving Job Applications

You can view your job applications by accessing the `/api/v1/jobs` endpoint, either via the frontend or using tools like Postman.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the Flask and SQLAlchemy communities for providing the tools to build this project.
- Special thanks to all contributors who provide feedback and suggestions.
