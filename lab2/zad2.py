from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')

pca_iris = PCA(n_components=3).fit(X)

print(pca_iris.explained_variance_ratio_)

# print(pca_iris.components_)

transformed_data = pca_iris.transform(X)
# print(transformed_data)

total_variance = sum(pca_iris.explained_variance_)

cumulative_variance = 0
components_to_keep = 0

for var in pca_iris.explained_variance_:
    cumulative_variance += var
    components_to_keep += 1
    if cumulative_variance / total_variance >= 0.95:
        break

print("liczba kolumn które można usunąć: ", len(X.columns) - components_to_keep)



if components_to_keep == 2:
    plt.figure()
    for i, target_name in enumerate(iris.target_names):
        plt.scatter(transformed_data[y == i, 0], transformed_data[y == i, 1], label=target_name)
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.title('PCA plot')
    plt.legend()
    plt.savefig('lol1.png') 
elif components_to_keep == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i, target_name in enumerate(iris.target_names):
        ax.scatter(transformed_data[y == i, 0], transformed_data[y == i, 1], transformed_data[y == i, 2], label=target_name)
    ax.set_xlabel('PCA1')
    ax.set_ylabel('PCA2')
    ax.set_zlabel('PCA3')
    ax.set_title('PCA plot')
    ax.legend()
    plt.savefig('lol2.png') 


X_pca = pca_iris.fit_transform(X)
print(pd.DataFrame(X_pca, columns=['PC1', 'PC2', 'PC3']))