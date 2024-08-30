# Meu Gerenciador de Tarefas

Este é um aplicativo de gerenciamento de tarefas simples desenvolvido com Python e Tkinter. O aplicativo permite adicionar, editar, excluir e marcar tarefas como concluídas.

## Funcionalidades

- **Adicionar Tarefa**: Insira uma nova tarefa no campo de entrada e clique no botão "Adicionar Tarefa".
- **Editar Tarefa**: Clique no ícone de editar ao lado de uma tarefa para alterá-la.
- **Excluir Tarefa**: Clique no ícone de excluir ao lado de uma tarefa para removê-la.
- **Marcar como Concluída**: Use a caixa de seleção para marcar uma tarefa como concluída, aplicando um estilo de texto riscado.

## Como Executar

1. **Pré-requisitos**: Certifique-se de ter o Python 3 e Tkinter instalados em seu sistema. O Tkinter geralmente vem pré-instalado com Python.

2. **Baixar o Código**:
   - Clone o repositório ou baixe o arquivo do código fonte.

3. **Executar o Código**:
   - Navegue até o diretório contendo o arquivo do código e execute-o com o Python:
     ```sh
     python nome_do_arquivo.py
     ```

4. **Imagens**:
   - O código usa imagens para os ícones de editar e excluir. Certifique-se de ter os arquivos `editar.png` e `excluir.png` no mesmo diretório do arquivo Python, ou ajuste o caminho no código para corresponder à localização das imagens.

## Estrutura do Código

- **Interface do Usuário**: Utiliza Tkinter para criar a interface gráfica.
- **Funções**:
  - `add_tarefa()`: Adiciona uma nova tarefa ou atualiza uma tarefa existente.
  - `add_item_tarefa(tarefa)`: Adiciona um item de tarefa à lista.
  - `preparar_edicao(frame_tarefa, label_tarefa)`: Prepara uma tarefa para edição.
  - `atualizar_tarefa(nova_tarefa)`: Atualiza uma tarefa existente.
  - `deletar_tarefa(frame_tarefa)`: Exclui uma tarefa com confirmação.
  - `alterar_sublinhado(label)`: Marca uma tarefa como concluída com texto riscado.

## Contribuindo

Se você encontrar bugs ou quiser melhorar o código, sinta-se à vontade para fazer um fork do repositório e enviar um pull request. Sugestões e contribuições são bem-vindas!

## Sobre o Autor

Este projeto foi desenvolvido por **Thierry Uchoa de Freitas**. 

- **Email**: thierryuchoa25@hotmail.com
- **GitHub**: https://github.com/Thierry-DV
