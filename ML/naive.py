import pandas as pd
veriSet= pd.read_csv(r"C:\Users\doguk\Desktop\ML\Epileptic Seizure Recognition.csv")
X = veriSet.iloc[:,1:-1].values
y = veriSet.iloc[:,-1:].values
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=10000, n_features=180, n_informative=10, n_classes=6, random_state=42)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
from sklearn.naive_bayes import GaussianNB
NB = GaussianNB()
NB.fit(X_train, y_train)
y_predict = NB.predict(X_test)    
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict)
accuracy = accuracy_score(y_test, y_predict)
from sklearn.metrics import accuracy_score, precision_score, recall_score
precision = precision_score(y_test, y_predict,average='weighted')
recall = recall_score(y_test,y_predict,average='weighted')
specificity = recall_score(y_test,y_predict,average='weighted')
print({"Confusion matrix":cm,"Accuracy":accuracy,"Precision":precision,"recall":recall,"Specificity":specificity}) 
import seaborn as sns  
#sns.barplot(x=feature_scores, y=feature_scores.index)
import matplotlib.pyplot as plt
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features") 
plt.show()

#rfc_classifier = 'rfc_trained_model.sav'
import joblib
#joblib.dump(rfc, rfc_classifier)