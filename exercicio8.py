arq = open('dados_fun_quadratica.txt','w')

for linha in range(0,100):
    arq.write(f'\nlinha: {linha}')


arq = open('dados_fun_quadratica.txt','r')


linhas = arq.readlines()


for i in range(1,7):
    arq.write(f'\nnovo: {i}')
arq.close()

for linha in linhas:
    print(linha)

arq.close()