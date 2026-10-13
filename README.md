# 🏏 IPL Win Probability Predictor

A Machine Learning web application that predicts the winning probability of IPL teams during a live match based on match conditions like score, wickets, overs, and target.

---

## 🚀 Live Demo

https://ipl-match-prediction-m4vzw8wupges4bgmbpgfxq.streamlit.app/

---

## 📌 Project Overview

This project uses historical IPL match data to predict the probability of the batting team winning a match in real-time.

It takes key match inputs such as:

* Batting Team
* Bowling Team
* Host City
* Target Score
* Current Score
* Overs Completed
* Wickets Lost

Based on these inputs, the model calculates:

* Runs left
* Balls left
* Current Run Rate (CRR)
* Required Run Rate (RRR)

And predicts:

* ✅ Batting Team Win Probability
* ❌ Bowling Team Win Probability

---

## 🧠 Machine Learning Model

* Algorithm Used: Logistic Regression
* Pipeline:

  * Data Preprocessing
  * Feature Engineering
  * One-Hot Encoding (Categorical Features)
  * Model Training

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Streamlit (for UI)
* Pickle (model serialization)

---

## 📊 Features

* 📈 Real-time win probability prediction
* 🎯 Accurate calculations using match metrics
* 🚨 Edge case handling:

  * All wickets lost → 0% win
  * No balls left → match result
  * Low wickets → adjusted probability

---

## 📁 Project Structure

```
├── app.py                # Streamlit app
├── pipe.pkl             # Trained ML model
├── deliveries.csv       # Dataset
├── matches.csv          # Dataset
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ipl-win-predictor.git
cd ipl-win-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 💡 Key Learnings

* Applied Machine Learning to real-world sports analytics
* Built end-to-end ML pipeline
* Developed interactive web app using Streamlit
* Combined ML with rule-based logic for better accuracy

---

## 🚀 Future Improvements

* Add player-level data (batsman, bowler stats)
* Improve model accuracy using advanced algorithms
* Add live match API integration
* Visualize win probability graph

---

## 👨‍💻 Author

**Munilalithya Sana**
Email:munilalithya@gmail.com

🔗 LinkedIn | GitHub

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
