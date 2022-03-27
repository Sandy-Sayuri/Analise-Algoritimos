#Entrada: Um vetor de inteiros de tamanho n. 
# Saída: a mediana dos valores do vetor.
v=[1,2,3,4,5,6,7,8,9] 

if len(v)%2==0:
    s=v[len(v)//2]+v[(len(v)//2)-1]
    m=s/2
    print(m)
else:
    print(v[(len(v)//2)])
#Classificação de complexidade O(1)