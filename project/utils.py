import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import  pickle
import warnings

warnings.filterwarnings("ignore")

data_dir = '../vaaz_model/data/flowers'

categories = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip', 'orchid', 'lavender', 'hydrangea']

data = []

def make_data():
    for category in  categories:
        path = os.path.join(data_dir, category)
        label = categories.index(category)

        for img_name in os.listdir(path):
            image_path = os.path.join(path, img_name)
            image = cv2.imread(image_path)

            try:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (224, 224))

                image = np.array(image, dtype=np.float32)

                data.append([image, label])

            except Exception as e:
                pass

    print(len(data))

    pik = open('data.pickle', 'wb')
    pickle.dump(data, pik)
    pik.close()

make_data()

def load_data():
    pick = open('data.pickle', 'rb')
    data =  pickle.load(pick)
    pick.close()

    feature = []
    labels = []

    for img, label in data:
        feature.append(img)
        labels.append(label)

    feature = np.array(feature, dtype=np.float32)
    labels = np.array(labels)

    feature = feature/255.0

    return [feature, labels]