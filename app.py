from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
import calculo

app = Flask(__name__) ## O app é o gerente do projeto da API, ele decide os que fazer

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculos.db' ##Configuração do banco de dados, nesse caso é um banco de dados SQLite chamado calculos.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ##Desativa uma funcionalidade que não é necessária, ajudando a economizar recursos
db = SQLAlchemy(app) ##Essa é a variável que vai fazer a comunicação com o banco de dados

class Historico(db.Model): ##Classe  que realiza a função de  criar uma tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) #Chave primaria
    n1 = db.Column(db.Float, nullable=False) #Número 1
    n2 = db.Column(db.Float, nullable=False) #Número 2
    operacao = db.Column(db.String(50), nullable=False) #Escolhe a operação
    resultado = db.Column(db.Float, nullable=False) #Vaariavél que contém os dados processados ou seja o resuktado

with app.app_context(): ##Garente que o contexto do aplicativo esteja relaciondo as configurações do APP especificadas acima
    db.create_all() #Verifica se a tabela já existe, se não existir ele cria a tabela

@app.route('/', methods=['GET']) ##Conecta o endereço da web ao codigo Python, o que possibilita roda-lo na API
def home():
    return "Bem vindo a API", 200


@app.route('/calcular', methods=['POST'])
def calcular(): ##Aqui eu criei a função calcular que irá fazer as operações matemáticas de acordo com o arquivo calculo.py
    if request.method == 'POST': ##Objeto que escuta o que o usuario está enviando, ou seja recebe os dados
        data = request.json ##Pega os dados no formato JSON pelo usuario
        operacao = data['operacao']
        n1 = data['n1']
        n2 = data['n2']
        resultado = 0 ##Incializa a variável com oresultado 0
        if operacao == 'soma':
            resultado = calculo.soma(n1, n2) ##Puxa cada função do classe calculo.py nesse caso soma

        elif operacao == 'subtracao':
            resultado = calculo.subtracao(n1, n2) ##Puxa cada função do classe calculo.py nesse caso subtração
            
        elif operacao == 'multiplicacao':
            resultado = calculo.multiplicacao(n1, n2) ##Puxa cada função do classe calculo.py nesse caso multiplicação
 
        elif operacao == 'divisao':
            resultado = calculo.divisao(n1, n2) ##Puxa cada função do classe calculo.py nesse caso divisao

        novo_calculo = Historico(n1=n1, n2=n2, operacao=operacao, resultado=resultado) ## Crio a variavel novo calculo que serve para salvar o histórico de entrada de dados e saida e atribuo a fução histórico pafra se adicionar a tabela
        db.session.add(novo_calculo)  ##Adicina  os dados da variavél novo_calculo na sessão do banco de daos
        db.session.commit() ##Confirma a adição dos dados no banco de dados

        return {'resultado': resultado}, 200 ##retorna o resultado da operação
    
@app.route('/historico', methods=['GET']) ##Aqui é o metodo GET quando o usuario requisita a API a vizuzalição do histórico de entrada e saida dos dados
def historico(): ##Função criada paraa vizualizar o histórico
    todos = Historico.query.all() ##É uma "query" que devolve todos os registros da tabela histórtico do BD 
    lista_saida = [] ##Cria uma variavél em forma de lista para armazenar os daodos de saída

    for registros in todos: ##Laço feito para percorrer todaa lista e devolver os registros
        lista_saida.append({ ##Adiciona os dados na lista de saída
            'id': registros.id,
            'n1': registros.n1,
            'n2': registros.n2,
            'operacao': registros.operacao,
                'resultado': registros.resultado
        })
    return jsonify(lista_saida), 200 ##Retorna a lista de saída em formato JSON

if __name__ == '__main__': ##Função main que inicializa a aplicação API
    app.run(host='0.0.0.0', port=5000, debug=True)    ##Define o host, porta e modo debug para a aplicação rodar






