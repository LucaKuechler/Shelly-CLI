import sys 
import os 
import time
from flask import Flask, render_template, request, jsonify, redirect, url_for
from data import DisplayDataList
from ShellLogic import main as backend


app = Flask(__name__)
elements_object = DisplayDataList()
logic = backend.Program()


@app.route("/", methods=['POST', 'GET'])
def Constructor():
    # should be loaded on start and everytime something is insterted
    elements = elements_object.getData()
    try:
        last_dir = elements[len(elements) - 1][1]
    except:
        last_dir = "/" 
    return render_template('home.html', elements=elements, last_dir = last_dir)




@app.route('/enter', methods=['POST', 'GET'])
def enter():
    t0 = time.time()
    inputData = request.form['command']

    if inputData:
        
        if inputData == "cls":
            elements_object.clearData()

        else: 
            curdir = elements_object.curDir
            logic.insert_command(curdir, inputData)
            output_data = logic.main_loop()
            t1 = time.time()
            total = t1 - t0
            if total == 0.0:
                total = 0.01
            li = [output_data['cur_dir'], inputData, output_data['cur_output'], total]
            elements_object.setData(li)
            

    return jsonify({'path' : 'asdf'})



@app.route("/tab", methods=['GET', 'POST'])
def tab():
    auto = 2
    return jsonify({'autocomplete' : auto})

  

@app.route("/settings")
def Settings():
    return render_template('settings.html') 



if __name__ == "__main__": 
    app.run(host='127.0.0.1', port=5000, debug=True) 

