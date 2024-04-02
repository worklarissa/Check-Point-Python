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
        return lista
    
    def insertion_sort(lista):
        n =len(lista)
        #adcionar o novo número na lista
        #comparar números
        #ordenar números
        #refazer até completar o array

    def merge_sort(lista):
        #pegar a quantidade de itens da lista
        #dividir por 2
        #dividir lista1 por 2 até ter vários arrays com 2 númeor
        #ordenar mini-arrays e rearmazenar
        #fazer o mesmo com a lista 2
        #unir listas

    def quick_sort(lista):
        