import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout, QLabel

class Shashka(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шашка")
        self.count = 0
        self.tekshir = 1
        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()
        self.buttons = []
        self.yurish_gali = QLabel("yurish gali '⚪️'")
        self.lbl = QLabel("Bobur_1402")
        self.lbl.setStyleSheet("color:black")
        self.lbl.move(0, 0)
        self.lbl.setFont(QFont("Italic", 6))
        self.yurish_gali.setFont(QFont("Italic", 16))
        self.yurish_gali.setFixedSize(140, 30)
        self.yurish_gali.setStyleSheet("color:black")
        self.h_box.addStretch()
        self.h_box.addWidget(self.yurish_gali)
        self.h_box.addStretch()
        self.gal = 1
        self.taqiqlanadi = 1
        self.v_box.addLayout(self.h_box)
        self.setStyleSheet("border-radius:10px;background-color:white")

        self.h_box = QHBoxLayout()

        self.setFixedSize(625, 625)

        count = 0
        i = 0
        while i < 8:
            j = 0
            self.temp = []
            while j < 8:
                self.kletka = QPushButton(' ')
                self.kletka.setFixedSize(70, 70)
                self.kletka.clicked.connect(self.xod)


                if count % 2 == 0:
                    if j % 2 != 0:
                        self.kletka.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        if i < 4:
                            self.kletka.setText('⚪️')
                        elif i > 4:
                            self.kletka.setText('⚫️')
                else:
                    if j % 2 == 0:
                        self.kletka.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        if i < 3:
                            self.kletka.setText('⚪️')
                        elif i > 4:
                            self.kletka.setText('⚫️')

                self.temp.append(self.kletka)

                self.h_box.addWidget(self.kletka)
                j+=1
            count +=1

            self.v_box.addLayout(self.h_box)
            self.h_box = QHBoxLayout()
            self.buttons.append(self.temp)
            i+=1
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.lbl)



        self.show()
        self.setLayout(self.v_box)

    def xod(self):
        txt = self.sender()
        color = txt.palette().window().color().name()

        if self.tekshir == 1 and color == "#2e2e2d":
            self.uwlaw1 = self.sender()
            self.uwlaw1_index = fountIndex2d(self.buttons, self.uwlaw1)
            self.tekshir = 0

        elif color == "#2e2e2d" and self.tekshir == 0:
            self.uwlaw2 = self.sender()
            self.uwlaw2_index = fountIndex2d(self.buttons, self.uwlaw2)

            if self.uwlaw2.text() == self.uwlaw1.text():
                self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                self.uwlaw1.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                self.uwlaw1 = self.uwlaw2
                self.uwlaw2 = ' '
                self.tekshir = 0
            else:
                self.tekshir = 1

        if self.taqiqlanadi == 1 and self.uwlaw1.text() == '⚫️' or self.taqiqlanadi == 0 and self.uwlaw1.text() == '⚪️':

            if txt.text() == '⚫️' or txt.text() == '⚪️' or txt.text() == ' ' and color != "#f0f0f0" and self.uwlaw1.text() != ' ':
                txt.setStyleSheet("font-size:40px;background-color:red")

                if self.tekshir == 1 and self.uwlaw2.text() != self.uwlaw1.text() and self.uwlaw1.text() != ' ':

                    if self.xod_tekshir() and self.uwlaw2.text() == ' ':
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw1.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw2.setText(self.uwlaw1.text())
                        self.uwlaw1.setText(' ')
                        if self.gal == 1:
                            self.yurish_gali.setText("yurish gali '⚫️'")
                            self.gal = 0
                            self.taqiqlanadi = 0
                        else:
                            self.yurish_gali.setText("yurish gali '⚪️'")
                            self.gal = 1
                            self.taqiqlanadi = 1
                    else:
                        self.tekshir = 1
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw1.setStyleSheet("font-size:40px;background-color:#2e2e2d")

            elif self.uwlaw1.text() == ' ':
                self.tekshir = 1


        else:
            self.tekshir = 1

    def xod_tekshir(self):
        if self.yutish():
            return True
        if self.uwlaw1.text() == '⚪️':

            if self.uwlaw1_index[0] + 1 == self.uwlaw2_index[0]:
                if self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] or self.uwlaw1_index[1] - 1 == self.uwlaw2_index[1]:

                    return True
            return False

        elif self.uwlaw1.text() == '⚫️':
            if self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] or self.uwlaw1_index[1] - 1 == self.uwlaw2_index[1]:
                if self.uwlaw1_index[0] - 1 == self.uwlaw2_index[0]:
                    return True
        return False
    def yutish(self):

        if self.uwlaw2_index[1] != 7 and self.uwlaw2_index[1] != 0:
            if self.buttons[self.uwlaw1_index[0]][self.uwlaw1_index[1]].text() == '⚪️' and self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].text() == '⚫️':
                if self.uwlaw1_index[0] + 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0]+1][self.uwlaw2_index[1]+1].text() == ' ':
                    self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                    self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                    self.uwlaw2 = self.buttons[self.uwlaw2_index[0]+1][self.uwlaw2_index[1]+1]
                    self.yutish()
                    return True
                elif self.uwlaw1_index[0] + 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] - 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0]+1][self.uwlaw2_index[1]-1].text() == ' ':
                    self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                    self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                    self.uwlaw2 = self.buttons[self.uwlaw2_index[0]+1][self.uwlaw2_index[1]-1]
                    self.yutish()
                    return True
                elif self.uwlaw1_index[0] - 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] - 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0]-1][self.uwlaw2_index[1]-1].text() == ' ':
                    self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                    self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                    self.uwlaw2 = self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] - 1]
                    self.yutish()
                    return True
                elif self.uwlaw1_index[0] - 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0]-1][self.uwlaw2_index[1]+1].text() == ' ':
                    self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                    self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                    self.uwlaw2 = self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] + 1]
                    self.yutish()
                    return True

            elif self.buttons[self.uwlaw1_index[0]][self.uwlaw1_index[1]].text() == '⚫️':
                if self.buttons[self.uwlaw1_index[0]][self.uwlaw1_index[1]].text() == '⚫️' and self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].text() == '⚪️':
                    if self.uwlaw1_index[0] + 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0] + 1][self.uwlaw2_index[1] + 1].text() == ' ':
                        self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw2 = self.buttons[self.uwlaw2_index[0] + 1][self.uwlaw2_index[1] + 1]
                        self.yutish()
                        return True
                    elif self.uwlaw1_index[0] + 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] - 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0] + 1][self.uwlaw2_index[1] - 1].text() == ' ':
                        self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw2 = self.buttons[self.uwlaw2_index[0] + 1][self.uwlaw2_index[1] - 1]
                        self.yutish()
                        return True
                    elif self.uwlaw1_index[0] - 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] - 1 ==  self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] - 1].text() == ' ':
                        self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw2 = self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] - 1]
                        self.yutish()
                        return True
                    elif self.uwlaw1_index[0] - 1 == self.uwlaw2_index[0] and self.uwlaw1_index[1] + 1 == self.uwlaw2_index[1] and self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] + 1].text() == ' ':
                        self.buttons[self.uwlaw2_index[0]][self.uwlaw2_index[1]].setText(' ')
                        self.uwlaw2.setStyleSheet("font-size:40px;background-color:#2e2e2d")
                        self.uwlaw2 = self.buttons[self.uwlaw2_index[0] - 1][self.uwlaw2_index[1] + 1]
                        self.yutish()
                        return True

        return False

def fountIndex2d(list1,found1):
    for i in range(8):
        for j in range(8):
            if list1[i][j] == found1:
                return  [i,j]




app = QApplication(sys.argv)
win = Shashka()
sys.exit(app.exec())
