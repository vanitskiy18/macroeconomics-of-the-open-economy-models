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
            self.openBilans()

    def openClassic(self):
         self.classic=SecondWindow()
         self.classic.show()

    def openIntRate(self):
        self.int_rate=ThirdWindow()
        self.int_rate.show()

    def openBilans(self):
        self.bilans=FourthWindow()
        self.bilans.show()



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

        self.slider_CA.valueChanged.connect(self.update_graph)

        self.slider_S.setValue((self.slider_S.minimum() + self.slider_S.maximum())//2)
        self.slider_I.setValue(self.slider_I.maximum())
        self.slider_r.setValue((self.slider_r.minimum() + self.slider_r.maximum())//2)
        self.slider_CA.setValue((self.slider_CA.minimum()+self.slider_CA.maximum())//2)

        self.plot_small_open_economy_1(5,5,5)
        self.plot_small_open_economy_2(5,5)
        self.update_graph()

        self.button_open.clicked.connect(self.openInfoOpen)

    def resizeEvent(self, event):
        self.canvas.setGeometry(self.widget.rect())
        self.canvas_1.setGeometry(self.widget_2.rect())
        super().resizeEvent(event)

    def update_graph(self):
        S = self.slider_S.value()/10
        I_param = self.slider_I.value()/10
        r_star=self.slider_r.value()/10
        sh=self.slider_CA.value()/10

        I_eq = I_param - r_star
        CF = S - I_eq

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

        ax.plot(I, r)
        ax.axvline(x=S)
        ax.scatter(I_eq, r_star)

        ax.hlines(r_star, 0, S, linestyles='dashed')
        ax.hlines(r_star, I_eq, S, linewidth=3)
        ax.text((I_eq+S)/2, r_star+0.3, 'CA')

        ax.set_xlabel("I+CF, S")
        ax.set_ylabel("r")

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.text(S + 0.2, 9, "S")
        ax.text(I[0]-1.2, r[0]+1.5, "I(r)+CF(r)")
        ax.text(-0.5, r_star, "r")

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        ax.annotate('', xy=(10,0), xytext=(-0.075,0),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5))
        ax.annotate('', xy=(0,10), xytext=(0,-0.075),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5))

        ax.set_xticks([])
        ax.set_yticks([])

        ax.xaxis.set_label_coords(0.9, -0.05)
        ax.yaxis.set_label_coords(-0.05, 0.98)

        self.figure.subplots_adjust(left=0.15, right= 0.95,
                                        top=0.9, bottom=0.2)
        self.canvas.draw()
        

    def plot_small_open_economy_2(self, CF, sh):
        self.figure_1.clear()
        bx=self.figure_1.add_subplot(111)
            
        q=np.linspace(-9,9.5,100)
        CA_curve=q + sh
        q_eq= CF - sh
        CA_eq= CF

        bx.plot(CA_curve, q)

        bx.axvline(x=CF)    

        bx.scatter(CA_eq, q_eq)

        bx.hlines(q_eq, -10, CA_eq, linestyles='dashed')

        bx.axhline(0, linewidth=1, linestyle='dashed', color='gray', alpha=0.5)

        bx.set_xlabel('CA')
        bx.set_ylabel('q')

        bx.set_xlim(-10,10)
        bx.set_ylim(-10,10)

        bx.set_yticks(range(-10,11,2))
        bx.set_xticks(range(-10,11,2))

        bx.text(CF + 0.3, 8, "CF")
        if q[-1]+sh>=10:
            bx.text(CA_curve[0]-0.5,q[0]+3, "CA(q)")
        else:
            bx.text(CA_curve[-1]-0.5, q[-1]-3, "CA(q)")
        bx.text(-9, q_eq+0.3, "q")

        bx.spines['top'].set_visible(False)
        bx.spines['right'].set_visible(False)
        bx.spines['bottom'].set_visible(False)
        bx.spines['left'].set_visible(False)

        bx.annotate('', xy=(10,-10), xytext=(-10.25,-10),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5))
        bx.annotate('', xy=(-10,10), xytext=(-10,-10.25),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5))

        bx.set_xticks([])
        bx.set_yticks([])

        bx.xaxis.set_label_coords(0.98, -0.05)
        bx.yaxis.set_label_coords(-0.05, 0.98)

        self.figure_1.subplots_adjust(left=0.2, right= 0.95,
                                            top=0.9, bottom=0.2)

        self.canvas_1.draw()

    def openInfoOpen(self):
        self.info=InfoOpen()
        self.info.show()

class InfoOpen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/info_open.ui', self)


class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/par_int_rate.ui', self)

class FourthWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Bilans.ui', self)
        self.figure=Figure()
        self.canvas=FigureCanvas(self.figure)
        self.canvas.setParent(self.widget_2)
        self.canvas.setGeometry(self.widget_2.rect())
        self.ppf_mode=None
                    
        self.slider_r.valueChanged.connect(self.update_graph)
        self.slider_beta.valueChanged.connect(self.update_graph)

        self.slider_r.setValue(0)
        self.slider_beta.setValue(50)

        self.button_future.clicked.connect(self.show_future)
        self.button_present.clicked.connect(self.show_present)
        self.button_hide.clicked.connect(self.hide_ppf)

        self.button_info.clicked.connect(self.openInfoBilans)

        self.plot_bilans(0.25,0.25)
        self.update_graph()
        #except Exception as e:
            #print("Błąd:", e)

    def resizeEvent(self, event):
        self.canvas.setGeometry(self.widget_2.rect())
        super().resizeEvent(event)

    def update_graph(self):
        r=self.slider_r.value()/100
        beta=self.slider_beta.value()/100

        self.plot_bilans(r, beta)

    def show_future(self):
        self.ppf_mode='future'
        self.update_graph()

    def show_present(self):
        self.ppf_mode='present'
        self.update_graph()

    def hide_ppf(self):
        self.ppf_mode=None
        self.update_graph()

    def ppf_present_curve(self,r, y1, y2, c1_max):
        x0=0.8*c1_max
        k=0.14

        x=np.linspace(0,c1_max,400)
        budget_y=(1+r)*(y1-x)+y2
        y=budget_y-k*(x-x0)**2

        y[y<0]=np.nan

        return x,y,x0

    def ppf_future_curve(self,r, y1, y2, c1_max):
        x0=0.2*c1_max
        k=0.75

        x=np.linspace(0,c1_max,400)
        budget_y=(1+r)*(y1-x)+y2
        y=budget_y-k*(x-x0)**2
        
        y[y<0]=np.nan

        return x,y,x0
    
    def plot_bilans(self, r, beta):
        self.figure.clear()
        cx = self.figure.add_subplot(111)
            
        y1=5
        y2=5
        c1=beta*(y1+y2/(1+r))
        c2=(1-beta)*((1+r)*y1+y2)
        c1_max=y1+(y2/(1+r))
        c1_vals=np.linspace(0.01,c1_max,100)
        c2_max=y1*(1+r)+y2
        U=(c1**beta)*(c2**(1-beta))

        x_r=None
        y_r=None
            
        line_budget=(1+r)*(y1-c1_vals)+y2
        utility_func=(U/(c1_vals**beta))**(1/(1-beta))
        utility_func[utility_func > c2_max-1.2]=np.nan
        utility_func[c1_vals > c1_max-1.2]=np.nan
            
        cx.plot(c1_vals, line_budget)
        cx.plot(c1_vals, utility_func)

        if self.ppf_mode == 'present':
            x_ppf, y_ppf, x_r=self.ppf_present_curve(r, y1, y2, c1_max)
            cx.plot(x_ppf, y_ppf, color='red', linewidth=2)

            y_r=(1+r)*(y1-x_r)+y2
            cx.scatter(x_r, y_r, zorder=5)
            cx.hlines(y_r, 0, x_r, linestyles='dashed', color='grey')
            cx.vlines(x_r, 0, y_r, linestyles='dashed', color='grey')
            
            if x_r!=c1:
                cx.text(x_r, -1, r'$Y_1$', fontsize=10)
            if y_r!=c2:
                cx.text(-1, y_r, r'$Y_2$', fontsize=10)
        elif self.ppf_mode == 'future':
            x_ppf, y_ppf, x_r=self.ppf_future_curve(r, y1, y2, c1_max)
            cx.plot(x_ppf, y_ppf, color='red', linewidth=2)

            y_r=(1+r)*(y1-x_r)+y2
            cx.scatter(x_r, y_r, zorder=5)
            cx.hlines(y_r, 0, x_r, linestyles='dashed', color='grey')
            cx.vlines(x_r, 0, y_r, linestyles='dashed', color='grey')
            
            if x_r!=c1:
                cx.text(x_r, -1, r'$Y_1$', fontsize=10)
            if y_r!=c2:
                cx.text(-1, y_r, r'$Y_2$', fontsize=10)

        elif self.ppf_mode==None:
            cx.scatter(y1,y2, zorder=5)
            cx.hlines(y2, 0, y1, linestyles='dashed', color='grey')
            cx.vlines(y1, 0, y2, linestyles='dashed', color='grey')
            if y1!=c1:
                cx.text(y1, -1, r'$Y_1$', fontsize=10)
            if y2!=c2:
                cx.text(-1, y2, r'$Y_2$', fontsize=10)
            
        cx.set_xlim(0, 10.5)
        cx.set_ylim(0, 10.5)

        cx.set_xticks([])
        cx.set_yticks([])
            
        cx.set_xlabel(r'$C_1$', fontsize=12)
        cx.set_ylabel(r'$C_2$', fontsize=12)
        cx.xaxis.set_label_coords(1, -0.05)
        cx.yaxis.set_label_coords(-0.05, 1)
            
        cx.text(c1_max-4, 1, r'$Y_1 + \frac{Y_2}{1+r}$', fontsize=10)
        cx.text(r*2+1.5, 9, r'$(1+r)Y_1 + Y_2$', fontsize=10)
        cx.scatter(c1, c2, zorder=5)
        cx.scatter(c1_max-0.15, 0.15, zorder=5)
        cx.scatter(0.15, c2_max-0.15, zorder=5)
        if c1==5 and c2==5:
            cx.text(5.25,5.25, r'$E_A$', fontsize=12)
        else:
            cx.text(c1+0.25, c2+0.25, r'$E_r$', fontsize=12)
        cx.hlines(c2, 0, c1, linestyles='dashed', color='grey')
        cx.vlines(c1, 0, c2, linestyles='dashed', color='grey')

        cx.spines['top'].set_visible(False)
        cx.spines['right'].set_visible(False)
        cx.spines['bottom'].set_visible(False)
        cx.spines['left'].set_visible(False)
            
        eps= 10.5*0.01
        cx.annotate('', xy=(10.5,0), xytext=(-eps,0),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5,
                                    zorder=0), zorder=0)
        cx.annotate('', xy=(0,10.5), xytext=(0,-eps),
                    arrowprops=dict(arrowstyle='->', linewidth=1.5,
                                    zorder=0), zorder=0)
        if c1==y1 and self.ppf_mode==None:
            cx.text(y1-0.3,-1, r'$C_1=Y_1$', fontsize=10)
        elif c1==x_r and self.pff_mode!=None:
            cx.text(x_r-0.3,-1, r'$C_1=Y_1$', fontsize=10)   
        else:
            cx.text(c1, -1, r'$C_1$', fontsize=10)
                
        if c2==y2 and self.ppf_mode==None:
            cx.text(-1.6, y2, r'$C_2=Y_2$', fontsize=10)
        elif c2==y_r and self.ppf_mode!=None:
            cx.text(-1.6, y_r, r'$C_2=Y_2$', fontsize=10)
        else:
            cx.text(-1, c2, r'$C_2$', fontsize=10)
                
        self.figure.subplots_adjust(left=0.12, right= 0.93,
                                        top=0.9, bottom=0.14)
        self.canvas.draw()

    def openInfoBilans(self):
        self.info=infoBilans()
        self.info.show()

