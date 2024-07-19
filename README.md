# Fraud Detection Project

This project aims to develop a fraud detection system for financial transactions using machine learning techniques. The model is designed to classify transactions as fraudulent or non-fraudulent based on various features.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
  - [Model Training](#model-training)
  - [Prediction](#prediction)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview
Credit card fraud is a significant issue worldwide, posing financial losses and security concerns for individuals and institutions. This project focuses on detecting fraudulent transactions in real-time by leveraging machine learning models trained on historical transaction data.

## Dataset
The dataset used for this project is from Kaggle and contains the following columns:
- `step`: Time step of the transaction
- `type`: Type of transaction (e.g., PAYMENT, TRANSFER, CASH_OUT, etc.)
- `amount`: Transaction amount
- `nameOrig`: Customer who initiated the transaction
- `oldbalanceOrg`: Initial balance before the transaction
- `newbalanceOrig`: New balance after the transaction
- `nameDest`: Recipient of the transaction
- `oldbalanceDest`: Initial balance of the recipient before the transaction
- `newbalanceDest`: New balance of the recipient after the transaction
- `isFraud`: Whether the transaction is fraudulent (1) or not (0)
- `isFlaggedFraud`: Whether the transaction is flagged as fraudulent by the system (1) or not (0)

## Installation
Clone the repository:
```bash
git clone https://github.com/OtaoDavis/Fraudify.git
cd fraud-detection
```

## Install Requirements

```bash
pip install -r requirements.txt
```
# Usage
## Model Training
To train the model, run the following command:

```bash
jupyter notebook train.ipynb
```
# Results
The model achieves high accuracy in detecting fraudulent transactions with a low false positive rate. Detailed results and performance metrics can be found in the results directory.

