from flask import Flask, request  
import calculo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

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

        return {'resultado': resultado}, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)    






