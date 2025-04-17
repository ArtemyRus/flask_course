from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    up_time = subprocess.check_output(['uptime', '-p'], text = True)
    return f"Current uptime is {up_time[3:]}"


if __name__ == '__main__':
    app.run(debug=True)