from flask import Flask, render_template, request

app = Flask(__name__)

# BMI Calculation functions
def predict_bmi_centi(weight_c, height_c):
    height_in_meters = height_c / 100  # convert cm to meters
    return weight_c / (height_in_meters ** 2)

def predict_bmi_meter(weight_, height_):  # Height is in meters
    return weight_ / (height_ ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height_unit = request.form['height_unit']
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    if height_unit == "cm":
        bmi = predict_bmi_centi(weight, height)
    else:
        bmi = predict_bmi_meter(weight, height)

    category = bmi_category(bmi)

    return render_template('result.html', bmi=round(bmi, 1), category=category)

if __name__ == "__main__":
    app.run(debug=True)
