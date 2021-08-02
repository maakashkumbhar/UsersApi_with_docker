import os
from flask import Flask,render_template,url_for,json,jsonify,request,make_response
import requests



app = Flask(__name__)


url='https://jsonplaceholder.typicode.com/users'

req=requests.get(url)
json_form=req.json()


@app.route('/home')
def hello_world():
    return render_template('index.html')

@app.route("/qstr")
def qs():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res

    res = make_response(jsonify({"error": "No Query String"}), 404)
    return res

@app.route("/getAllData")
def get_all_data():
    res = make_response(jsonify(json_form),200)
    return res


@app.route("/getDataWithID/<id>")
def getDataWithID(id):
    id1 = int(id)
    if len(json_form)<= id1:
        if json_form[id1-1]["id"] == int(id):
            res = make_response(jsonify(json_form[id1-1]),200)
            return res
        else:
            res = make_response(jsonify({"error":"cant find the id"}),400)
            return res
    else:
        res = make_response(jsonify({"error": "ID not in the list"}),400)
        return res

# @app.route("/getwithid/<id>")
# def getWithID(id):
#     jdata = json.loads(data)
#     for c in jdata:
#         if c['id']==id:
#             res = make_response(jsonify(c),200)
#             return res
#         else:
#             res  = make_response(jsonify({"error":"Cant Find Data"}),200)
#             return res
if __name__ == '__main__':
    app.run()
