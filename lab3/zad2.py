import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")


# a


train_set, test_set = train_test_split(df, train_size=0.7, random_state=483483)

# print(train_set)
# print(test_set)

train_inputs = train_set.drop('species', axis=1)
train_classes = train_set['species']
test_inputs = test_set.drop('species', axis=1)
test_classes = test_set['species']

# b

tree_clf = DecisionTreeClassifier(random_state=483483)



# c

tree_clf.fit(train_inputs, train_classes)



# d

tree_text = export_text(tree_clf, feature_names=list(train_inputs.columns))
# print(tree_text)

plt.figure(figsize=(12, 8))
plot_tree(tree_clf, feature_names=list(train_inputs.columns), class_names=tree_clf.classes_, filled=True)
plt.savefig("plot.png")


# e

accuracy = tree_clf.score(test_inputs, test_classes)
print("Dokładność klasyfikatora:", accuracy)

predictions = tree_clf.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)
print("Macierz błędów:")
print(conf_matrix)

# Dokładność klasyfikatora: 0.9777777777777777
# Macierz błędów:
# [[12  0  0]
#  [ 0 11  1]
#  [ 0  0 21]]