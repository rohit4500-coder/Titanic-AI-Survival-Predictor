# 🚢 Titanic AI Survival Predictor

<div align="center">

### AI-Powered Passenger Survival Prediction System

A Machine Learning web application that predicts whether a Titanic passenger survived based on historical passenger data.

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

## 📌 About The Project

Titanic AI Survival Predictor is a Machine Learning based web application that predicts the survival probability of a Titanic passenger.

The model is trained using the famous Titanic dataset and uses passenger information such as age, gender, passenger class, ticket fare, family members, and embarkation port.

The trained Machine Learning model is integrated into a Flask web application with a modern cyberpunk-inspired user interface.

---

# ✨ Features

- 🤖 Machine Learning based prediction
- 🌲 Random Forest Classifier
- 📊 Survival probability calculation
- 🌐 Flask web application
- 💻 Interactive prediction dashboard
- 🎨 Cyberpunk / hacker-style UI
- 📱 Fully responsive design
- ⚡ Real-time predictions
- 🔐 Clean and structured application architecture

---

# 🧠 Machine Learning Model

The application uses a **Random Forest Classifier** for predicting passenger survival.

### Model Workflow

```text
                 ┌──────────────────┐
                 │  Titanic Dataset │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Data Preprocessing│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Feature Selection │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Train-Test Split │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Random Forest ML │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Model Evaluation │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Flask Deployment │
                 └──────────────────┘




Titanic-AI-Survival-Predictor
│
├── 📄 app.py
├── 🤖 model.pkl
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
│
└── 📁 templates
    │
    └── 📄 index.html
