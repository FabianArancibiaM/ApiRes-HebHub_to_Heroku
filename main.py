import os
import json
from flask import Flask, render_template
from flask import request
from flask import make_response

import controler.UserControlers as ControlUser
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Entro')
    req = request.get_json(silent=True, force=True)
    if request.method == 'POST':
        name = req.get('name')
        password = req.get('password')
        print('name: {} and password {}'.format(name,password))
        controlUser = ControlUser.UserControler(name,password)
        if controlUser.validarUser():
            datos = {
                'nombre': name, 'password': password
            }
        else:
            datos = {
                'menssage': "Error Login"
            }
    else:
        datos = {
            'menssage': "Error Methods"
        }


    res = json.dumps(datos, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % (port))
    app.run(debug=False, port=port, host='0.0.0.0')
