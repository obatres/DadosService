from flask import Flask, request, json, Response
from random import randint as ran 
import json

app = Flask(__name__)

def retornarTiros(cantidad):
    tiros=[]
    for i in range(cantidad):
        tiros.append(ran(1,6))
    return tiros

@app.route('/tirar/<int:cantidad>', methods=['GET'])
def index(cantidad):
    if(type(cantidad)!=int or cantidad<=0):
        return Response(response="Número de dados a tirar no es válido",
                    status=400,
                    mimetype='application/json')
    else:
        tiros = retornarTiros(cantidad)
        res = {'dados': tiros}
        return Response(response=json.dumps(res),
                    status=200,
                    mimetype='application/json')

if __name__ == '__main__':

    app.run(debug=True, port=5001, host='0.0.0.0')