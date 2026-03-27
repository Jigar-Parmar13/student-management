# Student Management App 🎓

A simple Python + Flask web app to manage students.
Built to practice DevOps tools like GitHub Actions, Docker, Kubernetes.

## Features
- Add / Edit / Delete students
- View all students in a table
- Health check endpoint at `/health`

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

App runs at: http://localhost:5000

## Run Tests

```bash
pytest test_app.py
```

## Project Structure

```
student-management/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── test_app.py         # Tests (used by GitHub Actions)
├── templates/
│   ├── index.html      # Home page
│   └── edit.html       # Edit student page
└── README.md
```

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | List all students |
| POST | `/add` | Add a student |
| GET | `/edit/<id>` | Edit form |
| POST | `/edit/<id>` | Save edits |
| GET | `/delete/<id>` | Delete student |
| GET | `/health` | Health check |
