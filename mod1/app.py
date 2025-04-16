import datetime
import random
import os
import re
from flask import Flask

app = Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words():
    with open(BOOK_FILE, encoding='utf-8') as book:
        text = book.read()
        words_list = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)
    return words_list

words = get_words()


@app.route('/hello_world')
def hello_world():
    return 'Привет мир!'


@app.route('/cars')
def print_cars():
    return ", ".join(cars)


@app.route('/cats')
def get_random_cat():
    return random.choice(cats)


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def test_function():
    delta = datetime.timedelta(hours=1)
    current_time = datetime.datetime.now()
    current_time_after_hour = (current_time + delta).strftime('%H:%M:%S')
    return f'Точное время через час будет {current_time_after_hour}'

@app.route('/get_random_word')
def get_random_word():
    word = random.choice(words)
    return word


@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страница была открыта {counter.visits} раз.'

counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)
