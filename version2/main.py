from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUiType, loadUi
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import os,sys
from utils import *
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
def resource_path(relative_path):
    """"Get absolut path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
# s=''
# with open('info.html','r',encoding='utf8') as f:
#     for i in f:
#         s=s+i
    
v=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# dic={'a':0,'â':0,'à':0,'Ä':0,'A':0,'b':1,'B':1,'c':2,'C':2,'ç':2,'d':3,'D':3,'e':4,'E':4,'é':4,'è':4,'ê':4,'Ë':4,
#      'f':5,'F':5,'g':6,'G':6,'h':7,'H':7,'i':8,'I':8,'î':8,'ï':8,'j':9,'J':9,'k':10,'K':10,'l':11,'L':11,'m':12,'M':12,
#      'n':13,'N':13,'o':14,'O':14,'ô':14,'Ö':14,'p':15,'P':15,'q':16,'Q':16,'r':17,'R':17,'s':18,'S':18,'t':19,
#      'T':19,'u':20,'û':20,'Ü':20,'U':20,'v':21,'V':21,'w':22,'W':22,'x':23,'X':23,'y':24,'Y':24,'z':25,'Z':25,' ':26}

# dic = {'a': 0, 'â': 0, 'à': 0, 'Ä': 0, 'A': 0, 'b': 1, 'B': 1, 'c': 2, 'C': 2, 'ç': 2, 'd': 3, 'D': 3, 'e': 4, 'E': 4,
#        'é': 4, 'è': 4, 'ê': 4, 'Ë': 4,'É':4 ,'f': 5, 'F': 5, 'g': 6, 'G': 6, 'h': 7, 'H': 7, 'i': 8, 'I': 8, 'î': 8, 'ï': 8,
#        'j': 9, 'J': 9, 'k': 10, 'K': 10, 'l': 11, 'L': 11, 'm': 12, 'M': 12, 'n': 13, 'N': 13, 'o': 14, 'O': 14, 'ô': 14,
#        'Ö': 14, 'œ':14,'p': 15, 'P': 15, 'q': 16, 'Q': 16, 'r': 17, 'R': 17, 's': 18, 'S': 18, 't': 19, 'T': 19, 'u': 20, 'û': 20,
#        'Ü': 20,'ù':20, 'U': 20, 'v': 21, 'V': 21, 'w': 22, 'W': 22, 'x': 23, 'X': 23, 'y': 24, 'Y': 24, 'z': 25, 'Z': 25, ' ': 26}
dic = {'a': 0, 'â': 0, 'à': 0, 'ä': 0, 'A': 0, 'À': 0, 'b': 1, 'B': 1, 'c': 2, 'C': 2, 'ç': 2, 'd': 3, 'D': 3, 'e': 4, 'é': 4, 'è': 4, 'ê': 4, 'ë': 4, 'E': 4,
       'f': 5, 'F': 5, 'g': 6, 'G': 6, 'h': 7, 'H': 7, 'i': 8, 'î': 8, 'ï': 8, 'I': 8, 'j': 9, 'J': 9, 'k': 10, 'K': 10, 'l': 11, 'L': 11, 'm': 12, 'M': 12, 'n': 13, 'N': 13, 'o': 14, 'ô': 14,
       'ö': 14, 'œ': 14, 'O': 14, 'p': 15, 'P': 15, 'q': 16, 'Q': 16, 'r': 17, 'R': 17, 's': 18, 'S': 18, 't': 19, 'T': 19, 'u': 20, 'û': 20, 'ü': 20, 'ù': 20, 'U': 20, 'v': 21, 'V': 21, 'w': 22, 'W': 22, 'x': 23, 'X': 23, 'y': 24, 'Y': 24, 'z': 25, 'Z': 25,
       'é': 4, 'è': 4, 'ê': 4, 'É': 4, 'È': 4, 'Ê': 4,
       'î': 8, 'ï': 8, 'Î': 8, 'Ï': 8,
       'ô': 14, 'ö': 14, 'œ': 14, 'Ô': 14, 'Ö': 14,
       'û': 20, 'ü': 20, 'Û': 20, 'Ü': 20,
       'ù': 20, 'Ù': 20}

FROM_CLASS, _ = loadUiType(resource_path("Ui.ui"))
class Main(QMainWindow, FROM_CLASS):
    def __init__(self):
        super(Main, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        # self.setFixedSize(1400, 1000)
        # self.initUI()
        # self.txtinfo.setText(s)
        center_stylesheet = """
            QGroupBox {
                border: 1px solid gray;
                border-radius: 9px;
                margin-top: 0.5em;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
            }
        """
        self.groupBox.setStyleSheet(center_stylesheet)
        self.groupBox_2.setStyleSheet(center_stylesheet)
        self.groupBox_3.setStyleSheet(center_stylesheet)
        self.groupBox_4.setStyleSheet(center_stylesheet)
       
    def resizeEvent(self, event):
         
        super().resizeEvent(event)

        # Handle resizing event here
        for index in range(self.tabWidget.count()):
            tab = self.tabWidget.widget(index)
            if tab:
                tab_layout = tab.layout()
                if tab_layout:
                    tab_layout.setAlignment(Qt.AlignCenter)

                    for i in range(tab_layout.count()):
                        group_box = tab_layout.itemAt(i).widget()
                        if group_box and group_box.objectName() in ["groupBox", "groupBox_2", "groupBox_3", "groupBox_4"]:
                            group_box.setAlignment(Qt.AlignCenter)
    
    def loaddata(self, data):
        # Set the number of rows and columns
        self.datatable.setRowCount(data.shape[0])
        self.datatable.setColumnCount(data.shape[1])

        # Set horizontal header to stretch the sections
        header = self.datatable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Set size policy to make the QTableWidget take all available space
        self.datatable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set the column names
        self.datatable.setHorizontalHeaderLabels(data.columns)

        for row in data.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:.4f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.datatable.setItem(row[0], col_index, tableItem)

    def decode(self):
        m=self.txtinput.toPlainText()
        k=self.txtK.toPlainText()
        k=k.upper()
        
        if len(k)>0:
            c=Vdechiffrer(m,k,dic,v)
            self.txtoutput.setPlainText(str(c))
        else:
            message_erreur = "Clé de chiffrement vide"
            QMessageBox.critical(self, "Erreur", message_erreur)

    def cryptanalyse(self):
        m=self.txtcryptanalyse.toPlainText()
        m=sup_espace(m)
        Methode=self.comboBox.currentText()
        if len(m)>0:
            # if Methode=='Indice de Coïncidence':
            #     self.txtcryptanalyse_2.setVisible(False)
               
            #     bf=0.068
            #     bs=0.078
            #     dic1 = {
            #     'Clé': [],
            #     'Taille': [],
            #     'Indice de Coïncidence':[]
            # }
            #     cle,size,IC=cle_coincidence(m,dic,v,float(bf),float(bs))
                
                
            #     d={}
            #     k=0
            #     for i in cle:
            #         d[i]=[size[k],IC[k]]
            #         k=k+1
               
            #     for key in d:
            #         dic1['Clé'].append(key)
            #         dic1['Taille'].append(
            #             str(d[key][0]))
            #         dic1['Indice de Coïncidence'].append(float(d[key][1]))
            #     df = pd.DataFrame.from_dict(dic1)
            #     self.loaddata(df)
                
                # self.txtoutput.setPlainText(str(d))
            if Methode=='Babbage':
                self.txtcryptanalyse_2.setVisible(False)
                html_content=""
                
                dic1 = {
                'Clé': [],
                'Taille': [],
            }
                T,s=cle_repetition(m,dic,v)
                d={}
                k=0
                for i in T:
                    d[i]=s[k]
                    k=k+1
                
                for key in d:
                    dic1['Clé'].append(key)
                    dic1['Taille'].append(
                        str(d[key]))
                df = pd.DataFrame.from_dict(dic1)
                self.loaddata(df)

                # d={'Clé':T,'taille':s}
                # self.txtoutput.setPlainText(str(d))
            if Methode=='Indice de Coïncidence':
                intervalle,intervall=trouver_intervalle_anormal(m)
                y,extrait=trouver_cles_potentielles(m,intervalle,dic)
                html_content = f"""
        <style>
            h2 {{
                color: #3498db;
                margin-bottom: 10px;
            }}
            p, pre {{
                color: #ffffff;
                font-size: 14px;
                line-height: 1.4;
                margin-bottom: 15px;
            }}
            pre {{
                
                padding: 10px;
                border-radius: 5px;
                overflow: auto;
            }}
        </style>
        <h2>Indice de coïncidence</h2>
        <p>Intervalle de l'indice de coïncidence :<br> {intervall}</p>

        <h2>Longueur de clé</h2>
        <p>La longueur de la clé est de : {intervalle} caractères</p>

        <h2>Extrait</h2>
        <pre>{extrait}</pre>

        <h2>Clé</h2>
        <p>La clé est : {y}</p>
        """

        # Set the HTML content to the QTextBrowser
        self.txtcryptanalyse_2.setHtml(html_content)
                

    def clearC(self):
        self.txtinput.setPlainText('')
        self.txtoutput.setPlainText('')
        self.txtK.setPlainText('')
    def clearA(self):
        self.txtoutput.setPlainText('')
        self.txtcryptanalyse.setPlainText('')
        self.datatable.clearContents()
        
    def combo(self):
        Methode=self.comboBox.currentText()
        if Methode=='Indice de Coïncidence':
                self.txtcryptanalyse_2.setVisible(True)
        else:
            self.txtcryptanalyse_2.setVisible(False)
    def encoder(self):
        m=self.txtinput.toPlainText()
        # Vchiffrer(m,k,dic,v)
        k=self.txtK.toPlainText()
       
        if len(k)>0:
            k=k.upper()
          
            c=Vchiffrer(m,k,dic,v)
            self.txtoutput.setPlainText(str(c))
        else:
            message_erreur = "Clé de chiffrement vide"
            QMessageBox.critical(self, "Erreur", message_erreur)
    
    def save_text_to_file(self):
        # Open a file dialog to specify the save location and file name
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt)")

        # Write the content of QTextEdit to the selected file
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.txtoutput.toPlainText())

           
    
    def load_text_file(self):
        # Open a file dialog to select a text file
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")

        # Read the content of the selected file and display it in QTextEdit
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.txtinput.setPlainText(content)
    def load_text_file2(self):
        # Open a file dialog to select a text file
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")

        # Read the content of the selected file and display it in QTextEdit
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.txtcryptanalyse.setPlainText(content)

    
    def Handel_Buttons(self):
        try:
            self.btnencoder.clicked.connect(self.encoder)
            self.btndecode.clicked.connect(self.decode)
            self.btnencoder_2.clicked.connect(self.load_text_file)
            self.btnencoder_3.clicked.connect(self.load_text_file2)
            self.pushButton_3.clicked.connect(self.cryptanalyse)
            self.pushButton_5.clicked.connect(self.clearC)
            self.pushButton_4.clicked.connect(self.clearA)
            self.save.clicked.connect(self.save_text_to_file)
            self.comboBox.currentIndexChanged.connect(self.combo)
        except Exception as e:
            # Affichez une boîte de dialogue d'erreur
            message_erreur = f"Une erreur s'est produite : {str(e)}"
            QMessageBox.critical(self, "Erreur", message_erreur)
      
       


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
