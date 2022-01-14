from flask import Flask, jsonify, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def home():
    return render_template("homepage.html")


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

#upload site
if __name__ == '__main__':
    app.run(debug=True)

#servidor do heroku

