import random

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        key = vetor[i]
        j = i - 1
        while j >= 0 and key < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key

random_numbers = [random.randint(0, 1000) for _ in range(10)]

print("Vetor não ordenado:", random_numbers)
insertion_sort(random_numbers)
print("Vetor ordenado:", random_numbers)
