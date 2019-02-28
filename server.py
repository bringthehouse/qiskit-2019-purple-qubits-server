from flask import Flask
from flask import request
from flask import jsonify
from api import run_qasm
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Move along! Nothing to see here!"

@app.route('/api/run/qasm', methods=['POST'])
def qasm():
    # print(request.data)
    # print("-----------------------------------")
    # data = json.loads(request.data)
    # print(data)
    # print ("_______________________")
    # qasm = data['qasm']
    # backend = 'qasm_simulator'

    # data['qasm'] = request.form.get('qasm')
    # backend = data['backend'] if 'backend' in data else 'qasm_simulator'

    qasm = request.form.get('qasm')
    # data = request.get_data()
    # print("------------------------------------")
    # print(data)
    # print("------------------------------------")
    # # print(json.loads(data))
    # print (data)
    print("--------------")
    print (qasm)
    print(request.get_data())
    # print(qasm)
    # print("????????????????????", request.form.get('field1'))
    print (request.form)

    # print(request.get_json(force=True))
    # data = request.get_json(force=True)
    # qasm = data['qasm']
    backend = 'qasm_simulator'



    # backend = 'qasm_simulator' if not backend else backend


    # qasm = body["qasm"]
    # if "backend" in body:
    #     backend = body["backend"]
    # else:
    #     backend = "qasm_simulator"
    output = run_qasm(qasm, backend)
    ret = {"result": output}
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)