# 🔐 Network Security – Phishing Detection (End-to-End ML Pipeline)

This project is an **end-to-end Machine Learning pipeline** for detecting **phishing websites**, inspired by **Krish Naik’s MLOps-based project structure**.  
It demonstrates how to build a **production-ready ML system** using modular components, configuration-driven design, proper logging, and exception handling.

---

## 🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats.  
This project uses **machine learning classification models** to predict whether a website is **phishing or legitimate** based on extracted features.

The entire ML lifecycle is implemented as a **pipeline**, similar  to how real-world ML systems are built in industry.

---

## 🧠 Key Concepts Used

- Modular ML pipeline architecture  
- Configuration-driven development  
- Custom exception handling  
- Centralized logging  
- Hyperparameter tuning with GridSearchCV  
- Artifact-based pipeline execution  
- Scikit-learn ML models  
- Production-style folder structure  

---

## 🗂️ Project Structure
```bash
NETWORKSECURITY/
│
├── networksecurity/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_validation.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── constant/
│ │ └── training_pipeline/
│ │ └── model.py
│ │
│ ├── entity/
│ │ ├── config_entity.py
│ │ └── artifact_entity.py
│ │
│ ├── exception/
│ │ └── exception.py
│ │
│ ├── logging/
│ │ └── logger.py
│ │
│ ├── utils/
│ │ ├── main_utils/
│ │ │ └── utils.py
│ │ └── ml_utils/
│ │ ├── metric/
│ │ └── model/
│ │
├── data_schema/
│ └── schema.yaml
│
├── Artifacts/
│ └── (auto-generated pipeline artifacts)
│
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```
## ⚙️ ML Pipeline Workflow

### 1️⃣ Data Ingestion
- Reads phishing dataset
- Splits data into train and test sets
- Stores them as pipeline artifacts

### 2️⃣ Data Validation
- Validates dataset schema using `schema.yaml`
- Performs data drift checks
- Generates validation reports

### 3️⃣ Data Transformation
- Handles missing values
- Applies preprocessing steps
- Saves transformed NumPy arrays and preprocessing object

### 4️⃣ Model Training
- Trains multiple classification models
- Performs hyperparameter tuning
- Selects the best-performing model
- Saves the trained model

## 🤖 Models Used

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  
- AdaBoost Classifier  
- Gradient Boosting Classifier  

Evaluation is done using **classification metrics** such as accuracy and F1-score.

## 📦 Artifacts Generated

- Train/Test CSV files  
- Transformed NumPy arrays (`.npy`)  
- Preprocessing object (`preprocessing.pkl`)  
- Trained model (`model.pkl`)  
- Data drift report (`report.yaml`)  

Artifacts are stored inside the `Artifacts/` directory with timestamped folders.

## 🛠️ Installation & Setup

Follow the steps below to set up the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/NetworkSecurity.git
cd NetworkSecurity
```
2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
3️⃣ Activate the Virtual Environment
```bash
venv\Scripts\activate
```
4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
▶️ Run the Project
```bash
python main.py
```
## 🧩 Logging & Exception Handling

Centralized logging for tracking pipeline execution

Custom NetworkSecurityException for detailed error tracing

Helps in debugging and monitoring ML pipelines

🎯 Learning Outcomes

Understanding of end-to-end ML pipeline design

Hands-on experience with production-style ML projects

Knowledge of hyperparameter tuning and model selection

Clear separation of concerns using components and artifacts

Real-world MLOps project structure



## 👨‍💻 Author

Saksham Singh
B.Tech CSE | Aspiring AI & ML Engineer
