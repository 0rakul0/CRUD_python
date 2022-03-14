import psycopg2

# configurações
"""
configuraçãoes do docker
"""
host = 'localhost'
user = 'postgres'
password = 'sua senha'
database = 'postgres'
port = '15432'

try:
    conn_str = f'host={host} user={user} dbname={database} password={password} port={port}'
    conexao = psycopg2.connect(conn_str)
    print("conectado")
    cursor = conexao.cursor()
except:
    print("falha ao conectar")


def create_tabela():
    # criação de tabela
    try:
        cursor.execute(
            'CREATE TABLE inventario (\
	        id serial4 NOT NULL,\
	        "name" varchar(50) NULL,\
	        valor float8 NULL,\
	        quantidade int4 NULL,\
	        CONSTRAINT inventario_pkey PRIMARY KEY (id)\
            );')
        conexao.commit()
        print("Tabela Criada")
    except:
        print("A tabela já existe")


def create_produto(name, valor, quantidade):
    """
    :param name: nome do produto
    :param valor: valor unitário
    :param quantidade: quantidade em estoque
    """
    cursor.execute(f"INSERT INTO inventario (name,valor,quantidade) VALUES (%s, %s, %s);", (name, valor, quantidade))
    conexao.commit()


def find_all():
    """
    :return: retorna todos os itens
    """
    cursor.execute("SELECT*FROM inventario;")
    return cursor.fetchall()


def find_one(id):
    """
    :param id: do produto
    :return:
    """
    cursor.execute("SELECT * FROM inventario WHERE id=%s ;", (id,))
    return cursor.fetchall()


def update_user(id, name, valor, quantidade):
    cursor.execute("UPDATE inventario SET nome=%s, email=%s , senha=%s WHERE id=%s;", (name, valor, quantidade, id))


def delete_user(id):
    cursor.execute("DELETE FROM inventario WHERE id=%s ;", (id,))


if __name__ == "__main__":
    cursor = conexao.cursor()
    # create_tabela()
    # create_produto(name="laranja", valor=5.4, quantidade=7)
    cursor.close()
    conexao.close()
