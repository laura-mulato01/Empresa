from banco import conectar

def inserir_departamento():
    nome = input("Digite o nome do departamento: ")
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
            INSERT INTO departamento(nome)
            VALUES (%s)
        """
    cursor.execute(sql,(nome,))
    conexao.commit()
    cursor.close()
    print("Departamento inserido com sucesso!")

def listar_departamento():
    conexao = conectar()
    cursor = conexao.cursor()

    sql= """
         SELECT id, nome FROM departamento ORDER BY id
         """
    cursor.execute(sql)
    departamentos = cursor.fetchall()

    print("\n======================================")
    print("Departamentos")
    print("\n======================================")

    for departamento in departamentos:
        print(
            f"ID:{departamento[0]} | "
            f"Nome:{departamento[1]}"
        )
    cursor.close()
    conexao.close()

def atualizar_departamento():
    id_departamento = input("Digite o ID do departamento: ")
    novo_nome = input("Digite o novo nome: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
       UPDATE departamento
       SET nome = %s
       WHERE id = %s
    """
    cursor.execute(
      sql,
      (novo_nome, id_departamento)
    )
    conexao.commit()
    if cursor.rowcount > 0:
       print("Departamento atualizado!")
    else:
       print("Departamento não encontrado.")
    cursor.close()
    conexao.close()

def deletar_departamento():
    id_departamento = input("Digite o ID do departamento: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
      DELETE FROM departamento
      WHERE id = %s
    """
    try:
     cursor.execute(sql, (id_departamento,))
     conexao.commit()

     if cursor.rowcount > 0:
        print("Departamento excluído!")
     else:
        print("Departamento não encontrado.")

    except Exception as erro:
        conexao.rollback()
        print("Não foi possível excluir.")
        print("Existem funcionários vinculados a este departamento.")

    cursor.close()
    conexao.close()

def pesquisar_departamento():
    nome = input("Digite o nome para pesquisar: ")

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        SELECT id, nome
        FROM departamento
        WHERE nome LIKE %s
        ORDER BY nome
    """

    cursor.execute(sql, (f"%{nome}%",))

    departamentos = cursor.fetchall()

    print("\nRESULTADO DA PESQUISA")

    for departamento in departamentos:
      print(
        f"ID: {departamento[0]} | "
        f"Nome: {departamento[1]}"
      )
      
    cursor.close()
    conexao.close()