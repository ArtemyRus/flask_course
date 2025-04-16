from flask import Flask
from datetime import datetime

weekday = datetime.today().weekday()
weekdays_tuple = ("понедельника", "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья")

app = Flask(__name__)

@app.route('/hello-world/<username>')
def hello_world(username):
    if weekday == 2 or 4 or 5:
        return f'Привет, {username}! Хорошей {weekdays_tuple[weekday]}!'
    else: return f'Привет, {username}! Хорошего {weekdays_tuple[weekday]}!'

if __name__ == '__main__':
    app.run(debug=True)