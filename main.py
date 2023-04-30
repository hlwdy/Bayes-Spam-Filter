from sklearn.model_selection import train_test_split
import pandas as pd
from model import NaiveBayes
import numpy as np
import pickle

X_test = ['']

with open('test.txt', 'rb') as f:
    X_test = [f.read().decode()]

# 训练贝叶斯分类器
classifier = NaiveBayes()
with open('model.pkl', 'rb') as f:
    classifier = pickle.load(f)
print('load model ok')

print('test data:')
print(X_test)
# 在测试集上评估模型
res = classifier.predict_proba(X_test)
print("result:", res)