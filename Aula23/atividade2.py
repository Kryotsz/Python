lin=int(input('Número de linhas: '))
col=int(input('Número de colunas: '))

if lin!=col:
    print('Matriz não é triangular')
else:
    m=[]
    triangular=True
    for i in range(lin):
        elem=[]
        for j in range(col):
            elem.append(int(input(f'M[{i+1}][{j+1}]= ')))
        m.append(elem)
print('Matriz M:')
for i in range(lin):
    for j in range(col):
        print(m[i][j], end=' ')
    print()
    for i in range(lin):
        for j in range(col):
            if i<j:
                if m[i][j]!=0:
                    triangular=False
if triangular==True:
    print('M é matriz triangular inferior')
else:
    print('M não é uma matriz triangular inferior')
