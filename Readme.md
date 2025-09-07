![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest&logoColor=white)


# 🚀 Selenium-Pytest Automation Framework  

## 📌 Overview  
This project is a **Page Object Model (POM) based automation framework** built with **Python, Selenium, and Pytest**.  
It automates key workflows on this [practice site](https://rahulshettyacademy.com/loginpagePractise/), including:  
- User login  
- Product selection & checkout  
- Removing items from the cart  
- End-to-end purchase validation  

The framework is designed to be **scalable, maintainable, and easy to integrate** with CI/CD tools.  

---

## ⚙️ Tech Stack  
- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Test Runner:** Pytest  
- **Reporting:** pytest-html  
- **Parallel Execution:** pytest-xdist  
- **Logging:** Python logging module  
- **Data Handling:** JSON  

---

## 📂 Project Structure  
```
PageObject_version/
│
├── page_objects/ # Page classes (Login, Shop, Checkout, BasePage)
├── tests/ # Test files
├── utils/ # Utilities (Logger)
├── reports/ # Test reports & logs (runtime only)
├── screenshots/ # Screenshots (runtime only)
├── conftest.py # Pytest fixtures
├── test_data.json # Test data
├── requirements.txt # Dependencies
├── pytest.ini # Pytest config
└── README.md # Project documentation
```

---

## 🚀 How to Run  

### 1️⃣ Clone the repo  
```
git clone https://github.com/srikar-N/Automation_project_1.git

cd <repo-name>
```
### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Execute tests
```
pytest
```
### Run in parallel (2 threads):
```
pytest -n 2
```
### Run with HTML report:
```commandline
pytest --html=reports/test_report.html --self-contained-html
```
## 📊 Reports & Screenshots

- **Logs** → stored in reports/automation.log

- **HTML Report** → generated in reports/

- **Screenshots** → automatically captured on test failures, saved in screenshots/

## 🔮 Future Enhancements

- Jenkins CI/CD pipeline integration
- Excel-based test data handling

## 👤 Author
Built with ❤️ by Srikar
