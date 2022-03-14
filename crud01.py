import mysql.connector

conexao = mysql.connector.connect(
    host='ENDERECO',
    user='USER',
    password='SENHA',
    database='NOME_SCHEMA'
)

cursor = conexao.cursor()

#codigo

cursor.close()
conexao.close()
