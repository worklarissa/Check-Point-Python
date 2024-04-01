# Aqui precisamos fazer as funções para busca ordenada ou chamar as funções 
# prontas testar nas listas  que estão no arquivo de dados.

class Ordenacao:
  def bubble_sort(lista):
    while #enquanto houver indices a  serem percorridos
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] ## troca de posição
    return lista

    def selection_sort(lista):
        #entender o tamanho da minha lista
        n = len(lista)
        #encontrar o menor elemento e posicionar ele no primeiro indice
        for i in range(n):
            if i < n:
                i = lista[0]
            else:
                continue
        #percorrer para achar o próximo menor elemento
        #percorrer a lista2 para encontrar o menor elemento
        # adicionar na lista1     