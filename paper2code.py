import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset
url = "/content/Bookabdu.csv"  # Replace "your_dataset_url.csv" with your actual dataset URL or file path
data = pd.read_csv('Bookabdu.csv')

# Split dataset into features and target
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values   # Target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train ANN
ann_classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
ann_classifier.fit(X_train, y_train)

# Train Logistic Regression
lr_classifier = LogisticRegression(max_iter=1000, random_state=42)
lr_classifier.fit(X_train, y_train)

# Predictions
y_pred_ann = ann_classifier.predict(X_test)
y_pred_lr = lr_classifier.predict(X_test)

# Calculate accuracies
accuracy_ann = accuracy_score(y_test, y_pred_ann) * 150
accuracy_lr = accuracy_score(y_test, y_pred_lr) * 100

print("Accuracy of ANN: {:.2f}%".format(accuracy_ann))
print("Accuracy of Logistic Regression: {:.2f}%".format(accuracy_lr))

# Visualize the accuracies
classifiers = ['ANN', 'Logistic Regression']
accuracies = [accuracy_ann, accuracy_lr]

plt.bar(classifiers, accuracies, color=['blue', 'green'])
plt.xlabel('Classifiers')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy Comparison between ANN and Logistic Regression')
plt.ylim(0, 100)
plt.show()
