from sklearn.model_selection import train_test_split
import csv

header = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]

with open("wine.data.csv", "r") as f:
    rows = list(csv.reader(f))
    train, test = train_test_split(rows, test_size = 0.2, random_state = 0)
    train.insert(0, header)
    test.insert(0, header)

with open("train.csv", "w", newline = "") as f:
    csv.writer(f).writerows(train)

with open("test.csv", "w", newline = "") as f:
    csv.writer(f).writerows(test)