class infoBilans(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Bilans_info.ui', self)
        self.textBrowser.setHtml("""
        <html>
        <body style="font-family:'Segoe UI'; font-size:11pt;">
        <p><b>1.</b> Nachylenie linii budżetowej w modelu wynosi <b>−(1 + r)</b>.</p>
        <p><b>2.</b> W rozważanym modelu przyjmujemy tożsamość makroekonomiczną:
        <b>CA = Y − C</b>.</p>
        <p><b>3.</b> W modelu wykorzystujemy następujące zależności:</p>
        <p>C<sub>1</sub> = β (Y<sub>1</sub> + Y<sub>2</sub> / (1 + r))</p>
        <p>C<sub>2</sub> = (1 − β) ((1 + r)Y<sub>1</sub> + Y<sub>2</sub>)</p>
        <p>C<sub>1,max</sub> = Y<sub>1</sub> + Y<sub>2</sub> / (1 + r)</p>
        <p>C<sub>2,max</sub> = (1 + r)Y<sub>1</sub> + Y<sub>2</sub></p>
        <p><b>Funkcja użyteczności:</b></p>
        <p>U = C<sub>1</sub><sup>β</sup> · C<sub>2</sub><sup>1−β</sup></p>
        <p><b>Linia budżetowa:</b></p>
        <p>C<sub>2</sub> = (1 + r)(Y<sub>1</sub> − C<sub>1</sub>) + Y<sub>2</sub></p>
        <p><b>Przekształcona funkcja użyteczności wykorzystywana do wizualizacji:</b></p>
        <p>C<sub>2</sub> = (U / C<sub>1</sub><sup>β</sup>)<sup>1 / (1 − β)</sup></p>
        <p><b>4.</b> Krzywe możliwości produkcyjnych (PPF) są modelowane w sposób uproszczony jako funkcje paraboliczne „przyklejone” do linii budżetowej.</p>
        <p>Dla orientacji na teraźniejszość i przyszłość przyjmujemy:</p>
        <p>C<sub>2</sub> = (1 + r)(Y<sub>1</sub> − C<sub>1</sub>) + Y<sub>2</sub> − k(C<sub>1</sub> − x<sub>0</sub>)<sup>2</sup></p>
        <p>gdzie x<sub>0</sub> oznacza punkt styczności z linią budżetową.</p>
        <p>Należy zaznaczyć, że wizualna forma krzywych możliwości produkcyjnych stanowi przybliżenie. Pomimo że spełniają one podstawowe własności modelu, ich kształt nie jest w pełni zgodny z rozwiązaniem teoretycznym. W przyszłych wersjach projektu planowane jest ich dalsze dopracowanie.</p>
        </body>
        </html>
        """)
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec())
