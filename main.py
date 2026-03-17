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

    if len(dados_alunos) > 0:
        resultados = []
        maior_media = -1.0
        aluno_destaque = {"nome": "", "media": 0.0}
        
        print("\nProcessando tudo, aguarde...")
        
        for tupla_aluno in dados_alunos:
            nome_aluno = tupla_aluno[0]
            notas_aluno = tupla_aluno[1]
            
            media = calcular_media(notas_aluno)
            situacao = definir_situacao(media)
            
            resultados.append({
                "nome": nome_aluno,
                "media": media,
                "situacao": situacao
            })
            
            if media > maior_media:
                maior_media = media
                aluno_destaque["nome"] = nome_aluno
                aluno_destaque["media"] = media
        
        gerar_relatorio_txt(resultados, aluno_destaque)
        print("Finalizado! O arquivo 'resultado.txt' foi criado na pasta.")
    else:
        print("Nenhum dado válido foi inserido.")
        
if __name__ == "__main__":
    main()