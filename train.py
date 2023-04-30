import pandas as pd
from model import NaiveBayes
import numpy as np
import pickle

# 读取CSV文件
train_data = pd.read_csv('data.csv', names=['text', 'label'])
X_train = train_data['text']
y_train = train_data['label']
y_train=np.ravel(y_train)
print('read data ok')

# 训练贝叶斯分类器
classifier = NaiveBayes()
classifier.fit(X_train, y_train)
with open('model.pkl', 'wb') as f:
    pickle.dump(classifier, f)
print('training ok')