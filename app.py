from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['DEBUG'] = True

model = tf.keras.models.load_model('fraud_model.h5', compile=False)

# Compile the model manually with the same optimizer, loss, and metrics used during training
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='binary_crossentropy',
    metrics=[
        'accuracy',
        tf.keras.metrics.AUC(name='auc')
    ]
)

# Load the tokenizer and scaler
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(pd.read_csv('Fraud.csv', nrows=50000)['nameDest'])
scaler = StandardScaler()

# Sample data for fitting the scaler
sample_data = pd.DataFrame({
    'amount': [100.0],
    'oldbalanceOrg': [1000.0],
    'newbalanceOrig': [900.0],
    'oldbalanceDest': [2000.0],
    'newbalanceDest': [2500.0]
})

scaler.fit(sample_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.form
            # Preprocess the input data
            input_data = preprocess_input(data)
            # Make the prediction
            prediction = predict_fraud(input_data)
            return render_template('index.html', prediction=prediction)
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')

def preprocess_input(data):
    X = pd.DataFrame({
        'amount': [float(data['amount'])],
        'oldbalanceOrg': [float(data['oldbalanceOrg'])],
        'newbalanceOrig': [float(data['newbalanceOrig'])],
        'oldbalanceDest': [float(data['oldbalanceDest'])],
        'newbalanceDest': [float(data['newbalanceDest'])],
    })

    # Tokenize and pad the customer column
    customers = tokenizer.texts_to_sequences([data['nameDest']])
    customers = tf.keras.preprocessing.sequence.pad_sequences(customers, maxlen=1)

    # Scale the input features
    X = pd.DataFrame(scaler.transform(X), columns=X.columns)

    # One-hot encode the transaction type
    transaction_type = data['type']
    type_columns = ['tp_CASH_OUT', 'tp_TRANSFER', 'tp_PAYMENT', 'tp_DEBIT', 'tp_CASH_IN']
    type_encoded = [0] * len(type_columns)
    if transaction_type in type_columns:
        type_encoded[type_columns.index(transaction_type)] = 1
    X = pd.concat([X, pd.DataFrame([type_encoded], columns=type_columns)], axis=1)

    return X, customers

def predict_fraud(input_data):
    X, customers = input_data
    prediction = model.predict([X.values, customers])
    fraud_probability = prediction[0][0]
    if fraud_probability >= 0.5:
        return 'Fraud'
    else:
        return 'Not Fraud'   

if __name__ == '__main__':
    app.run()
