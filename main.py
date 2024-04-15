from flask import Flask, jsonify
from services.especificacoes import especificacao_1, especificacao_2, especificacao_3
from environs import Env

app = Flask(__name__)
env = Env()
env.read_env()


@app.route('/')
def hello():
    return jsonify({'message': env.str("version")})

@app.route('/generate_report_1', methods=['GET'])
def generate_report1():
    especificacao_1()

    return jsonify({'message': 'running'})

@app.route('/generate_report_2', methods=['GET'])
def generate_report2():
    especificacao_2()

    return jsonify({'message': 'running'})

@app.route('/generate_report_3', methods=['GET'])
def generate_report3():
    especificacao_3()

    return jsonify({'message': 'running'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)