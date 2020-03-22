from flask import Flask, request, abort
import json
from model.rsa import rsa
from model.eg import eg
from model.dh import dh
from model.egr import egr
from model.uegr import uegr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/rsa/random/')
def getpq():
    return json.dumps(rsa().get_random_numbers().__dict__)


@app.route('/rsa/privatekey/', methods=['POST'])
def get_private_key():
    return json.dumps(rsa(p=request.json["p"], q=request.json["q"], e=request.json["e"]).get_private_key().__dict__)


@app.route('/rsa/encrypt/', methods=['POST'])
def get_encryption():
    return json.dumps(rsa(p=request.json["p"], q=request.json["q"], e=request.json["e"], m=request.json["m"])
                      .get_encryption().__dict__)


@app.route('/rsa/decrypt/', methods=['POST'])
def get_decryption():
    return json.dumps(rsa(p=request.json["p"], q=request.json["q"], c=request.json["c"], d=request.json["d"])
                      .get_decryption().__dict__)


@app.route('/eg/public/', methods=['POST'])
def eg_get_public_key():
    return json.dumps(eg(x=request.json["x"]).get_public_key().__dict__)


@app.route('/eg/c1/', methods=['POST'])
def get_c1():
    return json.dumps(eg(r=request.json["r"]).getc1().__dict__)


@app.route('/eg/c2/', methods=['POST'])
def get_c2():
    return json.dumps(eg(m=request.json["m"], y=request.json["y"], r=request.json["r"]).getc2().__dict__)


@app.route('/eg/decrypt/', methods=['POST'])
def eg_get_decryption():
    return json.dumps(eg(c1=request.json["c1"], c2=request.json["c2"],x = request.json["x"]).get_decryption().__dict__)

@app.route('/dh/c1/', methods=['POST'])
def getX():
    return json.dumps(dh(x=request.json["x"]).getX().__dict__)

@app.route('/dh/c2/', methods=['POST'])
def getY():
    return json.dumps(dh(y=request.json["y"]).getY().__dict__)

@app.route('/dh/k1/', methods=['POST'])
def getK1():
    return json.dumps(dh(Y=request.json["Y"],x = request.json["x"]).getK1().__dict__)

@app.route('/dh/k2/', methods=['POST'])
def getK2():
    return json.dumps(dh(X=request.json["X"],y = request.json["y"]).getK2().__dict__)

@app.route('/egr/public/', methods=['POST'])
def egr_get_public_key():
    return json.dumps(egr().get_public_key(request.json))


@app.route('/egr/c1/', methods=['POST'])
def egr_get_c1():
    return json.dumps(egr().getc1(request.json))


@app.route('/egr/c2/', methods=['POST'])
def egr_get_c2():
    return json.dumps(egr().getc2(request.json))

@app.route('/egr/ree/', methods=['POST'])
def egr_get_ree():
    return json.dumps(egr().get_reencryption(request.json))

@app.route('/egr/dec/', methods=['POST'])
def egr_get_dec():
    return json.dumps(egr().get_decryption(request.json))

@app.route('/uegr/public/', methods=['POST'])
def uegr_get_public_key():
    return json.dumps(uegr().get_public_key(request.json))

@app.route('/uegr/c1/', methods=['POST'])
def uegr_get_c1():
    return json.dumps(uegr().get_c1(request.json))

@app.route('/uegr/c2/', methods=['POST'])
def uegr_get_c2():
    return json.dumps(uegr().get_c2(request.json))

@app.route('/uegr/c3/', methods=['POST'])
def uegr_get_c3():
    return json.dumps(uegr().get_c3(request.json))

@app.route('/uegr/c4/', methods=['POST'])
def uegr_get_c4():
    return json.dumps(uegr().get_c4(request.json)) 

@app.route('/uegr/c1_/', methods=['POST'])
def uegr_get_c1_():
    return json.dumps(uegr().get_c1_(request.json))

@app.route('/uegr/c2_/', methods=['POST'])
def uegr_get_c2_():
    return json.dumps(uegr().get_c2_(request.json))

@app.route('/uegr/c3_/', methods=['POST'])
def uegr_get_c3_():
    return json.dumps(uegr().get_c3_(request.json))

@app.route('/uegr/c4_/', methods=['POST'])
def uegr_get_c4_():
    return json.dumps(uegr().get_c4_(request.json))

@app.route('/uegr/dec/', methods=['POST'])
def uegr_get_dec():
    return json.dumps(uegr().get_decryption(request.json))    


if __name__ == '__main__':
    app.run(debug=True)
