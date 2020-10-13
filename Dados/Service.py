from flask import Flask, request, json, Response
import json

app = Flask(__name__)



@app.route('/cantidad', methods=['GET'])
def index():
    res = {'Status': 'Successfully ' + 'request ok'}
    return Response(response=json.dumps(res),
                    status=200,
                    mimetype='application/json')

if __name__ == '__main__':

    app.run(debug=True, port=5001, host='0.0.0.0')