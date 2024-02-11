from PyQt5.QtWidgets import *
from knn_arayuz import Ui_Form
import pandas as pd
import numpy as np 
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class KNN(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.BtnDYukle.clicked.connect(self.yukle)
       
        #komsuluk = int(self.ui.komsuluk_al.text())
        self.ui.TxtEgit.clicked.connect(self.knn_algoritmasi_calistir)
                
    def knn_algoritmasi_calistir(self):
        komsuluk = int(self.ui.TxtKomsulukDegeri.text())
        test_degeri = float(self.ui.TxtTestOrani.text())
        def knn_algoritmasi_calistir(test_degeri,komsuluk):
            data_set= pd.read_csv(r"C:\Users\doguk\Desktop\ML\Epileptic Seizure Recognition.csv")
            #data_set.head()
            ndata=data_set.isnull().sum()
            data_set = data_set.replace(0, pd.NA).dropna()
            #######datada gezinmek
            X = data_set.iloc[:,1:-1].values
            y = data_set.iloc[:,-1:].values
            y[y>1] = 0
            X.shape
            y.shape

            #####train-test split
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_degeri,shuffle=True) #disaridan bilgi alinan yer

            #####normalizasyon
            scaler_minmax = MinMaxScaler()
            scaled_data = scaler_minmax.fit_transform(X)
            scaler = StandardScaler()
            scaler.fit(X_train)
            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test) 

            ###model fit
            neighbor = komsuluk
            knn_model = KNeighborsClassifier(n_neighbors=neighbor)#disaridan bilgi alinan yer
            knn_model.fit(X_train, y_train)
            y_predict = knn_model.predict(X_test)

            ####karisiklik matrisi ve metrikler
            cm = confusion_matrix(y_test,y_predict,)
            accuracy = accuracy_score(y_test, y_predict)
            precision = precision_score(y_test, y_predict)
            recall = recall_score(y_test,y_predict)
            f1_s = f1_score(y_test,y_predict)
            specificity = recall_score(y_test,y_predict,pos_label=0)
            accuracy_str = f"Accuracy: {accuracy:.2f}"  # Format to 2 decimal places
            precision_str = f"Precision: {precision:.2f}"
            recall_str = f"Recall: {recall:.2f}"
            f1_s_str = f"F1 Score: {f1_s:.2f}"
            specificity_str = f"Specificity: {specificity:.2f}"
            self.ui.LblAccuracy.setText(accuracy_str)
            self.ui.LblAccuracy.setText(accuracy_str)
            self.ui.LblPrecision.setText(precision_str)
            self.ui.LblRecall.setText(recall_str)
            self.ui.LblF1Score.setText(f1_s_str)
            self.ui.LblSpecificity.setText(specificity_str)
            #print({"Confusion matrix":cm,"Accuracy":accuracy,"Precision":precision,"recall":recall,"Specificity":specificity,"F1_score":f1_s})

    # Print the confusion matrix
            print("Confusion Matrix:\n", cm)

            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(cmap="Blues", ax=None)
            plt.savefig("C:\\Users\\doguk\\Desktop\ML\\KNN_cm_goruntu.jpeg")
            cm_image = ("C:\\Users\\doguk\\Desktop\ML\\KNN_cm_goruntu.jpeg")
            pixmap = QPixmap(cm_image)
            self.ui.label_2.setPixmap(pixmap)
            self.ui.label_2.setScaledContents(True)
            
            ### listeleme
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
            #knn_classifier = 'knn_trained_model.sav'
            #knn_classifier.save('knn_trained_model.sav')
        return knn_algoritmasi_calistir(test_degeri,komsuluk)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = KNN()
    pencere.show()
    sys.exit(app.exec_())

            
