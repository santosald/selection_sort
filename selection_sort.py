import random

a = []

# Gera um vetor com 20 elementos entre 0 e 999.
def gera_vetor(a):

    for _ in range(20):
        a.append(random.randrange(0, 999))


def selection_sort(a):

    # Percorre o vetor de 0 ao tamanho do vetor, define x como a posição atual.
    for i in range(len(a)):
        x = i

        # Percorre a "metade desordenada" do vetor, comparando o elemento da posição 
        # atual com os demais e colocando em x a posição do valor menor encontrado.
        for j in range(i+1, len(a)):
            if a[x] > a[j]:
                x = j

        # Troca o elemento da posição atual (iteração) com o menor elemento da "metade desordenada".
        a[i], a[x] = a[x], a[i]

    print(f'Vetor ordenado: {a}')


if __name__ == "__main__":

    gera_vetor(a)

    print(f'Vetor original: {a}')

    selection_sort(a)
