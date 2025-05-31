# Практическая работа №1. Датасет Wine Quality

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy import stats
import numpy as np
from sklearn.preprocessing import StandardScaler

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (accuracy_score)

import warnings

warnings.filterwarnings('ignore')

# Загрузка данных.
data = pd.read_csv('WineQT.csv')

# Первичный анализ
print(f"Размерность данных: {data.shape}")
print(f"\nСтатистическое описание: \n{data.describe()}")
print(f"\nТипы данных: \n{data.dtypes}")
print(f"\nПроверка пропущенных значений: \n{data.isnull().sum()}")

# Распределение целевой переменной
plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=data)
plt.title('Распределение качества вина')
plt.show()

# Корреляционный анализ
corr_matrix = data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Матрица корреляций')
plt.show()

# Разделение выборок
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
          'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
          'pH', 'sulphates', 'alcohol']]
y = data['quality']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)

# Работа с пропусками
imputer = SimpleImputer(strategy='median')
X_train = imputer.fit_transform(X_train)
X_val = imputer.transform(X_val)
X_test = imputer.transform(X_test)

# Работа с выбросами
z_scores = stats.zscore(data.drop('quality', axis=1))
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
data = data[filtered_entries]

# Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# 1. Baseline модели
print("\n=== Baseline модели ===")

# Dummy Classifier
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train_scaled, y_train)
dummy_pred = dummy.predict(X_test_scaled)
print(f"Dummy Classifier Accuracy: {accuracy_score(y_test, dummy_pred):.4f}")

# Логистическая регрессия
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train_scaled, y_train)
logreg_pred = logreg.predict(X_test_scaled)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, logreg_pred):.4f}")

# Дерево решений
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train_scaled, y_train)
tree_pred = tree.predict(X_test_scaled)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, tree_pred):.4f}")

# 2. Продвинутые классификаторы
print("\n=== Продвинутые классификаторы ===")

random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train_scaled, y_train)
random_forest_pred = tree.predict(X_test_scaled)
print(f"Random Forest Accuracy: {accuracy_score(y_test, random_forest_pred):.4f}")

models = {
    "SVM": SVC(random_state=42),
    "KNN": KNeighborsClassifier(),
    "MLP": MLPClassifier(random_state=42, max_iter=1000)
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, pred)
    print(f"{name} Accuracy: {acc:.4f}")

# Сохранение модели и скейлера
import joblib
joblib.dump(tree, 'wine_quality_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(imputer, 'imputer.pkl')
print("Модель и скейлер сохранены на диск")

