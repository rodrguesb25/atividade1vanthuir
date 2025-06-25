from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return """
    <h1>CRIEATIVE</h1>
    <img src="https://lh6.googleusercontent.com/rKMoeTTJpTpzolBSreJT-Lx6j16ZckeMtLmtX5vcuciAAuxPf1Y6r6PDiPcSUygeuTnL7eWbGhE6nNPGhHoIrGls9gr_wMNA8W_52IRB4rtlKPhaCHY87kSdZsiIUp-lPM6Om5UOEEHFJpxleRqi0e3tADU9V7eHeFChSstT8DBHAO1xL_7RTw=w1280" alt="" style="width: 300px;">
    <a href="/quemsomos"><p>Quem somos</p></a>
    <a href=""><p>Portifolio</p></a>
    <a href=""><p>Serviços</p></a>
    <a href="/contato"><p>Acesse meu WhatsApp</p></a>
"""

@app.route("/quemsomos")
def quemsomos():
    return """
    <p>Jean Mendes da Silva</p>
    <a href="/"><p>Voltar</p></a>
    """

@app.route("/contato")
def contato():
    return """
    <a href="https://www.instagram.com/jean_mendes05"><p>Contato</p></a>
    <a href="/"><p>Voltar</p></a>
    """

if _name_ == "_main_":
    app.run(debug=True)