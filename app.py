##PRIMEIRO FIZ UMA FUNÇÃO QUE PERGUNTA ALTURA LARGURA E PESO CADA UMA OCM UM INPUT DEPOIS DISSE QUE A VARIAVEL VOLUME ERA GLOBAL PARA FUNCIONAR EM OUTRAS FUNÇÕES
##USEI O IF PARA CASO O VOLUME (QUE É A MULTIPLICAÇÃO DA LARGURA ALTURA E COMPRIMENTO) SEJA MAIOR MENOR OU IGUAL AOS NUMEROS CITDOS ELE DA UM CERTO PRECO
##USEI O TRY E O EXCEPT PRA CASO NAO DIGITE UM VALOR NUMERICO ELE RETORNA O ERRO DIZENDO PARA DIGITAR CORRETAMENTE E O WHILE TRUE PARA VOLTAR AO COMEÇO CASO DER ERRO
## E O BREAK PARA PARAR A FUNÇÃO CASO EXECUTE O CERTO AI VOLTA PARA O PROGRAMA PRINCIPAL
def dimensoesObjeto(pergunta, altura, largura, comprimento):
    while True:
          try:
                altura = int(input('escreva a altura (em cm)\n'))
                largura = int(input('escreva a largura (em cm)\n'))
                comprimento = int(input('escreva o comprimento (em cm)\n'))
                global volume
                volume = (altura * largura * comprimento)
                global preco
                print('O volume é {}cm³' .format(volume) )
                if (volume < 1000):
                    preco = 10
                    break
                elif (1000 <= volume < 10000):
                    preco =  20
                    break
                elif (10000 <= volume < 30000 ):
                    preco = 30
                    break        
                elif (30000 <= volume < 100000):
                    preco = 50
                    break
                elif (volume > 100000):
                    print('nao aceitamos esse valor \n digite novamente os dados')
                
          except ValueError:
            print('digite um valor numerico')  
             
    return volume 

## Aqui eu usei o try , Except para executar o codigo caso digitasse um numero nao númerico ele retornava o erro e começava de novo
##a logica é a mesma da função do volume acima
def pesoObjeto(peso):
    while True:
        try:
                global multiplicadorkg
                peso = int(input('escreva o peso (em kg)\n'))
                if (peso <= 0.1):
                    multiplicadorkg = 1
                    break
                elif (0.1 <= peso <1):
                    multiplicadorkg = 1.5
                    break
                elif(1 <= peso < 10):
                    multiplicadorkg = 2
                elif(10 <= peso <30):
                    multiplicadorkg = 3
                    break
                elif (peso >= 30):
                    print('não aceitamos esse valor')
        except ValueError:
                print('ERROR, digite um valor numerico')
    return
    
## ESSA É PRATICAMENTE A MESMA LOGICA TAMBÉM SO QUE NO LUGAR DE NUMERO É UMA SIGLA QUE É UMA STRING DEPENDENDO DA ROTA ESCOLHIDA A ATRIBUIÇÃO DO MULTIPLICADOR DA ROTA MUDA
## E BOTEI O multiplicadorRota Global também           
def rotaObjeto(rota):
     rota = input('Selecione a rota:\n RS - DE Rio de Janeiro até São Paulo\n SR De São Paulo até Rio de Janeiro \n BS - De Brasília até São Paulo\n SB - DE São Paulo até Brasília\n BR - De Brasília até Rio de Janeiro\n RB De Rio de Janeiro até Brasília\n')
     global multiplicadorRota
     if (rota == 'RS'):
        multiplicadorRota = 1
     elif(rota =='SR'):
        multiplicadorRota = 1
     elif(rota == 'BS'):
        multiplicadorRota = 1.2
     elif(rota == 'SB'):
        multiplicadorRota = 1.2
     elif(rota == 'BR'):
        multiplicadorRota = 1.5
     elif(rota == 'RB'):
        multiplicadorRota = 1.5
     print('o multiplicador da rota é {}' .format(multiplicadorRota))
     return
def total(totalapagar):
    global totalaPagar
    totalaPagar = preco * multiplicadorkg * multiplicadorRota
    print('o total a pagar é(R$) {} (dimensões: {} * peso: {} * rota: {})'.format(totalaPagar, preco, multiplicadorkg, multiplicadorRota))
    
     
print('Bem vindo ao Eduardo Filipe Albuquerque Pereira Logistica')
print('Digite a Largura em cm Altura em cm e comprimento em cm da encomenda ')
print('digite o peso em Kg')
print('digite a rota')
dimensoesObjeto('escreva a altura largura e comprimento','altura','largura','comprimento')
pesoObjeto('peso')
rotaObjeto('rota')
total('totalapagar')

  
   