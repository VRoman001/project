from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QListView, QFormLayout,QTextEdit,QInputDialog,QStyleFactory)

from random import shuffle # функція для переміщення відповідей
import json

app = QApplication([])
app.setStyle("Fusion")



# СТВОРЕННЯ ГОЛОВНОГО ВІКНА
window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('Memory Card')



'''
# СТВОРЕННЯ ВІДЖЕТІВ
btn_Menu = QPushButton('Меню') # кнопка повернення в головне меню
btn_Sleep = QPushButton('Відпочити') # кнопка забирає головне вікно і повертає його після того, як таймер пройде
box_Minutes = QSpinBox() # ввід кількості секунд
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст запитання

# СТВОРЕННЯ ПАНЕЛі З ВАРІАНТАМИ
RadioGroupBox = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів із відповідями

RadioGroup = QButtonGroup() # а це для групування перемикачів, щоб керувати їхньою поведінкою
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# СТВОРЕННЯ ПАНЕЛі З РЕЗУЛЬТАТАМИ
AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('') # тут розміщується напис "правильно" або "неправильно"
lb_Correct = QLabel('') # тут буде написано текст правильної відповіді




#  РОЗМІЩЕННЯ ПО ЛЕЯУТАХ

# Розміщуємо варіанти відповідей у два стовпці всередині групи:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді в перший стовпчик
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді в другий стовпчик
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #розміщуємо стовпці на одній лінії

RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей    
# розміщуємо результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо якомога довшим
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('секунд')) # 

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # задаємо величину кнопки
layout_line4.addStretch(1)

# Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробіли між вмістом

window.setLayout(layout_card)


question = 'Якого кольору банан?'
corect = 'Жовтий'
Wrong1 = 'Синій'
Wrong2 = 'Чорний'
Wrong3 = 'Червоний'

list1 =[rbtn_1,rbtn_2,rbtn_3,rbtn_4] 
shuffle(list1)
answer = list1[0]
w1 = list1[1]
w2 = list1[2]
w3 = list1[3]

def show_date ():
    lb_Question.setText(question)
    lb_Correct.setText(corect)
    answer.setText(corect)
    w1.setText(Wrong1) 
    w2.setText(Wrong2)
    w3.setText(Wrong3)


def check_result():
    a = answer.isChecked()
    if a:
        lb_Result.setText('Правильно')
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        b = w1.isChecked() or w2.isChecked() or w3.isChecked()
        if b:
            lb_Result.setText('Неправильно')
            RadioGroupBox.hide()
            AnsGroupBox.show()
            btn_OK.setText('Наступне запитання')

def ok():
    if btn_OK.text() == 'Наступне запитання':
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

    else:
        check_result()

btn_OK.clicked.connect(ok)   

show_date()



button1 = QPushButton('Нове питання')
button2 = QPushButton("Видалити питання")
button3 = QPushButton("Почати тренування")

text = QListView()


form = QFormLayout()



line1 = QLineEdit("")
line2 = QLineEdit("")
line3 = QLineEdit("")
line4 = QLineEdit("")
line5 = QLineEdit("")

form.addRow('Питання',line1)
form.addRow('Правильна відповідь:',line2)
form.addRow('Неправильна відповідь N1',line3)
form.addRow('Неправильна відповідь N2',line4)
form.addRow('Неправильна відповідь N3',line5)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_res = QVBoxLayout()

layout_line1.addWidget(text)
layout_line1.addLayout(form)


layout_line2.addWidget(button1)
layout_line2.addWidget(button2)

layout_line3.addWidget(button3)

layout_res.addLayout(layout_line1)
layout_res.addLayout(layout_line2)
layout_res.addLayout(layout_line3)
window.setLayout(layout_res)



#ФАЙЛИ--!

with open('pyton.txt', 'r') as f:
    f = f.read()
    print(f)
a = input("Хочете добавити тект?")
while a == "так":
    g = input("Введіть текст")
    with open('pyton.txt', 'a') as d:
        d = d.write(g)
        
        with open('pyton.txt', 'r') as j:
            j = j.read()
            print(j)
            a = input("Хочете добавити тект?")
print("oK")
'''



button1 = QPushButton('Створити замітки')
button2 = QPushButton('Видалити замітки')
button3 = QPushButton('Зберегти замітки')
button4 = QPushButton('Створии тег')
button5 = QPushButton('Видалити тег')
button6 = QPushButton('Шукати замітку по тегу')

text = QLabel()
text1 = QLabel()

Line = QLineEdit()
Line.setStyleSheet("background-color : aliceblue ")

Ed = QTextEdit()
Ed.setStyleSheet("background-color : aliceblue ")

list1 = QListWidget()
list1.setStyleSheet("background-color : aliceblue ")

list2 = QListWidget()
list2.setStyleSheet("background-color : aliceblue ")

H = QHBoxLayout()
H1 = QHBoxLayout()
H2 = QHBoxLayout()

V = QVBoxLayout()
V1 = QVBoxLayout()


V.addWidget(Ed)




H1.addWidget(button1)
H1.addWidget(button2)

V1.addWidget(text) 
V1.addWidget(list1)
V1.addLayout(H1)
V1.addWidget(button3)
V1.addWidget(text1)
V1.addWidget(list2)
V1.addWidget(Line)

H2.addWidget(button4)
H2.addWidget(button5)
V1.addLayout(H2)
V1.addWidget(button6)

H.addLayout(V)
H.addLayout(V1)
window.setLayout(H)


def show_notes():
    key = list1.selectedItems()[0].text()
    Ed.setText(notes[key]["text"])
    list2.clear()
    list2.addItems(notes[key]['tags'])

def add_notes():
    dialog,ok = QInputDialog.getText(window,'Додати замітку','Назва замітки')
    if dialog and ok != "":
        notes[dialog] = {'text':"","tags":[]}
        list1.addItem(dialog)

def save_notes():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        notes[key]["text"] = Ed.toPlainText()
        with open("a.json","w") as file:
            json.dump(notes,file)

def del_notes():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        del notes[key]
        Ed.clear()
        list1.clear()
        list1.addItems(notes)
        with open("a.json","w") as file:
            json.dump(notes,file)

def add_tags():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        tag = Line.text()
        if not tag in notes[key]['tags']:
            notes[key]['tags'].append(tag)
            list2.addItem(tag)
            Ed.clear()
            with open("a.json","w") as file:
                json.dump(notes,file)
        else:
            print('')

def del_tags():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        tag = list2.selectedItems()[0].text()
        notes[key]['tags'].remove(tag)
        list2.clear()
        list2.addItems(notes[key]['tags'])
        with open("a.json","w") as file:
            json.dump(notes,file)

def search_tags():
    tag = Line.text()
    if button6.text() == "Шукати замітку по тегу" and tag:
        notes_f = {}
        for i in notes:
            if tag in notes[i]['tags']:
                notes_f[i] = notes[i]
        button6.setText("Скасувати")
        list1.clear()
        list2.clear()
        list1.addItems(notes_f)
    elif button6.text() ==  "Скасувати":
        list1.clear()
        list2.clear()
        Ed.clear()
        list1.addItems(notes)
        button6.setText("Шукати замітку по тегу")
    else:
        pass



button2.clicked.connect(del_notes)
list1.itemClicked.connect(show_notes)
button1.clicked.connect(add_notes)
button3.clicked.connect(save_notes)
button4.clicked.connect(add_tags)
button5.clicked.connect(del_tags)
button6.clicked.connect(search_tags)

with open("a.json","r") as file:
    notes = json.load(file)
list1.addItems(notes)
window.show()
app.exec_()