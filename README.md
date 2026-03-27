# Student Performance Prediction 🎓📊

## Overview

This project builds a **Machine Learning model to predict student math scores** based on their **reading and writing scores**. The goal is to explore relationships between different academic performance indicators and apply **Linear Regression** to make predictions.

The project demonstrates key **data science workflow steps** including data exploration, visualization, model training, and evaluation.

---

## Dataset

The dataset used in this project is **StudentsPerformance.csv**, which contains academic performance data of students.

Key columns include:

* gender
* race/ethnicity
* parental level of education
* lunch
* test preparation course
* **math score**
* **reading score**
* **writing score**

In this project:

* **Target variable:** `math score`
* **Input features:** `reading score`, `writing score`

---

## Tech Stack

**Programming Language**

* Python

**Libraries**

* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## Project Structure

```text
student-performance-ml
│
├── StudentsPerformance.csv
├── model.py
└── README.md
```

---

## Machine Learning Workflow

### 1. Data Loading

The dataset is loaded using **Pandas**.

### 2. Data Exploration

Correlation analysis is performed to understand relationships between variables.

### 3. Feature Selection

The model uses:

* reading score
* writing score

to predict:

* math score

### 4. Train-Test Split

The dataset is split into training and testing sets using **scikit-learn**.

### 5. Model Training

A **Linear Regression model** is trained on the training dataset.

### 6. Model Evaluation

Model performance is evaluated using:

* Mean Squared Error (MSE)
* R² Score

### 7. Visualization

Predicted scores are compared with actual scores using scatter plots.

---

## Example Output

The project generates:

* Correlation heatmap
* Actual vs predicted score graph
* Model evaluation metrics

These visualizations help understand the model’s accuracy and relationships between variables.

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/divijatewari/student-performance-ml.git
```

### 2. Navigate to the project folder

```bash
cd student-performance-ml
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 4. Run the program

```bash
python model.py
```

---

## Learning Outcomes

Through this project, the following concepts were practiced:

* Data analysis using Pandas
* Data visualization with Seaborn and Matplotlib
* Feature correlation analysis
* Building a regression model
* Evaluating machine learning models

---

## Future Improvements

Possible improvements include:

* Using more advanced models (Random Forest, Gradient Boosting)
* Predicting scores using additional features
* Building an interactive web application using Streamlit
* Adding model comparison and performance tuning

---

## Author

**Divija Tewari**
B.Tech Computer Science Engineering
Indira Gandhi Delhi Technical University for Women

GitHub: https://github.com/divijatewari
<img width="1728" height="926" alt="image" src="https://github.com/user-attachments/assets/31fcf2a8-454d-46c0-9772-23d3602be9e1" />
<img width="789" height="675" alt="image" src="https://github.com/user-attachments/assets/005ca1be-a9e7-4d6f-a9d5-6cc568f795b6" />

