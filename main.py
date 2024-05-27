from flask import Flask, json
from faker import Faker

fake = Faker('pt_BR')

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def gerar_base():
    base = []

    for i in range(10):
        base.append(
            {
                'nome':fake.name(),
                'idade': fake.random_int(min=21, max=62),
                'ocupacao': fake.job(),
                'renda_anual': fake.random_number(digits=5, fix_len=True)
            }
        )
    resposta = json.dumps({'fake':base}, ensure_ascii=False, indent=4)
    return resposta, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)