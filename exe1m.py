# Entrada: dois vetores de inteiros, cada um de tamanho n. 
# Saída:se os dois vetores têm um elemento em comum.
v=[1,2,3,4]
v1=[4,5,6,7]
c=0
for i in range(len(v)):
    for j in range(len(v1)):
        if v[i]==v1[j]:
            c=c+1
            print(f' os 2 vetores tem pelo {c} elementos em comun') 
        
