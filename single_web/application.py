from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '这是一个简单的 Flask Web 服务器'


@app.route('/calculate/<n_size>')
def calculate(n_size):
    def logic(number):
        if number == 2:
            return 2
        return number * logic(number - 1)

    return str(logic(int(n_size)))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
