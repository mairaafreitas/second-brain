# Hash Table

A função de hash precisa ter algumas características bem importantes:

1. A função ***hash(chave)*** deve ser determinística. Para uma determinada chave a função sempre retorna o mesmo valor 
de hash.
2. Por ser utilizada como uma função de indexação, a função de hash deve sempre retornar um valor de hash dentro dos 
limites da tabela [0,N−1], onde N é o tamanho da tabela.
3. Uniforme. Todos os índices do array devem ter aproximadamente a mesma chance de serem mapeados pela função dehash. 
Essa característica é importante para distribuir os elementos uniformemente pela tabela.
4. A função de hash deve ser executada em tempo constante O(1).

Se  duas chaves distintas forem mapeadas para a mesma posição na tabela, precisamos lidar com a colisão.