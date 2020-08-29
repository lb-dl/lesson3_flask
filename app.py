from flask import Flask
from flask import request
from utils import generate_random_password

app = Flask(__name__)

@app.route('/gen_password/')
def generate_password():
    password_len = request.args.get('password_len', '10')


    if not password_len.isdigit():
        return 'Eror, password_len should be digit'

    password_len = int(password_len)
    if password_len > 100:
        return 'Error, password_len should be less than 100'
    return generate_random_password(password_len)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)



