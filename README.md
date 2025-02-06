# **QA Automation Test - Kiwi.com**

## **Project Overview**
This automation project is designed to test the **basic flight search functionality** on **Kiwi.com** using **Python, Playwright, and pytest-bdd**. The test interacts with the website in real-time, verifying search results and ensuring smooth user interactions.

---

## **1️⃣ Installation & Setup**

### **🔹 Prerequisites**
Ensure you have the following installed:
- Python 3.10+
- Node.js & NPM (for Playwright browsers)
- Git

### **🔹 Clone the Repository**
```sh
 git clone [playwright-bdd-test.git](https://github.com/mottwan/plawright-bdd-test.git)
 cd playwright-bdd-test
```

### **🔹 Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **🔹 Install Dependencies**
#### **Dependencies List**
```
playwright~=1.50.0
pytest == 8.3.4
pytest-bdd == 8.1.0
pytest-xdist == 3.6.1
pytest-playwright == 0.7.0
flake8 == 7.1.1
isort == 6.0.0
black == 25.1.0
mypy == 1.15.0
pylint == 3.3.4
flake8-bugbear == 24.12.12
flake8-docstrings == 1.7.0
pre-commit == 4.1.0
python-dateutil == 2.9.0.post0
```
```sh
pip install -e .[dev]
npx playwright install  # Install Playwright browsers
```

---

## **2️⃣ Running the Test Suite**

### **🔹 Run the Test using `@pytest.mark.basic_search`**
```sh
pytest -m "basic_search"
```

### **🔹 Run All Tests**
```sh
pytest
```

---

## **4️⃣ CI/CD Integration**

### **🔹 Jenkins Setup**
1. Install **Allure Plugin** & **Pipeline Plugin** in Jenkins.
2. Configure a Jenkins job and set the repository URL.
3. Use the `Jenkinsfile` provided in the repo.
4. Run the pipeline.
---

## **5️⃣ Generating Reports**

### **🔹 JUnit XML Report**
Located in `results.xml` and viewable in Jenkins/GitHub Actions.

---

## **6️⃣ Project Structure**
```
playwright-bdd-test/
│── features/                     # Gherkin feature files
│   ├── basic_search.feature     
├── steps/
│   ├── __init__.py
│   ├── search_steps.py           # Step definitions for BDD
│   ├── conftest.py               # Pytest configurations/fixtures
├── pages/                        # Page Object Model (POM)
│   ├── selectors/
│   │   ├── __init__.py
│   │   ├── home_page_selectors.py
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py   
│   ├── search_results_page.py   
├── utils/
│   ├── __init__.py
│   ├── airport_code_enum.py      
│   ├── datetime_utils.py         
├── reports/                      # Stores test reports
├── .pre-commit-config.yaml       # Executes flake8 formatting
├── lint.sh                       # Code formatting
├── pyproject.toml                # Dependencies and setup
├── Jenkinsfile                   # Jenkins pipeline configuration
├── README.md                     # Setup instructions
│── setup.py
```

---

## **7️⃣ Additional Notes**
- Tests **run in real browsers** (no mocking).
- The project follows the **Page Object Model (POM)** structure.
- CI/CD supports **Jenkins**.

🚀 **Now you're ready to automate Kiwi.com!**

