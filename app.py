from flask import Flask

app = Flask(__name__)


def sum(a,b):

    q = 'qwe'
    result = a+b

    result = f"{q} - {result}"

    return result

@app.route('/')
def hello_world():
    a=3
    b=5
    c=sum(a,b)
    return f'Hello World! {c}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
