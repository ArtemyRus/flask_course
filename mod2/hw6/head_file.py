from flask import Flask
import os

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    path = os.path.abspath(relative_path)
    with open(path, 'r', encoding='utf-8') as file:
        try:
            result_text = file.read(size)
            result_size = len(result_text)
            result = f"<b>{path}</b> {result_size}<br>{result_text}"
            return result
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app.run(debug=True)