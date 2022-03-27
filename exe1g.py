#Entrada: Um vetor de inteiros de tamanho n. 
# Saída: o vetor de entrada invertido.
v=[1,2,3]
v1=[]
for i in range(len(v)-1,-1,-1):
    v1.append(v[i])
print(v1)    
#Classificação de complexidade O(n)