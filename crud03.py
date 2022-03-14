import mysql.connector

conexao = mysql.connector.connect(
    host='ENDERECO',
    user='USER',
    password='SENHA',
    database='NOME_SCHEMA'
)


# codigo
# CREATE
def create(nome_produto, create_valor, create_qte):
    """
    :param nome_produto: nome do produto que será inserido na tabela
    :param create_valor: valor unitário do produto
    :param create_qte: quantidade de itens do mesmo produto
    :return:
    """
    comando_C = f'INSERT INTO `bdpython`.`vendas` (`nome_produto`, `valor`, `unidades`) ' \
                f'VALUES ("{nome_produto}", {create_valor}, {create_qte}) '
    cursor.execute(comando_C)
    conexao.commit()


# READ
def read():
    comando_R = 'SELECT * FROM `bdpython`.`vendas`'
    cursor.execute(comando_R)
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


# UPDATE
def updt(updt_nome, updt_valor, updt_qte):
    """
    :param updt_nome: valor do produto
    :param updt_valor: valor comercial unidade
    :param updt_qte: quantidade do produto em estoque
    :return:
    """
    comando_U = f'UPDATE vendas SET `valor` = {updt_valor} ,`unidades` = {updt_qte}' \
                f' WHERE (`nome_produto` = "{updt_nome}")'
    cursor.execute(comando_U)
    conexao.commit()


# DELETE
def delet(del_name="del_name"):
    """
    :param del_name: nome do produto para deletar
    :return:
    """
    comando_D = f'DELETE FROM vendas SET WHERE (`nome_produto` = "{del_name}")'
    cursor.execute(comando_D)
    conexao.commit()


if __name__ == "__main__":
    cursor = conexao.cursor()
    #create(nome_produto="pera", create_valor=3.60, create_qte=7)
    #read()
    cursor.close()
    conexao.close()
