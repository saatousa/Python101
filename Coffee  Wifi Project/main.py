from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import ValidationError, InputRequired, DataRequired, URL
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Enter the name of your cafe")])
    location = StringField('Cafe location on Google Maps (URL)', validators=[URL(message="Invalid url")])
    open_time = StringField('Open Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Close Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_strength = SelectField('Wifi Strength Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    socket = SelectField('Power Socket Availability:', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')
    # Cancel = SubmitField('Cancel')


# Exercise:
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',  methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = []
        new_cafe.append(form.cafe.data)
        new_cafe.append(form.location.data)
        new_cafe.append(form.open_time.data)
        new_cafe.append(form.close_time.data)
        new_cafe.append(form.rating.data)
        new_cafe.append(form.wifi_strength.data)
        new_cafe.append(form.socket.data)
        with open('cafe-data.csv', 'a', newline='') as cafes_data:
            writer = csv.writer(cafes_data)
            writer.writerow(new_cafe)
        return cafes()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='\n') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
