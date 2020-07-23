from flask import Flask, render_template, request, jsonify
from data import DisplayDataList, InputDataElement
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def Constructor():
    input_field = InputDataElement().getData()
    elements_object = DisplayDataList()
    elements_object.setData(input_field)
    elements = elements_object.getData()
    
    return render_template('home.html', elements=elements)



@app.route('/enter', methods=['POST'])
def enter():
    inputData = request.form['command']

    if inputData:
        print(inputData)

    return jsonify({'command' : inputData})


@app.route("/settings")
def Settings():
    return render_template('settings.html')


@app.route("/tab", methods=['GET', 'POST'])
def tab():
    print("works")
    auto = 2
    return jsonify({'autocomplete' : auto})



if __name__ == "__main__":
    app.run(debug=True)

