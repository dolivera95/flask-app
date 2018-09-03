from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name = 'Mundo'):
	name = request.args.get("name", name)
	return "Hola {}".format(name)


@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
	#Diccionario con variables
	context = {'num_1' : num1, 'num_2': num2}
	#**Descomprimir diccionario
	return render_template("add.html", **context)



app.run(debug = True, port=8000, host='0.0.0.0')
