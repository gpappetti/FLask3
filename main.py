from flask import Flask, jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def home():
    return 'Hello Dracar!!!'


ativo = [
        {
            'id': 1,
            'nome': u'PETROBRAS S.A.',
            'ticker': u'PETR3',
            'cotacao': 35.00
        },
        {
            'id': 2,
            'nome': u'VALE S.A.',
            'ticker': u'VALE3',
            'cotacao': 85.00
        }
    ]


@app.route('/api', methods=['GET'])
def api_ativos():
    return jsonify({'ativo': ativo})

if __name__ == '__main__':
    app.run()