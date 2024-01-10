from PyQt5.QtCore import *# подключение модулей
from PyQt5.QtWidgets import *
app = QApplication([])

window = QWidget() # создание окна
window.setWindowTitle("Анкета")  # заголовок
window.resize(400,600)

name1=QLabel("Ім'я")
name2=QLabel("Призвіще")
name3=QLabel("Дата народження")
name_w=QLineEdit() # поле вводе
name_h=QLineEdit()
name_v=QLineEdit()
laoyth_v=QVBoxLayout()
laoyth_h1=QHBoxLayout()
laoyth_h1.addWidget(name1)
laoyth_h1.addWidget(name_w)

laoyth_h2=QHBoxLayout()
laoyth_h2.addWidget(name2)
laoyth_h2.addWidget(name_h)
laoyth_h3=QHBoxLayout()
laoyth_h3.addWidget(name3)
laoyth_h3.addWidget(name_v)
laoyth_h4=QHBoxLayout()
s=QLabel("Стать")
s1=QRadioButton('ч')
s2=QRadioButton('ж')
laoyth_h4.addWidget(s)
laoyth_h4.addWidget(s1)
laoyth_h4.addWidget(s2)
laoyth_h5=QHBoxLayout()
c=QLabel("Улюбленне хобі")
c1=QCheckBox('футбол')# флажки
c2=QCheckBox('малювання')# флажки
c3=QCheckBox('волейбол')
laoyth_h5.addWidget(c)
laoyth_h5.addWidget(c1)
laoyth_h5.addWidget(c2)
laoyth_h5.addWidget(c3)
laoyth_h6=QHBoxLayout()
cat=QLabel("Порода котів")
cat1=QComboBox() # список
cat1.addItems(['Шпиц','Мяйкун','Хаски'])
laoyth_h6.addWidget(cat)
laoyth_h6.addWidget(cat1)
laoyth_v.addLayout(laoyth_h1)
laoyth_v.addLayout(laoyth_h2)
laoyth_v.addLayout(laoyth_h3)
laoyth_v.addLayout(laoyth_h4)
laoyth_v.addLayout(laoyth_h5)
laoyth_v.addLayout(laoyth_h6)
button=QPushButton('Ok') # кнопка
laoyth_v.addWidget(button)
window.setLayout(laoyth_v)
def hello():
    global index
    info_win=QMessageBox()
    info_win.setWindowTitle('Результат')
    info_win.setText('Дякуємо, ваша анкета заповнена \n'+name_w.text())
    info_win.exec_()

button.clicked.connect(hello)
window.show()
app.exec_()