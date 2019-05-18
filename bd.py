from flaskext.mysql import MySQL

def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'concessionaria'

def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def get_idlogin(cursor, login, senha):
    cursor.execute(f'SELECT idlogin FROM login WHERE login = "{login}" and senha = "{senha}"')
    idlogin = cursor.fetchone()
    cursor.close()
    return idlogin[0]

def get_carros(cursor):
    cursor.execute(f'SELECT idcarros, nome, quilometragem, combustivel, cor, cambio, ano FROM carros')
    carros = cursor.fetchall()
    return carros

def consultar_carros(cursor, buscando):
    cursor.execute(f'SELECT nome FROM carros WHERE nome = "{buscando}"')
    consulta = cursor.fetchone()
    cursor.close()
    print(consulta)
    return consulta

def add_user(cursor, conn, login, senha):
    cursor.execute(f'INSERT INTO login (login, senha) values("{login}", "{senha})')
    conn.commit()