import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import uic
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWindow.ui', self)
        self.pushButton.clicked.connect(self.button_work)

    def button_work(self):
        if self.radioButton.isChecked():
            self.openClassic()
        elif self.radioButton_3.isChecked():
            self.openIntRate()
        elif self.radioButton_4.isChecked():
            self.openClassic_big()

    def openClassic(self):
         self.classic=SecondWindow()
         self.classic.show()

    def openIntRate(self):
        self.int_rate=ThirdWindow()
        self.int_rate.show()

    def openClassic_big(self):
        self.classic_big=FourthWindow()
        self.classic_big.show()



class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Classic.ui', self)
        self.figure=Figure()
        self.figure_1=Figure()
        self.canvas=FigureCanvas(self.figure)
        self.canvas_1=FigureCanvas(self.figure_1)
        self.canvas_1.setParent(self.widget_2)
        self.canvas.setParent(self.widget)
        self.canvas.setGeometry(self.widget.rect())
        self.canvas_1.setGeometry(self.widget_2.rect())
        self.slider_S.valueChanged.connect(self.update_graph)
        self.slider_I.valueChanged.connect(self.update_graph)
        self.slider_r.valueChanged.connect(self.update_graph)
        self.slider_CF.valueChanged.connect(self.update_graph)
        self.slider_CA.valueChanged.connect(self.update_graph)

        self.plot_small_open_economy_1(5,5,5)
        self.plot_small_open_economy_2(5,5)
        self.update_graph()

    def resizeEvent(self, event):
        self.canvas.setGeometry(self.widget.rect())
    def resizeEvent_1(self, event):
        self.canvas_1.setGeometry(self.widget_2.rect())

    def update_graph(self):
        S = self.slider_S.value()/10
        I_param = self.slider_I.value()/10
        r_star=self.slider_r.value()/10
        CF=self.slider_CF.value()/10
        sh=self.slider_CA.value()/10

        self.plot_small_open_economy_1(S, I_param, r_star)
        self.plot_small_open_economy_2(CF,sh)

    def plot_small_open_economy_1(self, S, a, r_star):

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        r = np.linspace(1, 9.5, 100)

        I = a - r

        r_eq = a - S
        I_eq = a - r_star
        CA = S-I_eq

        ax.plot(I, r, label="I(r)")
        ax.axvline(x=S, label="S")
        ax.scatter(I_eq, r_star)

        ax.hlines(r_star, 0, S, linestyles='dashed')
        ax.hlines(r_star, I_eq, S, linewidth=3)
        ax.text((I_eq+S)/2, r_star+0.3, 'CA')

        ax.set_xlabel("I, S")
        ax.set_ylabel("r*")

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.text(S + 0.2, 8, "S")
        ax.text(8, 3, "I(r)")
        ax.text(0.2, r_star+0.5, "r*")

        ax.legend()

        self.figure.subplots_adjust(left=0.15, right= 0.95,
                                        top=0.9, bottom=0.2)
        self.canvas.draw()
        

    def plot_small_open_economy_2(self, CF, sh):
        self.figure_1.clear()
        bx=self.figure_1.add_subplot(111)
            
        q=np.linspace(1,9.5,100)
        CA_curve=q + sh
        q_eq= CF - sh
        CA_eq= CF

        bx.plot(CA_curve, q, label='CA(q)')

        bx.axvline(x=CF, label='CF')

        bx.scatter(CA_eq, q_eq)

        bx.hlines(q_eq, 0, CA_eq, linestyles='dashed')

        bx.set_xlabel('CA')
        bx.set_ylabel('q')

        bx.set_xlim(0,10)
        bx.set_ylim(0,10)

        bx.text(CF + 0.2, 8, "CF")
        bx.text(8, 7, "CA(q)")
        bx.text(0.2, q_eq+0.5, "q*")

        bx.legend()
        self.figure_1.subplots_adjust(left=0.15, right= 0.95,
                                            top=0.9, bottom=0.2)

        self.canvas_1.draw()


class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/par_int_rate.ui', self)

class FourthWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Classic_big.ui', self)
        

        
        
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec())
