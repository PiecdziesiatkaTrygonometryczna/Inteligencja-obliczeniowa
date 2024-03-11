import pandas as pd
df = pd.read_csv("iris.csv")
# print(df)

from sklearn.model_selection import train_test_split

# podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7, 
random_state=285745)

# print(test_set)
# print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# print(train_inputs)
# print(train_classes)
# print(test_inputs)
# print(test_classes)

def classify_iris(sl, sw, pl, pw):
 if sl < 5.5:
    return("setosa")
 elif pw <= 1.5:
    return("versicolor")
 else:
    return("virginica")
 
good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_inputs[i, 0], test_inputs[i, 1], test_inputs[i, 2], test_inputs[i, 3]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/len*100, "%")

# print(train_set)
