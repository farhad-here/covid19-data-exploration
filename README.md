# 🦠 COVID-19 Data Analysis Dashboard

This project is a data analysis dashboard built using **Streamlit**, **SQLite**, and **SQL**. It visualizes and explores key insights from a COVID-19 dataset provided by Kaggle.

## 📁 Dataset

- **Source:** [Kaggle – Corona Virus Report](https://www.kaggle.com/datasets/imdevskp/corona-virus-report)
- **File used:** `country_wise_latest.csv`

The dataset includes COVID-19 statistics such as total confirmed cases, deaths, recovered, and active cases by country.

## 📊 Features

This dashboard includes the following analytics:

1. **Total confirmed cases per country**
2. **Comparison of total confirmed cases for Iran and Egypt**
3. **Top 10 countries by death rate**
4. **Death rate of all countries**
5. **COVID-19 deaths in Iran**
6. **Comparison of active vs. recovered cases per country**

Each analysis includes both **data tables** and **interactive visualizations** (bar charts, line charts, and comparative charts with Altair).

## 🛠 Technologies Used

- Python 🐍
- Streamlit 📺
- SQLite 🗃
- SQL 🧠
- Pandas 📊
- Altair 📈

## 🚀 How to Run

1. Clone this repository:

  ```bash
  git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
  cd YOUR_REPO_NAME
  ```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt

  ```
3. Run the Streamlit app:
   ```bash
    streamlit run "app/COVID-19 Data Exploration.py"
   ```
```bash
your_project/
├── data/
│   └── country_wise_latest.csv
├── queries/
│   ├── Total confirmed cases per country.sql
│   ├── Total confirmed cases for Iran.sql
│   ├── Top ten countries by death rate.sql
│   ├── all countries death rate.sql
│   ├── iran death by covid.sql
│   └── Active vs Recovered comparison.sql
├── app.py
└── requirements.txt


```

## 📸 Sample Visualizations
![sq1](https://github.com/user-attachments/assets/1631168e-f8b0-47fe-b881-5e9665d7ed08)
![sq2](https://github.com/user-attachments/assets/fdf45081-659c-4506-98ee-680e7a820bed)
![sq3](https://github.com/user-attachments/assets/827de36a-2cbc-43aa-b3ff-9a61342630b7)
![sq4](https://github.com/user-attachments/assets/7dc760fd-9083-46d6-a73d-e3bca14cb52a)
![sq6](https://github.com/user-attachments/assets/0b4a96f0-133d-4d2d-b24b-da9cef3f1d65)
![sqf](https://github.com/user-attachments/assets/c7b34b94-fab8-40c2-8ab7-d40ba68ce238)

### ✅ Total Confirmed Cases per Country
Bar chart and line chart showing total confirmed COVID-19 cases.

### ⚰️ Top 10 Countries by Death Rate
Compare which countries had the highest death rates.

### 🇮🇷 Iran COVID-19 Trends
Track how Iran has been affected and compare with Egypt.

### 💪 Active vs. Recovered
Dual comparison of active vs. recovered patients in each country.

### 💡 Purpose
- This project is designed to:

- Practice SQL queries in a real-world scenario

- Build a data dashboard using Python & Streamlit

- Demonstrate data storytelling through visuals

- Be part of a data portfolio or GitHub résumé


