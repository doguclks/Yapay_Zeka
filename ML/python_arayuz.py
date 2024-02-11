from PyQt5.QtWidgets import *
from arayuz import Ui_Form
from python_knn import KNN
from python_Random_Forest import Random_Forest
from python_NB import NB
from python_ANN import ANN
import pandas as pd
import sys


class Arayuz(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.knn_sayfasi_ac = KNN()
        self.random_forest_sayfa_ac = Random_Forest()
        self.nb_sayfa_ac_1 = NB()
        self.ann_sayfa_ac = ANN()
        
        self.ui.BtnDYukle.clicked.connect(self.yukle)
        self.ui.BtnKNN.clicked.connect(self.knnac)
        self.ui.BtnNaive.clicked.connect(self.nb_sayfa_ac)
        self.ui.BtnRandomForest.clicked.connect(self.randomforestac)
        self.ui.BtnANN.clicked.connect(self.ann_ac)
        
        
        
    def yukle(self):
        try:
            data_set = pd.read_csv(r"C:\Users\doguk\Desktop\ML\Epileptic Seizure Recognition.csv")
            if not data_set.empty:
                self.populateTable(data_set)
            else:
                print("CSV file is empty.")
        except pd.errors.EmptyDataError:
            print("CSV file is empty.")
        except pd.errors.ParserError:
            print("Error parsing CSV file.")

                
    def populateTable(self, df):
        self.ui.tableWidget.clear()
        # Set row and column count
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setColumnCount(df.shape[1])

        # Set column headers
        self.ui.tableWidget.setHorizontalHeaderLabels(df.columns)

        # Fill the table with data
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[i, j]))
                self.ui.tableWidget.setItem(i, j, item)
        
    def knnac(self):
        self.knn_sayfasi_ac.show()  
        
    def randomforestac(self):
        self.random_forest_sayfa_ac.show()
            
        
    def nb_sayfa_ac(self):
        self.nb_sayfa_ac_1.show()
      
    def ann_ac(self):
        self.ann_sayfa_ac.show()  
    
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Arayuz()
    pencere.show()
    sys.exit(app.exec_())

    
        
    
