# Avaliação Prática: Sistema de Organização de Transporte 

**Disciplina:** Lógica de Programação / Programação Orientada a Objetos  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS) - IFCE Campus Umirim  
**Professor:** Luis Rodolfo  

---

##  Contexto do Desafio

O campus do IFCE em Umirim recebe diariamente estudantes de diversas cidades e rotas da região. A coordenação de infraestrutura precisa de um script básico para ajudar a registrar a alocação dos alunos nos ônibus escolares, organizando as informações de cada estudante de acordo com os turnos de aula e as rotas disponíveis.

Seu objetivo é desenvolver um programa em **Python** que simule esse sistema de registro, aplicando obrigatoriamente os conceitos de **funções, passagem de parâmetros, estruturas condicionais e retornos (`return`)**.

##  Requisitos do Sistema

O seu código deve conter, no mínimo, as seguintes funcionalidades:

1. **Definição de Rotas:** O sistema deve ter uma forma de listar ou reconhecer as rotas de ônibus disponíveis (ex: Rota 1 - Centro, Rota 2 - Interior).
2. **Função de Validação de Turno:** Uma função que receba o horário da aula do aluno (ou o período) e utilize estruturas condicionais para retornar qual o turno correspondente (Manhã, Tarde ou Noite).
3. **Função de Alocação (`alocar_aluno`):** Uma função central que receba como parâmetros: o nome do aluno, a rota desejada e o turno. 
    * A função deve processar essas informações e retornar uma mensagem formatada confirmando o registro (ex: *"Aluno [Nome] cadastrado com sucesso na [Rota] para o turno da [Turno]."*).
4. **Execução Interativa:** O código final deve ter um menu ou fluxo simples (utilizando `input()`) para que o usuário (simulando um servidor do IFCE) possa digitar os dados e registrar pelo menos 3 alunos, demonstrando o programa funcionando na prática.

##  Regras de Avaliação (Atenção!)

Para que a prova seja validada, a entrega deve seguir **rigorosamente** os critérios abaixo:

* **Histórico de Desenvolvimento (Git):** O projeto deve ser construído de forma incremental. **Não serão aceitos repositórios com um único commit do tipo "projeto finalizado"**. O histórico de commits deve mostrar a evolução do seu código (ex: `feat: cria funcao de turno`, `feat: adiciona inputs do usuario`, `fix: corrige formatacao do texto`).
* **Código Limpo e Comentado:** Seu código deve ser legível e conter comentários breves explicando o que cada função faz.
* **A Defesa (Vídeo):** Você deve gravar um vídeo curto (3 a 5 minutos) compartilhando sua tela. No vídeo, você deve:
    1. Executar o código e mostrar ele funcionando no terminal.
    2. Explicar a lógica construída dentro das suas funções.
    3. Explicar por que escolheu determinadas estruturas (como os `if/elif` que você utilizou).

##  Como Entregar

1. Faça o **Push** de todo o seu código finalizado para este repositório.
2. Cole o **Link deste seu repositório GitHub** no local indicado na nossa plataforma de aulas.
3. Cole o **Link do seu vídeo de defesa** (pode ser YouTube não listado, Google Drive com permissão de leitura, Loom, etc.) junto com a entrega do link do repositório.

Boa sorte e bom código!
