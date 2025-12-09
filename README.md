# Treino-API
Projeto criado com o objetivo de treinar a criação de APIS em Python, Flask e banco de dados e compreender seu funcionamento e estrutura.

##Requisitos

-Docker + Docker Compose instalados-
-Porta 5000 livre para a API
- Instalar o venv com o comando ```bash  python3 -m venv venv" ````
- Usar o comando ```bash source venv/bin/activate````
  
##Subindo o ambiente

```bash
docker-compose up --build
```
##Teste rádpido via curl

```bash
curl -X POST
-H "Content-Type: application/json"
-d '{
"n1":100,
"n2": 50,
"operacao": "subtracao"
}' http://localhost:5000/calcular
````

##Resposta esperada: 
```json
{
  "resultado": 50
}
````

##Encerrando


Pressione `Ctrl+C`no terminal que está rodando o Docker ovu o app.py ou então execute:
```bash
docker-compose down
```




