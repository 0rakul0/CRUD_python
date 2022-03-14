import mysql.connector

conexao = mysql.connector.connect(
    host='ENDERECO',
    user='USER',
    password='SENHA',
    database='NOME_SCHEMA'
)

cursor = conexao.cursor()

#codigo
cursor.execute("CREATE TABLE vendas (id serial PRIMARY KEY, name_produto VARCHAR(50), valor FLOAT, unidades INTEGER);")

cursor.close()
conexao.close()
