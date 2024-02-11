from PyQt5.QtWidgets import *
from NB_arayuz import Ui_Form
import pandas as pd
import sys
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
class NB(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.BtnEgit.clicked.connect(self.naive)
        
        
        
    def naive(self):
        test_size = float(self.ui.TxtTestSize.text())
        def naive(test_size):
            import pandas as pd
            veriSet= pd.read_csv(r"C:\Users\doguk\Desktop\ML\Epileptic Seizure Recognition.csv")
            X = veriSet.iloc[:,1:-1].values
            y = veriSet.iloc[:,-1:].values
            from sklearn.datasets import make_classification
            X, y = make_classification(n_samples=10000, n_features=180, n_informative=10, n_classes=6, random_state=42)
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size)
            from sklearn.naive_bayes import GaussianNB
            NB = GaussianNB()
            NB.fit(X_train, y_train)
            y_predict = NB.predict(X_test)    
            from sklearn.metrics import accuracy_score
            from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
            cm = confusion_matrix(y_test,y_predict)
            accuracy = accuracy_score(y_test, y_predict)
            from sklearn.metrics import accuracy_score, precision_score, recall_score
            precision = precision_score(y_test, y_predict,average='weighted')
            recall = recall_score(y_test,y_predict,average='weighted')
            specificity = recall_score(y_test,y_predict,average='weighted')
            print({"Confusion matrix":cm,"Accuracy":accuracy,"Precision":precision,"recall":recall,"Specificity":specificity}) 
            import seaborn as sns  
            #sns.barplot(x=feature_scores, y=feature_scores.index)
            accuracy_str = f"Accuracy: {accuracy:.2f}"  # Format to 2 decimal places
            precision_str = f"Precision: {precision:.2f}"
            recall_str = f"Recall: {recall:.2f}"
            specificity_str = f"Specificity: {specificity:.2f}"
            self.ui.LblAccuracy.setText(accuracy_str)
            self.ui.LblPrecision.setText(precision_str)
            self.ui.LblRecall.setText(recall_str)
            self.ui.LblSpecificity.setText(specificity_str)
            
            print("Confusion Matrix:\n", cm)

            # Visualize the confusion matrix using Seaborn heatmap
            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(cmap="Blues", ax=None)
            plt.savefig("C:\\Users\\doguk\\Desktop\ML\\NB_cm_goruntu.jpeg")
            cm_image = ("C:\\Users\\doguk\\Desktop\ML\\NB_cm_goruntu.jpeg")
            pixmap = QPixmap(cm_image)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
            
            self.ui.TableX_test.setRowCount(len(X_train) + len(X_test))
            self.ui.TableX_test.setColumnCount(2)
            self.ui.TableX_test.setHorizontalHeaderLabels(['Index', 'Value'])
            
            self.ui.TableX_train.setRowCount(len(X_train) + len(X_train))
            self.ui.TableX_train.setColumnCount(2)
            self.ui.TableX_train.setHorizontalHeaderLabels(['Index', 'Value'])
            
            self.ui.TableY_train.setRowCount(len(y_train) + len(y_train))
            self.ui.TableY_train.setColumnCount(2)
            self.ui.TableY_train.setHorizontalHeaderLabels(['Index', 'Value'])
            
            self.ui.TableY_test.setRowCount(len(y_test) + len(y_test))
            self.ui.TableY_test.setColumnCount(2)
            self.ui.TableY_test.setHorizontalHeaderLabels(['Index', 'Value'])
            
            

            row_index_train = 0
            row_index_test = 0
            row_index_y_train = 0
            row_index_y_test = 0
            for i, x_train_item in enumerate(X_train):
                self.ui.TableX_train.setItem(row_index_train, 0, QTableWidgetItem(f"X_train[{i}]"))
                self.ui.TableX_train.setItem(row_index_train, 1, QTableWidgetItem(str(x_train_item)))
                row_index_train += 1
            
            for i, x_test_item in enumerate(X_test):
                self.ui.TableX_test.setItem(row_index_test, 0, QTableWidgetItem(f"X_test[{i}]"))
                self.ui.TableX_test.setItem(row_index_test, 1, QTableWidgetItem(str(x_test_item)))
                row_index_test += 1
            
            for i, y_test_item in enumerate(y_test):
                self.ui.TableY_test.setItem(row_index_y_test, 0, QTableWidgetItem(f"Y_test[{i}]"))
                self.ui.TableY_test.setItem(row_index_y_test, 1, QTableWidgetItem(str(y_test_item)))
                row_index_y_test += 1
            for i, y_train_item in enumerate(y_train):
                self.ui.TableY_train.setItem(row_index_y_train, 0, QTableWidgetItem(f"Y_train[{i}]"))
                self.ui.TableY_train.setItem(row_index_y_train, 1, QTableWidgetItem(str(y_train_item)))
                row_index_y_train += 1
            ###saving model with joblib
            #NB_classifier = 'NB_trained_model.sav'
            #NB_classifier.save('knn_trained_model.sav')
        return naive(test_size)


        
                
 
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = NB()
    pencere.show()
    sys.exit(app.exec_())

            