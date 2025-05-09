from wsgiref.validate import validator

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange

from validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators = [InputRequired(), Email()])
    phone = IntegerField(validators = [InputRequired(), NumberLength(min = 1000000000, max = 9999999999)])
    name = StringField(validators = [InputRequired()])
    address = StringField(validators = [InputRequired()])
    index = IntegerField(validators = [InputRequired(), NumberRange(min = 100000, max = 999999)])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)