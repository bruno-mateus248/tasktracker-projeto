# TaskTracker CLI — Gerenciador de Tarefas em Python

Aplicação de linha de comando (CLI) desenvolvida em **Python 3** para o gerenciamento estruturado de tarefas diárias e acadêmicas, construída como parte do desafio cumulativo da disciplina **Bootcamp II** (Fase 2 — Entrega Intermediária).

## Identificação do Desenvolvedor

* **Estudante:** Bruno Mateus Borges
* **Curso:** Ciência da Computação — Centro Universitário de Brasília (CEUB)
* **Campus / Polo:** Asa Norte (Noturno)
* **Disciplina:** Bootcamp II

## Descrição Funcional

O **TaskTracker** soluciona a perda de prazos e a falta de priorização no controle de atividades diárias por meio de uma interface de terminal rápida, intuitiva e com validação rigorosa de dados:

* **Menu Interativo Contínuo:** Navegação direta via terminal com opções para cadastrar tarefas, listar registros ou encerrar o sistema.
* **Estrutura de Dados Padronizada:** Cada tarefa é armazenada em memória como um dicionário Python contendo `titulo`, `descricao`, `prioridade`, `data_limite` e `status`.
* **Validação Estrita de Regras de Negócio:**
  * **Título Obrigatório:** Rejeita entradas vazias ou compostas apenas por espaços em branco, solicitando nova digitação até que um título válido seja informado.
  * **Prioridade Padronizada:** Aceita exclusivamente as opções `Alta`, `Média` (ou `Media`) e `Baixa`, exibindo mensagem de erro e repetindo o prompt para entradas fora do padrão.
  * **Status Automático:** Toda tarefa cadastrada recebe automaticamente o status inicial `"Pendente"`.
* **Exibição Formatada:** Informa claramente quando não existem tarefas cadastradas e, quando há registros, apresenta todas as propriedades numeradas e organizadas no terminal.

## Arquitetura e Estrutura do Repositório

O repositório segue a árvore arquitetural planejada na Fase 1 do projeto:

```text
tasktracker-projeto/
├── README.md                  # Documentação principal da aplicação e instruções de uso
├── .gitignore                 # Regras para ignorar arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf # PDF com o planejamento lógico e arquitetural entregue na Fase 1
└── src/
    └── main.py                # Código-fonte principal da aplicação TaskTracker em Python
```

## Tecnologias Utilizadas

* **Linguagem:** Python 3.8+ (Biblioteca Padrão, sem necessidade de dependências externas)
* **Controle de Versão:** Git e GitHub

## Guia de Instalação e Execução

1. **Clone o repositório do GitHub para sua máquina local:**
   ```bash
   git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
   ```

2. **Acesse a pasta raiz do projeto:**
   ```bash
   cd tasktracker-projeto
   ```

3. **Execute a aplicação diretamente pelo terminal:**
   ```bash
   python3 src/main.py
   ```
   *(No Windows, caso utilize o instalador padrão do Python, você também pode executar `python src/main.py`)*.

## Exemplo de Uso no Terminal

1. Escolha a opção **`1`** no menu para cadastrar uma nova tarefa.
2. Informe o **Título** (teste pressionar *Enter* vazio para verificar a trava de validação funcionando).
3. Digite a **Descrição**, a **Prioridade** (`Alta`, `Média` ou `Baixa`) e a **Data Limite** (`DD/MM/AAAA`).
4. Escolha a opção **`2`** no menu para visualizar o relatório completo de tarefas pendentes.
5. Escolha a opção **`3`** para encerrar a aplicação com segurança.
