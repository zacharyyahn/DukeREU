import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

train_data = pd.read_csv("FinalizedDatasetTrimmed2.csv")
data = pd.read_csv("FinalizedDataset2.csv")

# def search_for_nan(row):
#     for item in row:
#         if type(item) != type(" ") and type(item) != type(1): #and type(item) != type(1.0):
#             print(item)

# data.apply(search_for_nan, axis=1)

print(data["Enumerated Event Severity"].value_counts())

feature_cols = ["Day", "Month", "Year", "Enumerated Division", "Enumerated Area","Enumerated Rank","Enumerated Sex","Enumerated Carrier"]
#"Enumerated Event Severity","Enumerated Injury Severity"

# X_train = train_data[feature_cols]
# y_train = train_data["Enumerated Event Severity"] #make sure one of the columns is called label
# X_test = test_data[feature_cols]
# y_test = test_data["Enumerated Event Severity"]

X = data[feature_cols]
y = data["Enumerated Event Severity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

tree_clf = DecisionTreeClassifier(criterion="entropy", max_depth=4) #criteriion="entropy, max_depth=3" #98.8% Accuracy
svm_clf = make_pipeline(StandardScaler(), SVC())
knn_clf = KNeighborsClassifier(algorithm="kd_tree", weights="distance") 
nb_clf = GaussianNB()
lr_clf = LogisticRegression(max_iter=2000, solver="newton-cg")

tree_clf = tree_clf.fit(X_train, y_train)
svm_clf = svm_clf.fit(X_train, y_train)
knn_clf = knn_clf.fit(X_train, y_train)
nb_clf = nb_clf.fit(X_train, y_train)
lr_clf = lr_clf.fit(X_train, y_train)

tree_y_pred = tree_clf.predict(X_test)
svm_y_pred = svm_clf.predict(X_test)
knn_y_pred = knn_clf.predict(X_test)
nb_y_pred = nb_clf.predict(X_test)
lr_y_pred = lr_clf.predict(X_test)

print("--------TREE--------")
print("Accuracy: ", metrics.accuracy_score(y_test, tree_y_pred))
print("F1: ", metrics.f1_score(y_test, tree_y_pred))
print("Balanced Accuracy: ", metrics.balanced_accuracy_score(y_test, tree_y_pred))
print("--------KNN--------")
print("Accuracy: ", metrics.accuracy_score(y_test, knn_y_pred))
print("F1: ", metrics.f1_score(y_test, knn_y_pred))
print("Balanced Accuracy: ", metrics.balanced_accuracy_score(y_test, knn_y_pred))
print("--------Bayes--------")
print("Accuracy: ", metrics.accuracy_score(y_test, nb_y_pred))
print("F1: ", metrics.f1_score(y_test, nb_y_pred))
print("Balanced Accuracy: ", metrics.balanced_accuracy_score(y_test, nb_y_pred))
print("--------SVM--------")
print("Accuracy: ", metrics.accuracy_score(y_test, svm_y_pred))
print("F1: ", metrics.f1_score(y_test, svm_y_pred))
print("Balanced Accuracy: ", metrics.balanced_accuracy_score(y_test, svm_y_pred))
print("--------Logistic--------")
print("Accuracy: ", metrics.accuracy_score(y_test, lr_y_pred))
print("F1: ", metrics.f1_score(y_test, lr_y_pred))
print("Balanced Accuracy: ", metrics.balanced_accuracy_score(y_test, lr_y_pred))

#Display the decision tree
event_severity_classes = ['1','2']
injury_severity_classes = ['1','3', '4', '5', '6', '7', '8']
dot_data = StringIO()
export_graphviz(tree_clf, out_file=dot_data, 
    filled=True, rounded=True, 
    special_characters=True, feature_names=feature_cols, class_names=event_severity_classes)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('decision_tree4.png')
Image(graph.create_png())