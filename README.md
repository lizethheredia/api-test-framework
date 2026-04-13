# API Test Framework — Restful Booker

Automated API test suite for the [Restful Booker](https://restful-booker.herokuapp.com) API,
a hotel booking REST API used for testing and practice purposes.
Built with Python and Pytest.

## 🌐 API Under Test
**Restful Booker** — https://restful-booker.herokuapp.com

A REST API that simulates a hotel booking system with endpoints for:
- Authentication
- Creating, reading, updating, and deleting bookings

API documentation: https://restful-booker.herokuapp.com/apidoc/index.html

## 🛠️ Tech Stack
- Python 3.10
- Pytest
- Requests
- python-dotenv
- GitHub Actions (CI/CD)

## 📁 Project Structure
    api-test-framework/
    ├── .github/workflows/    # CI/CD pipeline
    ├── config/               # Environment configuration
    ├── src/api/              # API client classes
    ├── tests/                # Test suites
    ├── reports/              # HTML test reports
    ├── .env                  # Local secrets (not committed)
    ├── pytest.ini            # Pytest configuration and markers
    └── requirements.txt      # Project dependencies

## ✅ Test Coverage
| Module | Tests |
|--------|-------|
| Authentication | Token generation, invalid credentials, missing credentials |
| Create Booking | Success, response validation |
| Get Booking | All bookings, single, not found |
| Update Booking | Full update, partial update |
| Delete Booking | Success, verify deletion |

## 🚀 How to Run

### 1. Clone the repository
    git clone https://github.com/lheredia/api-test-framework.git
    cd api-test-framework

### 2. Create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate

### 3. Install dependencies
    pip install -r requirements.txt

### 4. Set up environment variables
    cp .env.example .env

### 5. Run all tests
    pytest
py
### 6. Run by marker
    pytest -m smoke
    pytest -m regression

### 7. Run with HTML report
    pytest --html=reports/report.html

## ⚙️ CI/CD
Tests run automatically on every push to main via GitHub Actions.

## 🔐 Environment Variables
Create a `.env` file in the root directory:

    BASE_URL=https://restful-booker.herokuapp.com
    API_USERNAME=admin
    API_PASSWORD=password123

## 👩‍💻 Author
Liz Heredia — SDET | Python Automation | API Testing
[GitHub](https://github.com/lheredia)