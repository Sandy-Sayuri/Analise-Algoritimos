#Entrada: dois vetores de inteiros, cada um de tamanho n. 
# Saída:um vetor cuja posição i guarda a soma dos elementos da posição i de cada vetor de entrada.
v=[1,2,3]
v1=[]
s=0
for i in range(len(v)):
    s=v[i]+s
    v1.append(s)
print(v1)
#Classificação de complexidade O(n)