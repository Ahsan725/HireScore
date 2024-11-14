# HireScore

HireScore is a powerful Django web application designed to optimize your resume and improve your chances of passing Applicant Tracking Systems (ATS) filters. By analyzing job descriptions and your resume, it identifies key keywords and phrases, compares them, and provides actionable insights. Whether you're a job seeker looking to stand out or a hiring manager seeking optimized job descriptions, HireScore is the perfect tool.

## Features

- **Job Description Analysis**: Upload a job description, and the app will extract and save the most relevant keywords.
- **Resume Matching**: Compare your resume against job description keywords to see which skills or keywords are missing.
- **Custom Stop Words**: Add specific words to a custom stop words list to exclude irrelevant terms from analyses.
- **Top Keywords**: View the most frequently occurring keywords across all job descriptions for better resume optimization.
- **User-Friendly Interface**: Simple and clean UI that makes it easy to upload files, view results, and refine your resume.

## Screenshots

![Home Page](path/to/screenshot1.png)
![Results Page](path/to/screenshot2.png)

## Technologies Used

- **Django**: Backend framework for building the web application.
- **SQLite**: Database for storing job descriptions, keywords, and custom stop words.
- **HTML/CSS/JavaScript**: Frontend technologies for creating a responsive and interactive UI.
- **Bootstrap**: Used for styling the interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the Repository**

   Open your terminal, navigate to the directory where you want to store this project, and run:

   ```bash
   git clone https://github.com/Ahsan725/HireScore.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd HireScore
   ```

3. **Create a Virtual Environment**

   It’s recommended to use a virtual environment to keep dependencies isolated. Run:

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**

   - **For macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

   - **For Windows**:

     ```bash
     venv\Scripts\activate
     ```

5. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run Database Migrations**

   Since the project includes a `db.sqlite3` file, the database is already populated with initial data. However, if you want to create a fresh database, you can delete `db.sqlite3` and run:

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Optional)**

   To access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin account.

8. **Run the Server**

   Start the development server:

   ```bash
   python manage.py runserver
   ```

9. **Access the Application**

   Open your browser and go to `http://127.0.0.1:8000` to access the HireScore application.

### Using HireScore

- **Upload Job Descriptions**: Navigate to the analysis page to upload a job description and extract keywords.
- **Resume Comparison**: Upload your resume text and compare it against a job description for keyword matching.
- **Manage Stop Words**: Add or remove words from your custom stop words list to fine-tune the analysis.

### Project Structure

```
HireScore/
├── analyzer/                 # Django app containing main functionalities
│   ├── management/           # Custom Django management commands
│   ├── migrations/           # Database migrations
│   ├── templates/analyzer/   # HTML templates for the app
│   ├── static/               # Static files (CSS, JavaScript, images)
│   ├── views.py              # View functions
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing for this app
│   └── ...                   # Other app files
├── job_analyzer/             # Project settings
│   ├── settings.py           # Django project settings
│   ├── urls.py               # URL routing for the project
│   └── ...                   # Other configuration files
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django management script
└── README.md                 # Project documentation
```

### Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
