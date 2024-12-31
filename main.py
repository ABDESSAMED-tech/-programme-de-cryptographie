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

dic = {'a': 0, 'â': 0, 'à': 0, 'Ä': 0, 'A': 0, 'b': 1, 'B': 1, 'c': 2, 'C': 2, 'ç': 2, 'd': 3, 'D': 3, 'e': 4, 'E': 4,
       'é': 4, 'è': 4, 'ê': 4, 'Ë': 4, 'f': 5, 'F': 5, 'g': 6, 'G': 6, 'h': 7, 'H': 7, 'i': 8, 'I': 8, 'î': 8, 'ï': 8,
       'j': 9, 'J': 9, 'k': 10, 'K': 10, 'l': 11, 'L': 11, 'm': 12, 'M': 12, 'n': 13, 'N': 13, 'o': 14, 'O': 14, 'ô': 14,
       'Ö': 14, 'p': 15, 'P': 15, 'q': 16, 'Q': 16, 'r': 17, 'R': 17, 's': 18, 'S': 18, 't': 19, 'T': 19, 'u': 20, 'û': 20,
       'Ü': 20,'ù':20, 'U': 20, 'v': 21, 'V': 21, 'w': 22, 'W': 22, 'x': 23, 'X': 23, 'y': 24, 'Y': 24, 'z': 25, 'Z': 25, ' ': 26}

FROM_CLASS, _ = loadUiType(resource_path("Ui.ui"))
class Main(QMainWindow, FROM_CLASS):
    def __init__(self):
        super(Main, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.setFixedSize(944, 700)
        self.groupBox_5.setVisible(False)
        self.initUI()
        # self.txtinfo.setText(s)
    def initUI(self):
        self.setGeometry(0, 0, 400, 300)  # Set the initial size of the window

        # Calculate the center position of the screen
        screen_rect = QDesktopWidget().screenGeometry()
        x = (screen_rect.width() - self.width()) // 2
        y = (screen_rect.height() - self.height()) // 2

        # Move the window to the center position
        self.move(x, y)

        self.setWindowTitle('Centered Window')
        self.show()
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
        # print(k)
        if len(k)>0:
            c=Vdechiffrer(m,k,dic,v)
            self.txtoutput.setPlainText(str(c))
        else:
            self.txtoutput.setPlainText('Clé de chiffrement vide ')

    def cryptanalyse(self):
        m=self.txtcryptanalyse.toPlainText()
        m=sup_espace(m)
        Methode=self.comboBox.currentText()
        if len(m)>0:
            if Methode=='Friedman':
                bf=self.spnBF.value()
                bs=self.spnSup.value()
                dic1 = {
                'Clé': [],
                'Taille': [],
                'IC':[]
            }
                cle,size,IC=cle_coincidence(m,dic,v,float(bf),float(bs))
                # print(IC[0])
                d={}
                k=0
                for i in cle:
                    d[i]=[size[k],IC[k]]
                    k=k+1
                # print(d)
                for key in d:
                    dic1['Clé'].append(key)
                    dic1['Taille'].append(
                        str(d[key][0]))
                    dic1['IC'].append(float(d[key][1]))
                df = pd.DataFrame.from_dict(dic1)
                self.loaddata(df)
                # print(df)
                # self.txtoutput.setPlainText(str(d))
            if Methode=='Babbage':
                self.groupBox_5.setVisible(False)
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
                # print(d)
                for key in d:
                    dic1['Clé'].append(key)
                    dic1['Taille'].append(
                        str(d[key]))
                df = pd.DataFrame.from_dict(dic1)
                self.loaddata(df)

                # d={'Clé':T,'taille':s}
                # self.txtoutput.setPlainText(str(d))
    def combo(self):
        Methode=self.comboBox.currentText()
        if Methode=='Friedman':
                self.groupBox_5.setVisible(True)
        else:
            self.groupBox_5.setVisible(False)

    def clearC(self):
        self.txtinput.setPlainText('')
        self.txtoutput.setPlainText('')
    def clearA(self):
        self.txtoutput.setPlainText('')
        self.txtcryptanalyse.setPlainText('')
        self.datatable.clearContents()
        

    def encoder(self):
        m=self.txtinput.toPlainText()
        # Vchiffrer(m,k,dic,v)
        k=self.txtK.toPlainText()
       
        if len(k)>0:
            k=k.upper()
            # print(k)
            c=Vchiffrer(m,k,dic,v)
            self.txtoutput.setPlainText(str(c))
        else:
            self.txtoutput.setPlainText('Clé de chiffrement vide ')
            
    def decode2(self):
        i=0
        self.txtoutput_2.setPlainText('')
        m=self.txtinput_2.toPlainText()
        k=self.txtK_2.toPlainText()
        k1=k.upper()
        k=self.txtK_3.toPlainText()
        k=k.upper()
        # print(k)
        if len(k)>0 and len(k1)>0 :
            c=Vdechiffrer(m,k,dic,v)
            c1=Vdechiffrer(m,k1,dic,v)
            text_cursor = self.txtoutput_2.textCursor()
            for char_c, char_c1 in zip(str(c), str(c1)):
                char_format = QTextCharFormat()

                # Compare characters and set color accordingly
                if char_c != char_c1:
                    char_format.setForeground(QColor("red"))  # Change color to red for differences
                    i=i+1
                else:
                    char_format.setForeground(QColor("white"))  # Set the default color

                text_cursor.mergeCharFormat(char_format)
                text_cursor.insertText(char_c)

            # Move the cursor to the end of the text to avoid overwriting
            text_cursor.movePosition(QTextCursor.End)

            # Set the modified cursor back to the text edit widget
            self.txtoutput_2.setTextCursor(text_cursor)
            c=''
            c1=""
            self.diff.setText(f'Il y a une différence de {i} entre la clé réelle et la clé de test.')
        else:
            self.txtoutput_2.setPlainText('Clé de chiffrement vide ')
    def save_text_to_file(self):
        # Open a file dialog to specify the save location and file name
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt)")

        # Write the content of QTextEdit to the selected file
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.txtoutput.toPlainText())

            print(f"File '{file_path}' saved successfully.")
    def clearD(self):
        self.txtinput_2.setPlainText('')
        self.txtoutput_2.setPlainText('')
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
    def load_text_file3(self):
        # Open a file dialog to select a text file
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")

        # Read the content of the selected file and display it in QTextEdit
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.txtinput_2.setPlainText(content)
    
    def Handel_Buttons(self):
       self.btnencoder.clicked.connect(self.encoder)
       self.btndecode.clicked.connect(self.decode)
       self.btnencoder_2.clicked.connect(self.load_text_file)
       self.btnencoder_3.clicked.connect(self.load_text_file2)
       self.btndecode_2.clicked.connect(self.decode2)
       self.pushButton_3.clicked.connect(self.cryptanalyse)
       self.pushButton_5.clicked.connect(self.clearC)
       self.pushButton_4.clicked.connect(self.clearA)
       self.pushButton_6.clicked.connect(self.clearD)
       self.comboBox.currentIndexChanged.connect(self.combo)
       self.save.clicked.connect(self.save_text_to_file)
       self.btnencoder_4.clicked.connect(self.load_text_file3)
       


def main():
    app = QApplication(sys.argv)
    window = Main()

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
