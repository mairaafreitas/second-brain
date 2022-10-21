# Linked List



É um tipo de estrutura linear, em que um node está conectado ao outro.

### Diferença entre um Array e uma lista encadeada:

- Array: no array é possível encontrar um objeto pelo seu índice porque os objetos estão seguidos na memória. 
  - Um array estará localizado em uma memória contínua, os seus objetos estão um do lado da outro, por isso é possível 
  usar índice, é possível mapear a memória para um local específico. Para adicionar ou remover um elemento, é necessário
  mover todos os elementos da lista para uma nova lista.


- Linked List: os objetos estão dispersos na memória e o próximo objeto da lista é encontrado a partir do apontamento 
para o nó posterior. 
  - Como estão ligados ao nó seguinte, os dados não são perdidos. Para adicionar ou remover um elemento, 
  como não existe a obrigatoriedade dos elementos estarem em posições contíguas da memória, precisa realizar alterações 
  apenas nas referências dos nós, sendo um novo nó rapidamente inserido ou removido.

Esta estrutura é mais adequada para listas com centenas ou milhares de nós, onde uma inserção ou remoção em uma lista
contígua representará uma perda notável no desempenho do processamento.

**Vantagens: Rápido para inserir e remover (no início e final da lista) O(1)**
1. A inserção e remoção de elementos podem ser feitas sem deslocar os itens seguintes da lista;
2. Não há necessidade de previsão do número de elementos da lista, o espaço necessário é alocado em tempo de execução;
3. Facilita o gerenciamento de várias listas (fusão, divisão,...).

**Desvantagens: Devagar para conseguir pegar um elemento O(n)**
1. Acesso indireto aos elementos;
2. Tempo variável para acessar os elementos (depende da posição do elemento);
3. Gasto de memória maior pela necessidade de um novo campo para o ponteiro.

Uma linked list pode ser representada guardando o seu primeiro nó (head) e último nó (tail) em um ponteiro. Cada um 
desses nós aponta para o próximo nó, sendo o último não apontando para nada.


`Célula 1 ---> Célula 2 ---> Célula 3 ---> Célula 4 ---> Célula 5 ---> (Nulo)`

> Para manipularmos: inserir ou remover dados temos que sempre lembrar em ter um ponteiro que aponte para o 1º 
> elemento e outro que aponte para o fim. Isto porque se queremos inserir ou apagar dados que estão no inicio ou no fim 
> da lista então a operação é rapidamente executada, caso seja um nó que esteja no meio da lista, terá que haver uma 
> procura até encontrar a posição desejada.