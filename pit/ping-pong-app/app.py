import os
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    response = os.getenv('PONG_RESPONSE', 'Pong')
    port = os.getenv('PORT', '5000')
    return f"{response} from port {port}"

if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)