#Entrada: Um vetor de reais de tamanho n.
# Saída: a média doselementos do vetor de entrada
v=[1,2,3]
m=0
s=0
for i in range(len(v)):
    s=v[i]+s
m=s/len(v)
print(m)
#Classificação de complexidade O(n)