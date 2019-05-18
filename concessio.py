from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import*

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

config(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        cursor = mysql.get_db().cursor()

        idlogin = get_idlogin(cursor, login, senha)

        if idlogin is None:
            return render_template('home.html', erro='Login/senha incorretos!')
        else:
            return render_template('comandos.html')

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

@app.route('/consultacarros', methods=['GET', 'POST'])
def consultacarros():
    if request.method == 'POST':
        buscando = request.form.get('buscando')
        cursor = mysql.get_db().cursor()
        teste = consultar_carros(cursor, buscando)
        if teste is None:
            return render_template('home.html', error='Nada encontrado!')

        else:
            cursor = mysql.get_db().cursor()
            return render_template('consultacarro.html', consulta=consultar_carros(cursor, buscando))
    return

@app.route('/add_user', methods=['POST'])
def adicionar_usuario():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        conn, cursor = get_db(mysql)

        add_user(cursor, conn, login, senha)

        cursor.close()
        conn.close()
        return 



if __name__ == '__main__':
    app.run(debug=True)