Requisitos Funcionais (RF)

 RF01: Processar o cadastro de alunos e o recebimento de suas respectivas notas.
 RF02: Calcular a média aritmética das notas de cada aluno cadastrado.
 RF03: Identificar automaticamente o "Top Student" (aluno com a maior média da turma).
 RF04: Gerar um arquivo `resultado.txt` contendo o relatório final formatado com a situação de toda a turma.
Requisitos Não-Funcionais (RNF)

 RNF01: Modularização obrigatória do código, separando as responsabilidades entre `main.py` e `processamento.py`.
 RNF02: Tratamento de erros robusto para barrar a entrada de dados vazios ou corrompidos.
 RNF03: Uso de versionamento Git simulando ambiente colaborativo com fluxo de branches separadas por funcionalidade.
Regras de Negócio (RN)

 RN01: A estrutura de dados principal do sistema deve ser uma lista de tuplas no formato: `[("Nome", [notas])]`.
 RN02: O número de notas lançadas por aluno é variável (nem todos têm a mesma quantidade de atividades).
 RN03: Alunos que obtiverem média inferior a 7.0 devem ser classificados com a situação "Recuperação".
