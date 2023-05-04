cadastro = []
codigo = 0



def cadastrarpeca(codigo):
      print('Você entrou em cadastrar produto')
      print('Códico do produto: {} ' . format(codigo))
      peca = input('escreva o nome da peça \n')
      fabricante = input('escreva o nome do fabricante \n')
      valor = int(input('escreva o valor \n'))
      dicionariopeca ={'codigo' : codigo, 'peca' : peca ,'fabricante': fabricante, 'valor' : valor}
      cadastro.append(dicionariopeca.copy())

def consultarpeca():
    while True:
        escolhaconsultar = input('escolha a opção desejada para consultar:\n 1 - Consultar todas as peças\n 2 - consultar por codigo da peça \n 3 - consultar por fabricante \n 4 - para retornar ao menu inicial\n')
        if escolhaconsultar == '1':
            print('a escolha foi consultar todos so produtos')
            for produto in cadastro:
                for chave, valor in produto.items():
                    print('{} : {} '. format(chave, valor))
        elif escolhaconsultar == '2':
            codigodoproduto = int(input('insira o codigo '))
            for produto in cadastro:
                if produto['codigo'] == codigodoproduto:
                    for chave, valor in produto.items():
                        print('{} : {}' .format(chave, valor))


         

        elif escolhaconsultar == '3':
            print(' voce esta escolhendo por fabricante')
            codigofabricante = input('insira o nome do fabricante ')
            for produto in cadastro:
                if produto['fabricante'] == codigofabricante:
                    for chave, valor in produto.items():
                        print('{} : {}' .format(chave, valor))

            
        elif escolhaconsultar == '4':
            return
        else: 
            print('opão invalida')
            continue
def removerpeca():
    print('Voce escolheu a opção de remover peça ')   
    opcaoremover = input('Escolha a opção:\n 1 - para remover a peça \n 2 - para retonar ao menu inicial')
    if opcaoremover == '1':
        removerpeca = int(input('insira o codigo da peca \n'))
        for produto in cadastro:
            if produto['codigo'] == removerpeca:
                cadastro.remove(produto)
                print('A peça foi Removida')
    elif opcaoremover == '2':
        return
    else:
        print('opcao invalida')
        
    
    
    
                
        

                    
        


       
        
#PROGRAMA PRINCIPAL
print('bem vindo a o Estoque de peças da bicicletaria Eduardo Filipe Albuquerque Pereira')
while True:
    escolha_opcao = input('escolha a opção desejada:\n'+ '1 - cadastrar peça\n' + '2 - consultar peça\n' + '3 - Remover peça\n' + '4 - Para Sair \n')
    if escolha_opcao == '1':
        codigo = codigo + 1
        cadastrarpeca(codigo)
    elif escolha_opcao == '2':
        consultarpeca()
    elif escolha_opcao == '3':
        removerpeca()
    elif escolha_opcao == '4':
        break
    else:
        print('voce escolheu uma opção invalida')
        continue
print(cadastro)
print(codigo)
