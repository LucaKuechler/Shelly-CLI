import sys 
import os 
import time
from flask import Flask, render_template, request, jsonify, redirect, url_for
from data import DisplayDataList, InputDataElement
from ShellLogic import main as backend


app = Flask(__name__)
elements_object = DisplayDataList()
logic = backend.Program()


@app.route("/", methods=['POST', 'GET'])
def Constructor():
    # should be loaded on start and everytime something is insterted
    elements = elements_object.getData()
    return render_template('home.html', elements=elements)




@app.route('/enter', methods=['POST', 'GET'])
def enter():
    inputData = request.form['command']
    t0 = time.time()
    if inputData:
        print(inputData)
        curdir = elements_object.curDir     
        logic.insert_command(curdir, inputData)
        output_data = logic.main_loop()
        # li = ["asd", "asd", "asd", "asd"]
        # elements_object.setData(li)
        # elements_object.setData(input_field)
        # input_field = InputDataElement().getData()
        elements = elements_object.getData()

    t1 = time.time()
    total = t1 - t0
    print(f"{total} secconds")
    print(output_data)
    return ("nothing")



@app.route("/tab", methods=['GET', 'POST'])
def tab():
    auto = 2
    return jsonify({'autocomplete' : auto})

  

@app.route("/settings")
def Settings():
    return render_template('settings.html') 



if __name__ == "__main__": 
    app.run(host='127.0.0.1', port=5000, debug=True) 

