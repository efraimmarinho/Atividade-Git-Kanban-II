from processamento import calcular_media, definir_situacao, gerar_relatorio_txt

def main():
    dados_alunos = []

    print(" SISTEMA DE NOTAS SENAI ")
    print("Digite 'sair' no nome do aluno para encerrar.\n")

    while True:
        nome = input("Nome do aluno: ").strip()
        if nome.lower() == 'sair':
            break

        try:
            notas_str = input(f"Digite as notas de {nome} (separadas por espaço): ")
            notas = [float(n) for n in notas_str.split()]

            dados_alunos.append((nome, notas))
            print("Notas salvas com sucesso!\n")

        except ValueError:
            print(" Digite apenas números separados por espaço.\n")
            
if __name__ == "__main__":
    main()