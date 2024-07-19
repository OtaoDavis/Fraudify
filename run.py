# Force TensorFlow to use CPU only
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# Now you can safely import TensorFlow and other libraries
import tensorflow as tf
from flaskml import app

# Ensure the optimizer configuration does not include 'weight_decay' or is correctly configured
# Example: optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

if __name__ == '__main__':
    app.run(debug=True)