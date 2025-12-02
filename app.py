from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
import calculo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n1 = db.Column(db.Float, nullable=False)
    n2 = db.Column(db.Float, nullable=False)
    operacao = db.Column(db.String(50), nullable=False)
    resultado = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return "Bem vindo a API", 200


@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        data = request.json
        operacao = data['operacao']
        n1 = data['n1']
        n2 = data['n2']
        resultado = 0
        if operacao == 'soma':
            resultado = calculo.soma(n1, n2)

        elif operacao == 'subtracao':
            resultado = calculo.subtracao(n1, n2)
            
        elif operacao == 'multiplicacao':
            resultado = calculo.multiplicacao(n1, n2)

        elif operacao == 'divisao':
            resultado = calculo.divisao(n1, n2)

        novo_calculo = Historico(n1=n1, n2=n2, operacao=operacao, resultado=resultado)    
        db.session.add(novo_calculo)
        db.session.commit()

        return {'resultado': resultado}, 200
    
    @app.route('/historico', methods=['GET'])
    def historico():
        todos = Historico.query.all()
        lista_saida = []

        for registros in todos:
            lista_saida.append({
                'id': registros.id,
                'n1': registros.n1,
                'n2': registros.n2,
                'operacao': registros.operacao,
                'resultado': registros.resultado
            })
        return jsonify(lista_saida)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)    






