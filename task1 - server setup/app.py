from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello <strong>HNGi9</strong>, this is Olawale Olaleye</h1>'


@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        'slackUsername': 'ddosbro',
        'backend': True,
        'age': 25,
        'bio': 'I like to push my limits'
    })


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=3000)
