"""
Decision Tree trained on all highs (64) and 64 low injures
Accuracy: 48.3% on a max_depth=4 tree
Dataset: FinalizedDatasetTrimmed2
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from sklearn import svm
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

full_data = pd.read_csv("FinalizedDataset.csv")
trimmed_data = pd.read_csv("FinalizedDatasetTrimmed2.csv")

# def search_for_nan(row):
#     for item in row:
#         if type(item) != type(" ") and type(item) != type(1): #and type(item) != type(1.0):
#             print(item)

# data.apply(search_for_nan, axis=1)

feature_cols = ["Day", "Month", "Year", "Enumerated Division", "Enumerated Area","Enumerated Rank","Enumerated Sex","Enumerated Carrier"]
#"Enumerated Event Severity","Enumerated Injury Severity"

# X = data[feature_cols]
# y = data["Enumerated Event Severity"] #make sure one of the columns is called label

X_train = trimmed_data[feature_cols] 
y_train = trimmed_data["Enumerated Event Severity"]
X_test = full_data[feature_cols]
y_test = full_data["Enumerated Event Severity"]
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=5)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=4) #criteriion="entropy, max_depth=3" #98.8% Accuracy
#clf = svm.SVC()  98.8% Accuracy
#clf = NearestCentroid()  68% Accuracy
#clf = GaussianNB() 98.8% Accuracy
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

#Display the decision tree
event_severity_classes = ['1','2']
injury_severity_classes = ['1','3', '4', '5', '6', '7', '8']
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, 
    filled=True, rounded=True, 
    special_characters=True, feature_names=feature_cols, class_names=event_severity_classes)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('decision_tree3.png')
Image(graph.create_png())