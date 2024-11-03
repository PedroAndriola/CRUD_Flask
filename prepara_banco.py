import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
    cursor = conn.cursor()

    # Criar ou substituir o banco de dados
    cursor.execute("DROP DATABASE IF EXISTS `biblioteca`;")
    cursor.execute("CREATE DATABASE `biblioteca`;")
    cursor.execute("USE `biblioteca`;")

    # Criar tabelas
    TABLES = {}
    TABLES['Livros'] = ('''
        CREATE TABLE `livros` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `genero` varchar(40) NOT NULL,
        `autor` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    TABLES['Usuarios'] = ('''
        CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    for tabela_nome in TABLES:
        tabela_sql = TABLES[tabela_nome]
        try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)
        else:
            print('OK')

    # Inserir usuários
    usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
    usuarios = [
        ("Pedro Andriola", "P.A", generate_password_hash("12345")),
        ("PeppaPig", "Peppaa", generate_password_hash("paozinho")),
        ("Mohamed", "Buum", generate_password_hash("python_flask"))
    ]
    cursor.executemany(usuario_sql, usuarios)

    cursor.execute('SELECT * FROM usuarios')  # Remova "biblioteca." aqui
    print('-------------  Usuários:  -------------')
    for user in cursor.fetchall():
        print(user[1])

    # Inserir livros
    livros_sql = 'INSERT INTO livros (nome, genero, autor) VALUES (%s, %s, %s)'
    livros = [
        ('Dom Casmurro', 'Romance Clássico Brasileiro', 'Machado de Assis'),
        ('God of War', 'Hack n Slash', 'PS2'),
        ('Mortal Kombat', 'Luta', 'PS2'),
        ('Valorant', 'FPS', 'PC'),
        ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
        ('Need for Speed', 'Corrida', 'PS2'),
    ]
    cursor.executemany(livros_sql, livros)

    cursor.execute('SELECT * FROM livros')  # Remova "Biblioteca." aqui
    print('-------------  Livros:  -------------')
    for livro in cursor.fetchall():
        print(livro[1])

    # Comitar as alterações
    conn.commit()

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    conn.close()
