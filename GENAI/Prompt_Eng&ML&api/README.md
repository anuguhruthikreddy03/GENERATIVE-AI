# Prompt Engineering & Machine Learning for Sentiment Analysis

## 📌 Project Overview

This repository contains two NLP-focused projects that demonstrate both traditional Machine Learning techniques and modern Prompt Engineering approaches for sentiment and emotion analysis.

The projects are:

1. **Machine Learning-Based Emotion Detection**
2. **Prompt Engineering-Based Sentiment Analysis using Gemini LLM**

These projects showcase how text data can be analyzed using both classical NLP pipelines and Large Language Models (LLMs).

---

# 📂 Project Structure

```text
Prompt_Eng&ML&api/
│
├── ml-tree-promting.ipynb
│
├── Promt_engineering.ipynb
│
└── README.md
```

---

# Project 1: Machine Learning-Based Emotion Detection

## 🎯 Objective

The goal of this project is to classify human emotions from textual data using traditional Machine Learning techniques.

The model learns patterns from labeled emotion datasets and predicts emotions such as:

- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise

---

## 📊 Dataset

The project uses the **Emotions Dataset for NLP** obtained from Kaggle.

### Dataset Features

| Column | Description |
|----------|-------------|
| text | User text or sentence |
| emotion | Corresponding emotion label |

Example:

| Text | Emotion |
|--------|---------|
| I am feeling great today | Joy |
| I lost my best friend | Sadness |

---

## 🔄 Workflow

### 1. Data Collection

The emotion dataset is downloaded from Kaggle.

### 2. Data Loading

The dataset is loaded into a Pandas DataFrame for preprocessing and analysis.

### 3. Data Cleaning

Several preprocessing techniques are applied:

#### Text Normalization

- Convert text to lowercase

#### Remove Punctuation

Example:

```text
Hello!!!
```

becomes

```text
hello
```

#### Remove URLs

Example:

```text
https://example.com
```

is removed.

#### Remove HTML Tags

Example:

```html
<p>Hello</p>
```

becomes

```text
Hello
```

#### Remove Emojis

Non-ASCII emoji characters are removed.

#### Remove Stopwords

Common words such as:

```text
the
is
a
an
```

are removed to improve model performance.

---

### 4. Label Encoding

Emotion labels are converted into numerical values for model training.

Example:

```text
joy      → 0
sadness  → 1
anger    → 2
fear     → 3
love     → 4
surprise → 5
```

---

### 5. Train-Test Split

The dataset is divided into:

- Training Data (80%)
- Testing Data (20%)

This helps evaluate model performance on unseen data.

---

## 🧠 Feature Engineering

Two NLP feature extraction techniques are used.

### TF-IDF Vectorization

TF-IDF measures how important a word is within a document compared to the entire dataset.

Benefits:

- Reduces influence of common words
- Highlights informative words
- Works well with text classification

---

### Bag of Words (BoW)

Converts text into numerical vectors based on word frequency.

Benefits:

- Simple
- Easy to understand
- Effective baseline model

---

## 🤖 Model Used

### Logistic Regression

A supervised machine learning algorithm commonly used for text classification.

Advantages:

- Fast training
- High interpretability
- Strong baseline performance

---

## 📈 Evaluation Metrics

The model is evaluated using:

### Accuracy Score

Measures overall prediction correctness.

### Classification Report

Provides:

- Precision
- Recall
- F1 Score

for each emotion class.

---

## 🚀 Results

Two separate models are trained:

### Logistic Regression + Bag of Words

Used as a baseline NLP model.

### Logistic Regression + TF-IDF

Used for improved text representation and performance.

The project compares both approaches to determine the better feature extraction method.

---

## 📚 Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-Learn
- Matplotlib
- Seaborn
- KaggleHub

---

# Project 2: Prompt Engineering-Based Sentiment Analysis using Gemini

## 🎯 Objective

The goal of this project is to perform sentiment analysis using Google's Gemini Large Language Model through Prompt Engineering techniques.

Instead of training a machine learning model, carefully designed prompts guide the LLM to generate sentiment predictions.

---

## 🧠 What is Prompt Engineering?

Prompt Engineering is the process of designing instructions that help Large Language Models produce accurate and reliable outputs.

Rather than training a model, we provide structured examples and reasoning steps.

---

## 🤖 Model Used

### Gemini 2.5 Flash Lite

The project utilizes:

- Google Gemini API
- LangChain Integration
- ChatGoogleGenerativeAI

Benefits:

- Fast response generation
- High-quality reasoning
- Minimal infrastructure requirements

---

## 📋 Task Performed

The model analyzes customer reviews and predicts:

- Positive Sentiment
- Negative Sentiment
- Neutral Sentiment

---

## 🔄 Workflow

### 1. API Configuration

The Gemini API key is securely loaded and configured.

### 2. Model Initialization

The Gemini model is initialized using LangChain.

### 3. Customer Review Collection

A set of sample customer reviews is provided.

Examples include:

```text
The product quality is amazing and delivery was very fast.
```

```text
Terrible customer support and poor build quality.
```

```text
Average product. Nothing special but not bad either.
```

---

### 4. Few-Shot Prompting

The project uses Few-Shot Prompting.

The prompt contains:

- Instructions
- Examples
- Expected outputs

This helps the model understand the required task.

---

### 5. Chain-of-Thought Reasoning

The model follows a step-by-step reasoning process:

1. Identify positive phrases
2. Identify negative phrases
3. Detect mixed sentiment
4. Determine final sentiment
5. Explain reasoning

This improves transparency and interpretability.

---

## 📈 Output Format

For each review, the model provides:

### Positive Indicators

Positive phrases found in the review.

### Negative Indicators

Negative phrases found in the review.

### Sentiment Classification

One of:

- Positive
- Negative
- Neutral

### Reasoning

Step-by-step explanation of the prediction.

---

## 📚 Technologies Used

- Python
- Google Gemini API
- LangChain
- Prompt Engineering
- Few-Shot Learning
- Chain-of-Thought Prompting

---

# Comparison: Machine Learning vs Prompt Engineering

| Feature | Machine Learning | Prompt Engineering |
|----------|----------------|-------------------|
| Training Required | Yes | No |
| Dataset Required | Yes | Minimal |
| Model Building | Required | Not Required |
| Feature Engineering | Required | Not Required |
| Explainability | Moderate | High |
| Development Time | Higher | Lower |
| Scalability | High | Depends on API |
| Cost | Lower after training | API Usage Cost |

---

# Key Learning Outcomes

Through these projects, the following concepts are explored:

### NLP Fundamentals

- Text Cleaning
- Tokenization
- Stopword Removal

### Feature Engineering

- TF-IDF
- Bag of Words

### Machine Learning

- Logistic Regression
- Model Evaluation

### Generative AI

- Gemini API
- LangChain Integration

### Prompt Engineering

- Few-Shot Prompting
- Chain-of-Thought Reasoning
- Sentiment Analysis
---

# Conclusion

This repository demonstrates two different approaches to solving text classification problems:

1. A traditional Machine Learning pipeline using TF-IDF, Bag of Words, and Logistic Regression for emotion detection.
2. A modern Generative AI approach using Gemini and Prompt Engineering for sentiment analysis.

Together, these projects provide a comprehensive understanding of both classical NLP techniques and emerging LLM-based workflows for text analytics.
