from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.metrics import confusion_matrix, classification_report

app = Flask(__name__)

def onehot_encode(df, column, prefix):
    # Your onehot_encode function code

 def preprocess_inputs(df):
    # Your preprocess_inputs function code

  @app.route('/') 
  def matrix():
    # Rest of your code...

    data = pd.read_csv('Fraud.csv', nrows=50000)
    X_train, X_test, customers_train, customers_test, y_train, y_test = preprocess_inputs(data)

    # Load the saved model
    model = tf.keras.models.load_model('fraud_model.h5')

    # Perform predictions
    y_true = np.array(y_test)
    y_pred = np.squeeze(model.predict([X_test, customers_test]))
    y_pred = (y_pred >= 0.5).astype(np.int)

    # Calculate confusion matrix and classification report
    cm = confusion_matrix(y_true, y_pred)
    clr = classification_report(y_true, y_pred, target_names=["Not Fraud", "Fraud"])

    # Plot confusion matrix
    plt.figure(figsize=(8, 8))
    sns.heatmap(cm, annot=True, vmin=0, fmt='g', cbar=False, cmap='Blues')
    plt.xticks(np.arange(2) + 0.5, ["Not Fraud", "Fraud"])
    plt.yticks(np.arange(2) + 0.5, ["Not Fraud", "Fraud"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.savefig('static/confusion_matrix.png')  # Save the confusion matrix plot as a static file

    # Render the template with classification report and confusion matrix image path
    return render_template('matrix.html', classification_report=clr, confusion_matrix_image='static/confusion_matrix.png')

if __name__ == '__main__':
    app.run(debug=True)
