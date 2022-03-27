# Entrada: Um vetor de inteiros de tamanho n. 
# Saída: a soma de todos elementos do vetor de entrada
v=[1,2,3] 
s=0
for i in range(len(v)):
    s=v[i]+s
print(s)
#Classificação de complexidade O(n)