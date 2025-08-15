from flask import Flask, render_template, request
app= Flask (__name__)
#rota principal
@app.route("/")

def home():
 return render_template("index.html",
 mensagem = "ultimo dia",
 paragrafo= "boa noite",
 h2= "meu h2")

@app.route("/processar",methods= ["POST"])
def processar():
    nome = request.form["nome"]
    numero = request.form["numero"]
    mensagem = f"Olá {nome}, você digitou {numero}"
    return render_template("index.html",resultadoForm = mensagem)

  
 
if __name__== '__main__':
  app.run(debug=True)
