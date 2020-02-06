# Relatório Projeto Final de Introdução a Matemática e Física para Videojogos I (Recurso)
## André Figueira - 21901435 [GitHub](https://github.com/affigueir)
## João Matos - 21901219 [Github](https://github.com/JMatos1221)
### [GitHub Project](https://github.com/JMatos1221/imfj1_2019_projecto)
---
Para o nosso trabalho, utilizámos o ficheiro `sample.py` para fazer a primeira parte (3D Viewer), e criámos um ficheiro `sample2.py` para realizar a segunda parte (FPS-like application). Houve também uma edição no ficheiro `mesh.py` e no ficheiro `scene.py` para a realização dos objectos e da segunda parte do trabalho (FPS-like application) respetivamente.

As contribuições de cada elemento do grupo foram:-
1. Criação do objeto usado para o 3D viewer - João Matos
2. Implementação das rotações sobre os eixos do mesmo e alteração da posição - André Figueira
3. Implementação dos vários objetos na FPS-like application - João Matos
4. Implementação da câmara, movimento e backface-culling - André Figueira
5. Bugfix e polish da câmara e movimentos - João Matos
6. Relatório - André Figueira e João Matos  

Apesar dos diferentes `commits`, todo este projeto foi realizado em conjunto, utilizando as ferramentas `Live Share` do Visual Studio Code de forma a que ambos o membros estejam atualizados sobre o progresso do trabalho, editando o mesmo ficheiro em tempo real.

## PostMortem

Neste projetos, começámos por desenhar os objectos, que não podiam ser cubos nem retângulos, de início, houve várias dúvidas , sendo que estávamos com problemas em obter as faces do objeto no sítio desejado. Acabámos assim por desenhar um prisma triangular utilizado somente código, desenhando dois triângulos  em paralelo e três retângulos ligando os pontos dos triângulos. O mesmo foi realizado para o `child object`.

![Mesh](Prints\mesh.png)

Após desenhados os objetos, o resto da parte um deste trabalho foi realizada com mais facilidade, pois o grupo já tinha um boa noção de como controlar os objetos.

Seguidamente foi realizada a parte dois, onde a implementação dos objetos foi bastante direta, usando as fórmulas realizadas anteriormente, alterando assim os valores como pedido (ex: tamanho e posição)

![FPS Meshes](Prints\part2meshes.png)

Feito isto, o grupo realizou o movimento da câmara em primeira pessoa com o as teclas WASD, e o movimento da câmara sobre o seu eixo, utilizado o rato. Tivémos algumas dificuldades de início, como por exemplo o movimento funcionar, cada tecla WASD apenas movia numa direção predefinida, ou seja, o jogador virando a câmara 90 graus ao mover-se com a tecla W, iria andar para o lado, pois o eixo não era atualizado com a posição da câmara. Sendo que após o grupo identificar o erro e como o resolver, foi feito um commit para bugfixing. 

![FPS-like Application](Prints\fpslikeapp.gif)