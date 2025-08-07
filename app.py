# app.py

from db_config import conectar

def main():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros;") # Exemplo de consulta seimples

            resultados = cursor.fechall()

            print("\nLivros cadastros:")
            for linha in resultados:
                print(linha)

        except Exception as e:
            print(f"Erro na execução: {e}")
        finally:
            conexao.close()
            print("\nConexão encerrada.")

if__name__ == "__main__":
    