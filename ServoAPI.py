import flask, os, hashlib
from flask import request

app = flask.Flask(__name__)

def check_auth(header):
    # 128 character random password, good enough
    hash = b'+4\x11l\x81c\xe1\xdd\xe4Y\x96i\xae\xd1\xd7\r\xfd\x9a\xb0N*\x95\xcbC\xa0B\x91e\x90\x9b\x84\x13'
    m = hashlib.sha256()
    m.update(header.encode())
    dig = m.digest()
    return hash == dig

@app.route("/turn", methods=["POST"])
def turn():
    auth = request.headers.get("Authorization")
    if auth and check_auth(auth):
        print("Running servo turn script!")
        os.system("/usr/bin/python /home/pi/dev/ServoAPI/turn180.py")
        return "ok"
    print("Attempt to make a turn without authorization!")
    return "Unauthorized", 403



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
