

Sistema de Batalha de RPG em Python

Este é um sistema de batalha de RPG simples em Python, onde o jogador luta contra NPCs (Personagens Não-Jogáveis) em uma batalha baseada em turnos.


Funcionalidades

Criação de NPCs: NPCs são criados com base no nível, e cada NPC tem atributos como nome, nível, dano e pontos de vida.
Batalha: O jogador e o NPC atacam-se mutuamente até que um deles fique sem pontos de vida.
Experiência e Níveis: O jogador ganha experiência ao derrotar um NPC. Quando a experiência ultrapassa um certo limite, o jogador sobe de nível.
Implementação
O jogador e os NPCs são representados como dicionários em Python.
A batalha ocorre em um loop enquanto ambos o jogador e o NPC têm pontos de vida.
Após cada batalha, o jogador ganha experiência, e seu nível e atributos podem ser atualizados.
A lógica de batalha é baseada em ataques de ambos os lados, com dano causado dependendo dos atributos do jogador e do NPC.


Como Usar

Certifique-se de ter Python instalado em seu sistema.
Instale a biblioteca Colorama se ainda não tiver instalado:

  pip install colorama


Execute o script Python:

  python nome_do_arquivo.py

  

Siga as instruções exibidas no console para interagir com o sistema de batalha.
Observações
Este é um projeto simples criado para fins educacionais e de aprendizado de Python.
Sinta-se à vontade para modificar e expandir o código de acordo com suas necessidades e interesses.
