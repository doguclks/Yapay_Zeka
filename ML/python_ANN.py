from PyQt5.QtWidgets import *
from ANN_arayuz import Ui_Form
import pandas as pd
import sys
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
import numpy as np
from sklearn.metrics import accuracy_score
import tensorflow as tf
from sklearn.datasets import make_classification


class ANN(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.BtnModeliEgit.clicked.connect(self.ANN)
        
    def ANN(self):
        k_fold = int(self.ui.TxtKFold.text())
        test_size = float(self.ui.TxtTestSize.text())
        batch_size = int(self.ui.TxtBatchSize.text())
        epochs = int(self.ui.TxtEpochs.text())
        validation = float(self.ui.TxtValidatioin.text())
        patience = int(self.ui.TxtPatience.text())
        def ANN(k_fold,test_size,batch_size,epochs,validation,patience):
            data_setim= pd.read_csv(r"C:\Users\doguk\Desktop\ML\Epileptic Seizure Recognition.csv")
            #verisetinde gezinmek icin
            X = data_setim.iloc[:,1:-1].values
            y = data_setim.iloc[:,-1:].values
            #11500 ornekli data setinde 180 ozellik var,6 class ve onemli değer 300 tane(informative kismi keyfi)
            X, y = make_classification(n_samples=11500, n_features=180, n_informative=50, n_classes=6, random_state=42)
            #data k tane parcaya bolunecek ve daha sonrasında kfold uygulanacak(her birisi icin itere sekilde)
            from sklearn.model_selection import KFold
            Kfold = KFold(n_splits=k_fold, shuffle=True, random_state=42)
            accuracy_scores = []
            for train_index, test_index in Kfold.split(X, y):
                X_Kfold, X_test = X[train_index], X[test_index]
                y_Kfold, y_test = y[train_index], y[test_index]
                from sklearn.model_selection import train_test_split
                from keras.utils import to_categorical
                #6class dedigimiz icin test ve trainleri 6 classli kategorilere cevirdik normal train test yerine kfold uygulanmis
                #multi classli bir yapi uygulayacagiz
                X_train, _, y_train, _ = train_test_split(X_Kfold, y_Kfold, test_size=test_size, shuffle=True, random_state=42)
                y_train_multi = to_categorical(y_train, num_classes=6)
                y_test_multi = to_categorical(y_test, num_classes=6) #öznitelik dönüştürme
                #normalizasyon uygulandi
                from sklearn.preprocessing import StandardScaler
                normalizasyon = StandardScaler()
                normalizasyon.fit(X_train)
                X_train = normalizasyon.transform(X_train)
                X_test = normalizasyon.transform(X_test) 
                
            from keras.models import Sequential
            from keras.layers import Dense
            #modelin semasini belirledikten sonra giris-gizli ve cikis katmani olarak katmanladim. son katman 6 cunku her bir class icin
            sinir_agi = Sequential()
            #model karmasikligini belirleyen kisim units, modele gore degiskenlik gosterebilir
            sinir_agi.add(Dense(units=256,activation='relu'))
            sinir_agi.add(Dense(units=128,activation='relu'))
            sinir_agi.add(Dense(units=64,activation='relu'))
            #softmaxle en yuksek gelen deger donecek
            sinir_agi.add(Dense(units=6,activation='softmax'))
            from keras.callbacks import EarlyStopping
            from keras.callbacks import ModelCheckpoint
            sinir_agi.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
            early_stopping = EarlyStopping(monitor='val_loss', mode='min', patience=patience)
            checkpoint = ModelCheckpoint(filepath='C:\\Users\\doguk\\Desktop\\ML"/checkpoint', save_best_only=True)

            sinir_agi.fit(X_train,y_train_multi,batch_size=batch_size,epochs = epochs,validation_split=(validation),callbacks=[early_stopping],verbose=1)
            accuracy_score= sinir_agi.evaluate(X_test, y_test_multi)
            accuracy_scores.append(accuracy_score[1])
            print(accuracy_score,Kfold)
            mean_accuracy = np.mean(accuracy_scores)
            print("Mean Accuracy:", np.mean(accuracy_scores))
            accuracy_text = f"Accuracy Score: {accuracy_score[1]:.4f}"
            self.ui.label_7.setText(accuracy_text)
            mean_accuracy_text = f"Mean Accuracy: {mean_accuracy:.4f}"
            self.ui.label_8.setText(mean_accuracy_text)
        return ANN(k_fold,test_size,batch_size,epochs,validation,patience)
    
        
        
        
        
        
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = ANN()
    pencere.show()
    sys.exit(app.exec_())
