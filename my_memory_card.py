from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)

questions = []
question_num = 0
correct = 0
incorrect = 0

class Question:
    def __init__(self, question='', ans1='', ans2='', ans3='', ans4='', correct_answer=''):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.correct_answer = correct_answer
    
    
question1 = Question(question='как звали автора романа "дубровский"?', ans1='пушкин', ans2='лермонтов', ans3='тютчев', ans4='што', correct_answer='пушкин')     
questions.append(question1)
question2 = Question(question='сколько будет 2 + 2?', ans1='2', ans2='4', ans3='5', ans4='я не знаю', correct_answer='4')     
questions.append(question2)
question3 = Question(question='как переводится i dont know?', ans1='я не знаю', ans2='не знаю', ans3='"я не знаю"', ans4='я не учил английский', correct_answer='"я не знаю"')     
questions.append(question3)
question4 = Question(question='какой океан омывает Антарктиду?', ans1='тихий', ans2='южный', ans3='атлантический', ans4='я не знаю', correct_answer='южный')     
questions.append(question4)
question5 = Question(question='как звали учёного, составившего таблицу хим. элементов?', ans1='менделеев', ans2='ломоносов', ans3='гук', ans4='я ничего не знаю', correct_answer='менделеев')     
questions.append(question5)
question6 = Question(question='какая болезнь была распространена в средневековье?', ans1='чума', ans2='грипп', ans3='орви', ans4='цинга', correct_answer='чума')     
questions.append(question6)

print(questions)

def check_answer():
    if rbtn_1.isChecked():
        return rbtn_1.text()
    elif rbtn_2.isChecked():
        return rbtn_2.text()
    elif rbtn_3.isChecked():
        return rbtn_3.text()
    elif rbtn_4.isChecked():
        return rbtn_4.text()
    
def next():
    global question_num
    if question_num < len(questions):
        res = questions[question_num]
        question_num += 1
        return res

def show_question(question: Question):
    if question is not None:
        lb_Question.setText(question.question)
        rbtn_1.setText(question.ans1)
        rbtn_2.setText(question.ans2)
        rbtn_3.setText(question.ans3)
        rbtn_4.setText(question.ans4)
    

def start_test():
    global q, correct, incorrect
    if btn_OK.text() == 'Следующий вопрос':
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText("Ответить")
        q = next()
        show_question(q)
    
    elif btn_OK.text() == 'Ответить':
        AnsGroupBox.show()
        RadioGroupBox.hide()
        btn_OK.setText('Следующий вопрос')

        if q.correct_answer == check_answer():
            correct += 1
            lb_Result.setText("Правильно")
            lb_Correct.setText(q.correct_answer)
        else:
            incorrect += 1
            lb_Result.setText("Неправильно")
            lb_Correct.setText(q.correct_answer)

        if question_num == len(questions):
            btn_OK.setText("Завершить викторину")

    elif btn_OK.text() == 'Завершить викторину':
        btn_OK.hide() 
        AnsGroupBox.hide()
        RadioGroupBox.hide()
        lb_Question.setText(f"Конец викторины\r\nПравильно: {correct}\r\nНеправильно: {incorrect}")
        


app = QApplication([])
    

# Создаем панель вопроса
btn_OK = QPushButton('Следующий вопрос')
btn_OK.clicked.connect(start_test)

lb_Question = QLabel('Самый сложный вопрос в мире!')


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()


app.exec()