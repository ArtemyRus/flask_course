from flask import Flask, request
import subprocess
import shlex
from typing import List

app = Flask(__name__)


@app.route("/ps", methods=['GET'])
def ps() -> str:
    args: List[str] = request.args.getlist('arg')
    args_clean = [shlex.quote(arg) for arg in args]
    cmd_str = f"ps {' '.join(args_clean)}"
    cmd = shlex.split(cmd_str)
    result = subprocess.run(cmd, capture_output=True)
    output = result.stdout.decode()
    return f'<pre>{output}</pre>'

if __name__ == '__main__':
    app.run(debug=True)