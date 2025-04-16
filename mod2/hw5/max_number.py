from flask import Flask, abort

app = Flask(__name__)


@app.route("/max_number/<path:nums>")
def max_number(nums):
    list_nums = nums.split("/")
    numbers = []
    for i in list_nums:
        try:
            numbers.append(float(i))
        except ValueError as er:
            print(er)
    max_value = max(numbers)
    return f"Максимальное число: {max_value}"


if __name__ == "__main__":
    app.run(debug=True)
