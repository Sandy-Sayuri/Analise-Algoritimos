# Entrada: Duas matrizes quadradas de tamanho n. 
# Saída: a soma das duas matrizes.
m1=[[1,2],[3,4]]
m2=[[4,5],[6,7]]
res=[]
m=0
for l in range(len(m1)):
    for c in range(len(m1[l])):
        m=m1[l][c]+m2[l][c]
        res.append(m)
print(res)
#Classificação de complexidade O(n)^2