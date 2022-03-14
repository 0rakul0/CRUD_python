import mysql.connector

conexao = mysql.connector.connect(
    host='ENDERECO',
    user='USER',
    password='SENHA',
    database='NOME_SCHEMA'
)

cursor = conexao.cursor()
# codigo
# CREATE
"""
    nome_produto: nome do produto que será inserido na tabela
    create_valor: valor unitário do produto
    create_qte: quantidade de itens do mesmo produto
"""
nome_produto = "atum"
create_valor = 6
create_qte = 32
comando_C = f'INSERT INTO `bdpython`.`vendas` (`nome_produto`, `valor`, `unidades`) ' \
            f'VALUES ("{nome_produto}", {create_valor}, {create_qte}) '
cursor.execute(comando_C)
conexao.commit()

# READ
comando_R = 'SELECT * FROM `bdpython`.`vendas`'
cursor.execute(comando_R)
resultado = cursor.fetchall()
print(resultado)

# UPDATE
"""
updt_nome: valor do produto
updt_valor: valor comercial unidade
updt_qte: quantidade do produto em estoque
"""
updt_nome = "updt"
updt_valor = 5
updt_qte = 23

comando_U = f'UPDATE vendas SET `valor` = {updt_valor} ,`unidades` = {updt_qte}' \
            f' WHERE (`nome_produto` = "{updt_nome}")'
cursor.execute(comando_U)
conexao.commit()

# DELETE
"""
del_name: nome do produto para deletar
"""
del_name = "del_name"
comando_D = f'DELETE FROM vendas SET WHERE (`nome_produto` = "{del_name}")'
cursor.execute(comando_D)
conexao.commit()

cursor.close()
conexao.close()
