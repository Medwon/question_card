from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel , QVBoxLayout , QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup
)
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,400)

quest = QLabel('Какой национальности не существует?')
bt_an = QPushButton('Ответить')

c_or_i = QLabel('Правильно/Неправильно')

result = QLabel('Правильный ответ')

main_win.stat = 0


box = QGroupBox('Варианты ответов')
box_result = QGroupBox('Результат теста')

bt1 = QRadioButton('Энцы')
bt2 = QRadioButton('Чулымцы')
bt3 = QRadioButton('Смурфы')
bt4 = QRadioButton('Алеуты')

main_win.cur_quest = -1 


awnsers = [bt1 , bt2 , bt3 , bt4]

layH1 = QHBoxLayout()
layH2 = QHBoxLayout()
layH3 = QHBoxLayout()
layV1 = QVBoxLayout()
layV2 = QVBoxLayout()
layV3 = QVBoxLayout()
layH4 = QHBoxLayout()
layV4 = QVBoxLayout()


class Question():
    def __init__(self,question_for_box, rihgt  , wrong_1 , wrong_2 , wrong_3):
        self.question_for_box = question_for_box
        self.rihgt = rihgt
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

def show_result():
    box.hide()
    box_result.show()
    
    bt_an.setText('Следующий вопрос')

def show_question():
    box_result.hide()   
    box.show() 
    reset_bt = QButtonGroup()
    reset_bt.addButton(bt1) 
    reset_bt.addButton(bt2)
    reset_bt.addButton(bt3)
    reset_bt.addButton(bt4)
    reset_bt.setExclusive(False)
    bt1.setChecked(False)
    bt2.setChecked(False)
    bt3.setChecked(False)
    bt4.setChecked(False)
    reset_bt.setExclusive(True)
    bt_an.setText('Ответить')

def start_test():
    if bt_an.text() == 'Следующий вопрос':
        show_question()
    if bt_an.text() == 'Ответить':
        show_result()





def ask(q: Question):
    shuffle(awnsers)
    awnsers[0].setText(q.rihgt)
    awnsers[1].setText(q.wrong_1)
    awnsers[2].setText(q.wrong_2)
    awnsers[3].setText(q.wrong_3)
    quest.setText(q.question_for_box)
    result.setText(q.rihgt)
    show_question()

def correct(res):
    c_or_i.setText(res)
    show_result()

    

def check_awns():
    if awnsers[0].isChecked():
        correct('Правильно')

    else:
        correct('Не правильно')


def click_forbt():
    if bt_an.text() == 'Ответить':
        check_awns()
        print(1)
    else:
        next_quest()   
        print(2)

def next_quest():
    main_win.cur_quest += 1
    if main_win.cur_quest >= len(quest_list):
        main_win.cur_quest = 0
        shuffle(quest_list)
    q = quest_list[main_win.cur_quest]
    ask(q)


layH1.addWidget(quest , alignment = Qt.AlignCenter)
layV3.addLayout(layH1)

#вопросы
quest_list = []
quest_list.append(Question('Перевод слова enjoy?', 'наслаждатся', 'ходить' , 'переставлять', 'удивлятся'))
quest_list.append(Question('Какой стране пренадлижить Гринландия?', 'Дание', 'Италие' , 'Америке' , 'Канаде'))
quest_list.append(Question('Как расшифровывается BS','Brawl Stars','Berlin Start','Ben Strong','Bruh Slow'))
shuffle(quest_list)



#box
layV1.addWidget(bt1)
layV1.addWidget(bt3)
layV2.addWidget(bt2)
layV2.addWidget(bt4)
layH2.addLayout(layV1)
layH2.addLayout(layV2)
box.setLayout(layH2)
layV3.addWidget(box)

#box_result
layH4.addWidget(c_or_i)
layV4.addLayout(layH4)
layV4.addWidget(result, alignment= Qt.AlignCenter)
box_result.setLayout(layV4)
layV3.addWidget(box_result)


next_quest()

bt_an.clicked.connect(click_forbt)





layH3.addWidget(bt_an, alignment = Qt.AlignCenter)
layV3.addLayout(layH3)



main_win.setLayout(layV3)






main_win.show()
app.exec_()