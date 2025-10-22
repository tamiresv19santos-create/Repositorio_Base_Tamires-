import sqlite3

# Passo 1 - Conectar/criar o banco
con = sqlite3.connect("escola.db")
cursor = con.cursor()

# Passo 2 - Criar a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    email TEXT
)
""")
print("Tabela criada com sucesso!\n")

# Passo 3 - Inserir dados
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("João", 20, "joao@example.com"))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Maria", 22, "maria@example.com"))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Carlos", 21, "carlos@example.com"))
con.commit()
print("Dados inseridos!\n")

# Passo 4 - Listar dados
cursor.execute("SELECT * FROM alunos")
for aluno in cursor.fetchall():
    print(aluno)
print("\n")

# Passo 5 - Atualizar um registro
cursor.execute("UPDATE alunos SET email = ? WHERE nome = ?", ("carla.doe@example.com", "Carla"))
con.commit()
print("Dados atualizados!\n")

# Passo 6 - Deletar um registro
cursor.execute("DELETE FROM alunos WHERE nome = ?", ("Carla",))
con.commit()
print("Registro deletado!\n")

# Encerrar conexão
con.close()