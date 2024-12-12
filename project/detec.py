from utils import load_data

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import warnings

from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")

(feature, labels) = load_data()

x_train, x_test, y_train, y_test = train_test_split(feature, labels, test_size = 0.1)

categories = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip', 'orchid', 'lavender', 'hydrangea']

model = tf.keras.models.load_model('my_model.h5')

model.evaluate(x_test, y_test, verbose=True)

prediction =  model.predict(x_test)
plt.figure(figsize=(9, 9))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_test[i])
    plt.xlabel('Actual: '+categories[y_test[i]]+'\n'+'Predicted: '+
               categories[np.argmax(prediction[i])])
    
    plt.xticks([])

plt.savefig('plot_4.png')