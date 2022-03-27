#Entrada: Duas matrizes quadradas de tamanho n. 
#Saída: a multiplicação das duas matrizes.
m1=[[1,2],[3,4]]
m2=[[4,5],[6,7]]
res=[]
m=0
ma=0
cont=0
s=0
s1=0
for l in range(len(m1)):
    s=0
    s1=0
    for c in range(len(m1[l])):
        m=m1[l][c]*m2[c][l]
        s=s+m
        print(s)
        cont=cont+1
        if cont==1 or cont==2:
            ma=m1[l][c]*m2[c][1] 
            s1=s1+ma
        if cont==3 or cont==4: 
            ma=m1[l][c]*m2[c][0]
            s1=s1+ma 
    res.append(s)
    res.append(s1)
print(res)
#Classificação de complexidade O(n)^2