import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

class NaiveBayes:
    def __init__(self):
        self.prior = None
        self.likelihood = None
        self.classes = None
        self.vocabulary = None

    def fit(self, X, y):
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(X)
        self.vocabulary = vectorizer.vocabulary_
        self.classes, y_count = np.unique(y, return_counts=True)
        self.prior = y_count / y_count.sum()
        self.likelihood = np.zeros((len(self.classes), X.shape[1]))
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.likelihood[i, :] = (X_c.sum(axis=0) + 1) / (X_c.shape[0] + 2)
        
    def predict_proba(self, X):
        vectorizer = CountVectorizer(vocabulary=self.vocabulary)
        X = vectorizer.fit_transform(X)
        log_prior = np.log(self.prior)
        log_likelihood = np.log(self.likelihood)
        log_posterior = log_prior + X.dot(log_likelihood.T)
        # shift the values to avoid numerical underflow
        log_posterior -= log_posterior.max(axis=1)[:, np.newaxis]
        posterior = np.exp(log_posterior)
        return posterior / posterior.sum(axis=1)[:, np.newaxis]
