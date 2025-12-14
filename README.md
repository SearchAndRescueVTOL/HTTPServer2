# Hello World Python Application

A simple Python hello world application with pytest testing and Docker containerization, integrated with GitHub Actions CI/CD.

## Project Structure

```
.
├── app.py              # Main Python application
├── test_app.py         # Pytest test suite
├── requirements.txt    # Python dependencies (pytest)
├── Dockerfile          # Docker container configuration
└── .github/workflows/
    ├── docker-image.yml    # Build and test workflow
    └── codeql.yml          # Security analysis workflow
```

## Local Development

### Prerequisites

- Python 3.10+
- Docker Desktop
- pytest

### Running Tests Locally

```bash
pytest test_app.py -v
```

### Running the Application

```bash
python app.py
```

Expected output: `Hello, World!`

## Docker

### Build the Docker Image

```bash
docker build -t hello-world-app .
```

### Run the Container

```bash
docker run hello-world-app
```

### Run Tests in Container

```bash
docker run hello-world-app pytest test_app.py -v
```

## GitHub Actions Workflows

### Build and Test Workflow

**File**: `.github/workflows/docker-image.yml`

This workflow runs on every push and pull request to the main branch. It consists of two separate jobs:

#### Job 1: Build
1. Checks out the code
2. Builds the Docker image
3. Saves the image as an artifact for the test job

#### Job 2: Test
1. Downloads the built Docker image from the build job
2. Loads the Docker image
3. Runs pytest tests inside the container
4. Runs the application to verify it works

The two-job structure provides:
- **Clear separation** of build and test stages in GitHub UI
- **Efficiency** by building the Docker image once and reusing it for testing
- **Reliability** by testing the actual containerized application

### CodeQL Workflow

**File**: `.github/workflows/codeql.yml`

Runs automated security analysis on Python code to detect vulnerabilities.

## Testing

The test suite includes:

- `test_hello_world()` - Verifies the function returns "Hello, World!"
- `test_main()` - Tests the main entry point
- `test_hello_world_not_empty()` - Ensures output is not empty

All tests run inside the Docker container during CI to ensure consistency with the production environment.
