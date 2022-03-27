#Entrada: Duas matrizes quadradas de tamanho n. 
# Saída: se as duas matrizes têm um elemento em comum.
m=[[1,2,3],[4,5,6]]
m1=[[7,8,9],[10,2,11]]
for i in range(len(m)):
    for s in range(len(m[0])):
        for v in range(len(m)):
            for j in range(len(m[0])):
                if m[i][s]==m1[v][j]:
                    c=c+1
                    print('os 2 matrizes tem pelo {c} elementos em comun')