from IPython.display import display, Math, Latex
from sympy import symbols, diff, init_printing, latex, Pow, UnevaluatedExpr
from ipywidgets import Button, HBox, VBox, Label
from random import randint

init_printing(use_unicode=True)


x = symbols('x')


def new_question():
    while 1:
        a = randint(-10, 10)
        if a != 0:
            break
        return a * x ** randint(1, 10)


question_label = Label()


q_a_couple = dict(question_latex='', answer_latex='')


def create_new_question_and_answer():
    f = new_question()
    a = diff(f)
    q_a_couple['question_latex'] = '$${}$$'.format(latex(f))
    q_a_couple['answer_latex'] = '$${}$$'.format(latex(a))
    question_label.value = q_a_couple['question_latex']

create_new_question_and_answer()
show_button = Button(description='Show answer')
next_button = Button(description='Next')
answer_label = Label('')


def on_show_click(*args):
    answer_label.value = q_a_couple['answer_latex']


show_button.on_click(on_show_click)


def on_next_click(*args):
    answer_label.value = ''
    create_new_question_and_answer()


next_button.on_click(on_next_click)

buttons_container = VBox([show_button, next_button])
main_container = HBox([question_label, buttons_container, Label(value='Answer: '), answer_label])

display(main_container)