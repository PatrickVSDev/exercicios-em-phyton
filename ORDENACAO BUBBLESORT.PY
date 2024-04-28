import random
menu = 0
vetor = []
   
def ale():
     vetor = [random.randint(1,1000) for i in range(10)]
     return vetor

def bubblesort(vetor):
     n = len(vetor)
     for i in range(n - 1):
          for j in range(0, n - i -1):
               if vetor [j] < vetor [j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
     return vetor
alert = ale()
print(alert)

alert = bubblesort(alert)
print(alert)

def ale2():
     num_ale = random.randint(1,1000)
     return num_ale

alea2 = ale2()
alert[1] = alea2
alert = bubblesort(alert)
print (alert)