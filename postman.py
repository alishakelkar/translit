import json
import os
from flask import Flask, redirect, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
output_path = ''

#old RAW form. Takes in JSON
@app.route('/test', methods =['GET', 'POST'])
def test():
    if request.method == 'GET':
        return jsonify({"response": "Get Request Called"})
    elif request.method == "POST":
        req_Json = request.json
        input_path = req_Json['input_path']
        output_path = req_Json['output_path']
        lang_code = req_Json['lang_code']
        cmd = "cd /datadrive/nt_translit/IndicXlit/inference/cli/ && python3 transliterate_task.py "
        # os.system(cmd)
        # cmd = "python3 transliterate_task.py  "
        returned_value = os.system(cmd + input_path + ' ' + output_path + ' ' + "'" + lang_code + "'") 
        
        
        # output_path = req_Json['output_path']
        #return jsonify({"Output" : "Find at " + output_path})
        return jsonify({"response": "Success!", "input_path" : "Input path is " + input_path, "output_path" : "Output path is " + output_path, "lang_code": lang_code})


#form-data

@app.route('/upload', methods=['POST'])
def signin():
    req_form = request.form

    current = str(os.getcwd())

    input_file = request.files['input_file']
    save_path = os.path.join(os.getcwd(), secure_filename(input_file.filename))
    # input_file.save(os.path.join(os.getcwd(), secure_filename(input_file.filename)))
    input_file.save(save_path)

    input_path = save_path
    #input_path = req_form['input_path']
    output_path = req_form['output_path']
    lang_code = req_form['lang_code']
    cmd = "cd /datadrive/nt_translit/IndicXlit/inference/cli/ && python3 transliterate_task.py "

    returned_value = os.system(cmd + input_path + ' ' + output_path + ' ' + "'" + lang_code + "'") 
    

    d = pd.read_csv(output_path,  encoding='utf8')
    df = pd.DataFrame(d)

    '''
    with open('daf.json', 'w', encoding='utf-8') as file:
        data = df.to_json(file, force_ascii=False)

    new_df = pd.read_json('daf.json')
    '''

    df_json = df.to_json()
    #json.loads(new_df)
    
    '''with open('encoded.json', 'w', encoding='utf-8') as file:
        data = df_json
        '''
    #return jsonify(json.dump(new_df))
    return jsonify({"response": "Success!", "input_path" : input_path, "output_path" : output_path, "lang_code": lang_code, "output" : df_json}) 

if __name__ == '__main__':
    app.run(debug=True, port=8080)