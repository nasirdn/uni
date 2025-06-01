import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# 1. Загрузка данных
df = pd.read_excel('dlia_studentov.xlsx')

# 2. Предварительный анализ данных
print("Размерность данных:", df.shape)
print("\nПервые 5 строк:")
print(df.head())
print("\nИнформация о данных:")
print(df.info())
print("\nПропущенные значения:")
print(df.isnull().sum())

# 3. Обработка данных
# Удаление ненужных столбцов
df = df.drop(['ID', 'Время создания'], axis=1)

# Кодирование бинарных признаков
binary_columns = df.columns[2:]  # Все столбцы кроме факультета и платформы
le = LabelEncoder()
for col in binary_columns:
    df[col] = le.fit_transform(df[col])

# Кодирование платформы
df['Какая платформа для обучения дисциплине "ИНФОКОММУНИКАЦИОННЫЕ ТЕХНОЛОГИИ" использовалась?'] = \
    le.fit_transform(df['Какая платформа для обучения дисциплине "ИНФОКОММУНИКАЦИОННЫЕ ТЕХНОЛОГИИ" использовалась?'])

# Сохранение факультетов для последующего анализа
faculties = df['На каком факультете/в каком институте Вы обучаетесь?']
df = df.drop('На каком факультете/в каком институте Вы обучаетесь?', axis=1)

# 4. Визуализация данных
# Распределение ответов по вопросам
plt.figure(figsize=(15, 20))
for i, col in enumerate(binary_columns, 1):
    plt.subplot(6, 4, i)
    sns.countplot(x=col, data=df)
    plt.title(col)
    plt.xticks([0, 1], ['Нет', 'Да'])
plt.tight_layout()
plt.show()

# 5. Анализ корреляций
# Матрица корреляций для бинарных признаков
corr_matrix = df.corr()
plt.figure(figsize=(15, 12))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Матрица корреляций")
plt.show()

# 6. Снижение размерности с помощью t-SNE и PCA
# Подготовка данных
X = df.values

# Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# t-SNE с 2 компонентами
tsne = TSNE(n_components=2, random_state=42)
embedding_tsne = tsne.fit_transform(X_scaled)

# PCA с 2 компонентами
pca = PCA(n_components=2, random_state=42)
embedding_pca = pca.fit_transform(X_scaled)

# Визуализация t-SNE
plt.figure(figsize=(10, 8))
plt.scatter(embedding_tsne[:, 0], embedding_tsne[:, 1], s=5)
plt.title('t-SNE проекция данных (2D)')
plt.xlabel('Компонента 1')
plt.ylabel('Компонента 2')
plt.show()

# Визуализация PCA
plt.figure(figsize=(10, 8))
plt.scatter(embedding_pca[:, 0], embedding_pca[:, 1], s=5)
plt.title('PCA проекция данных (2D)')
plt.xlabel('Главная компонента 1')
plt.ylabel('Главная компонента 2')
plt.show()


# 7. Кластеризация
# Функция для оценки кластеризации
def evaluate_clustering(X, labels):
    if len(set(labels)) > 1:  # Для метрик нужно хотя бы 2 кластера
        silhouette = silhouette_score(X, labels)
        davies_bouldin = davies_bouldin_score(X, labels)
        return silhouette, davies_bouldin
    return None, None


# Метод локтя для K-Means
inertia = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia, marker='o')
plt.title('Метод локтя для K-Means')
plt.xlabel('Количество кластеров')
plt.ylabel('Инерция')
plt.show()

# Выбираем оптимальное количество кластеров (например, 4)
n_clusters = 4

# K-Means
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=n_clusters)
agg_labels = agg.fit_predict(X_scaled)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)

# Gaussian Mixture Models
gmm = GaussianMixture(n_components=n_clusters, random_state=42)
gmm_labels = gmm.fit_predict(X_scaled)

# Оценка кластеризаций
results = []
for name, labels in [('K-Means', kmeans_labels),
                     ('Agglomerative', agg_labels),
                     ('DBSCAN', dbscan_labels),
                     ('GMM', gmm_labels)]:
    silhouette, davies_bouldin = evaluate_clustering(X_scaled, labels)
    results.append({
        'Метод': name,
        'Silhouette Score': silhouette,
        'Davies-Bouldin Index': davies_bouldin,
        'Количество кластеров': len(set(labels))
    })

results_df = pd.DataFrame(results)
print("\nРезультаты кластеризации:")
print(results_df)

# Выбираем лучший метод (например, K-Means)
best_labels = kmeans_labels

# 8. Анализ кластеров
df['Cluster'] = best_labels

# Средние значения по кластерам
cluster_means = df.groupby('Cluster').mean()
print("\nСредние значения по кластерам:")
print(cluster_means)

# Визуализация кластеров в 2D t-SNE
plt.figure(figsize=(10, 8))
for cluster in sorted(df['Cluster'].unique()):
    mask = df['Cluster'] == cluster
    plt.scatter(embedding_tsne[mask, 0], embedding_tsne[mask, 1],
                label=f'Cluster {cluster}', s=5)
plt.title('Кластеры на t-SNE проекции (2D)')
plt.xlabel('Компонента 1')
plt.ylabel('Компонента 2')
plt.legend()
plt.show()

# Визуализация кластеров в 2D PCA
plt.figure(figsize=(10, 8))
for cluster in sorted(df['Cluster'].unique()):
    mask = df['Cluster'] == cluster
    plt.scatter(embedding_pca[mask, 0], embedding_pca[mask, 1],
                label=f'Cluster {cluster}', s=5)
plt.title('Кластеры на PCA проекции (2D)')
plt.xlabel('Главная компонента 1')
plt.ylabel('Главная компонента 2')
plt.legend()
plt.show()


# Радарные диаграммы для кластеров
def plot_radar_chart(cluster_data, features, title):
    angles = np.linspace(0, 2 * np.pi, len(features), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    for cluster, values in cluster_data.iterrows():
        data = values[features].values
        data = np.concatenate((data, [data[0]]))
        ax.plot(angles, data, 'o-', linewidth=2, label=f'Cluster {cluster}')

    ax.set_thetagrids(angles[:-1] * 180 / np.pi, features)
    ax.set_title(title)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.show()


# Выбираем наиболее информативные признаки (первые 8 по важности)
important_features = cluster_means.std().sort_values(ascending=False).head(8).index
plot_radar_chart(cluster_means, important_features, 'Профили кластеров по важным признакам')

# 9. Распределение кластеров по факультетам
faculty_cluster = pd.crosstab(faculties, df['Cluster'], normalize='index')
faculty_cluster.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Распределение кластеров по факультетам')
plt.ylabel('Доля студентов')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Кластер')
plt.tight_layout()
plt.show()

# 10. Интерпретация кластеров
# Даем названия кластерам на основе их характеристик
cluster_names = {}
for cluster in sorted(df['Cluster'].unique()):
    cluster_data = cluster_means.loc[cluster]
    # Определяем характеристики кластера
    characteristics = []
    for feature, value in cluster_data.items():
        if value > 0.7:
            characteristics.append(feature + " (да)")
        elif value < 0.3:
            characteristics.append(feature + " (нет)")

    # Формируем название кластера
    name = f"Кластер {cluster}: " + ", ".join(characteristics[:3]) + "..."
    cluster_names[cluster] = name
    print(name)

# Сохранение результатов
df['Факультет'] = faculties
df['Cluster_Name'] = df['Cluster'].map(cluster_names)
df.to_excel('clustered_students.xlsx', index=False)