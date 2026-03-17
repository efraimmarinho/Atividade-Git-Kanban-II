def validar_notas(lista_notas):
   
    if not lista_notas:
        return False
    return True

def calcular_media(notas):
   
    if not validar_notas(notas):
        return 0.0
    
    
    return sum(notas) / len(notas)

def definir_situacao(media):
   
    if media < 7.0:
        return "Recuperação"
    else:
        return "Aprovado"

def gerar_relatorio_txt(dados, top_student):
   
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== RELATÓRIO DE NOTAS ===\n")
        
        for aluno in dados:
            linha = f"Aluno: {aluno['nome']} | Média: {aluno['media']:.2f} | Situação: {aluno['situacao']}\n"
            arquivo.write(linha)
            
        arquivo.write("-" * 25 + "\n")
        arquivo.write(f"DESTAQUE DA TURMA: {top_student['nome']} (Média {top_student['media']:.2f})\n")