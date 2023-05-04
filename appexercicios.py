##Tirando de 2 numeros flutuantes no python, simulando uma nota de escola
x = float(input('Digite Sua primeira nota '))
y = float(input('Digite sua segunda nota '))
media = ('O seu Resultado final foi {}') .format ((x+y)/2)
print(media)
##Quantas vezes 73 cabe em 403
print(403//73)

##A sobra quando 403 é dividido por 73
403%73

##2 elevado a decima potencia
2**10

##O valor absoluto da difenrença entre 54 e 57
print(abs(57-54))

#o menor valor entre 34,29 e 31
print(min(34,29,31))

# executa as seguintes atribuições s1= 'ant' , s2='bat, s3='cod' agora, utilizando os operadores + e* , crie as saídas a seguir a)'ant bat cod' b)'ant ant ant ant ant ant ant ant ant ant' c)'ant bat bat cod cod cod' d)'ant bat ant bat ant bat ant bat ant bat 'ant bat'ant bat' e)'batbatcod' batbatcad batbattcod batbatcod batbatcod'
s1 = 'ant' 
s2 = 'bat'
s3= 'cod'
print(s1+' '+s2+' '+s3)
print(10*(s1+ ' '))
print(s1+' '+s2*2+' '+s3*3)
print(7*(s1+' '+s2 +' '))
print(5*(s2*2+s3+' '))

#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele, calcule e exiba o valor do desconto e o preçõ final do protudo
x=float(input('escreva o valor do produto '))
y=float(input('escrava o desconto dele '))
desconto = + ((x*y)/100)
valorfinal = x-desconto
print('o desconto foi de {} '.format(desconto))
print('o valor final foi de {}'.format(valorfinal))


#Escreva um programa que pergunte a quantidade de km percorridos por carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. calcule o preço a pagar, sabendo que o carro custa 60 por dia e 0,15 por km rodado
x = int(input('descreva a quantidade de km feito '))
y = int(input('descreva a quantidade de dias rodados '))
preco = 60 * y + 0.15 * x
print('o km rodado foi {}. os dias rodados foram {}' .format(x,y) )
print('o valor a ser pago é {}'.format(preco))
#Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variavel agora contendo a medade da string digitada. imprima na tela somente os dois ultimos carcteres da segunda varievel do tipo string

frase1 =  input('digite uma frase:')
tam = len(frase1)
frase2 = frase1[:int(tam/2)]
print(frase2[-3:])

#Faça uma escolha de 3 produtos 1 para maça , 2 para laranja , 3 para banana o algoritmo de calcular o preço total do produto escolhido e mostrar na tela considere que a maçã custa 2.30 uma laranja 3.60 e a banana 1.85
print('escolha oque deseja comprar')
print('1 - maçã')
print('2 - laranja')
print('3 - banana')
produto = int(input('qual a sua escolha'))
qtd = int(input('escolha a quantidade'))
if (produto == 1):
  qtdmaca = qtd * 2.30
  print('voce escolheu maçã o total a pagar é,  {}' .format(qtdmaca))
else: 
  if (produto == 2):
    qtdlaranja = qtd * 3.60
    print('voce escolheu laranja o total a pagar é, {}' .format(qtdlaranja))
  else:
    if (produto == 3):
      qtdbanana = qtd * 1.85
      print('voce escolheu a banana o total a pagar é, {}' .format(qtdbanana))
    else:
      print('você não escolheu nenhuma fruta')

#Mesmo exercico a cima com o elif
print('escolha oque deseja comprar')
print('1 - maçã')
print('2 - laranja')
print('3 - banana')
produto = int(input('qual a sua escolha'))
qtd = int(input('escolha a quantidade'))
if (produto == 1):
  qtdmaca = qtd * 2.30
  print('voce escolheu maçã o total a pagar é,  {}' .format(qtdmaca))
elif (produto == 2):
    qtdlaranja = qtd * 3.60
    print('voce escolheu laranja o total a pagar é, {}' .format(qtdlaranja))
elif (produto == 3):
      qtdbanana = qtd * 1.85
      print('voce escolheu a banana o total a pagar é, {}' .format(qtdbanana))
else:
  print('você não escolheu nenhuma fruta')

#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usúario qual operação ele deseja realizar: adiçâo (+) subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada
print('CALCULADORA')
print('primeiro escolha os 2 numeros a ser feito')
print('depois escolha o numero da operação desejada as opções 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão')
x = float(input('escreva o primeiro valor '))
y = float(input('escreva o segundo valor '))
b = int(input('escreva a sua orperação '))
#primeiro fiz uma variavel com input para digitar o valor e a operação desejada depois usei o if para saber qual operação se for a escolhida passei as instruções do que fazer, o professor usou o input do operador com sinais como +
#e botou no if com um '+' ou '-' entre aspas se não ele não reconhece
if (b == 1):
  adicao = x + y
  print(adicao)
elif (b == 2):
  subtracao = x - y
  print(subtracao)
elif (b == 3):
  multiplicacao = x * y
  print(multiplicacao)
elif (b == 4):
  divisao = x / y
  print(divisao)

##Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:R para residência, I para indústria e C para comércios!
#Seguintes preços
#Residencial até 500 kWh preço 0,40 Residencial acima de 500 preço 0,65
#Comercial até 1000 preço 0,55 Comercial Acima de 1000 preço 0,60
#Industrial até 5000 preço 0,55 Industrial Acima de 5000 preço 0,60
print('primeiro escreva a quantidade de kWh')
print('depois escreva o tipo de intalação R para residencia, I para industria e C para comercio ')

x = float(input('escreva a quantidade de kWh '))
y = input('escreva o tipo de instalação ')

print(x)

if(y == 'R' and x <=500):
  Rmenos = x * 0.40
  print('o valor da energia da residencia é {}'.format(Rmenos))
elif(y == 'R' and x > 500):
  Rmais = x * 0.65
  print('o valor da energia residencia é {}'.format(Rmais))
elif(y == 'C' and x <= 1000):
  Cmenos = x * 0.55
  print('o valor a pagar da energia do comercio é {} '.format(Cmenos))
elif(y == 'C' and x > 1000):
  Cmais = x * 0,60
  print('o valor a pagar da energia do comercio é '.format(Cmais))
elif(y == 'I' and x <= 5000):
  Imenos = x * 0.55
  print('o valor a pagar da energia da industria é {}'.format(Imenos))
elif(y == 'I' and x > 5000):
  Imais = x * 0.60
  print('o valor a pagar da energia da industria é {} '.format(Imais))
else:
  print('você não escolheu a instalação certa')

#Realize a sequência de print com for e while a)inteiros de 3 a 12, com 12 incluso b) intereiros de 0 até 9, excluindo 0, com passo de 2
## a)
x = 3
while(x<=13):
    print(x)
    x+=1

for y in range (3,13,1):
    print(y)
           
## b)
x = 0
while(x<9):
  print(x)
  x+=2

for y in range(0,9,2):
  print(y)
 
#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usúario qual operação ele deseja realizar: adiçâo (+) subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada

#+Repita até que a operação de saída seja escolhida
#Enquanto a operacao nao for n ele excuta o while, digitou N ele sai da operação
print('CALCULADORA')

op = input('digite o operador + para adição - para subtração / para divisão e  * para multiplicação caso queria parar digite N ')

if op == '+' or op == '-' or op == '*' or op == '/':
  x = int(input('digite o primeiro numero '))
  y = int(input('digite o segundo numero '))

while (op != 'N'):
  if (op == '+'):
    resp = x +y
    print('voce escolheu soma esse é o resultado {} ' .format(resp))
  elif (op == '-'):
    resp = x - y
    print('voce escolheu subtração esse é o resultado {} ' .format(resp))
  elif (op == '*'):
    resp = x * y
    print('voce escolheu multiplicação esse é o resultado {} ' .format(resp))
  elif (op == '/'):
    resp = x / y
    print('voce escolheu divisão o resultado é {} ' . format(resp))
  else:
    ('Você digitou as opções incorretas')
  
print('operação encerrada')

#O mesmo exericio anterior usando o break e o continue
##diferente do de cima botamos um break e no começo botamos um while true e entre as operaçoes usamos o 
##continue
print('CALCULADORA')


while True:
  op = input('digite o operador + para adição - para subtração / para divisão e  * para multiplicação caso queria parar digite n')
  if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('digite o primeiro numero '))
    y = int(input('digite o segundo numero '))
    x = int(input('digite o primeiro numero '))
    y = int(input('digite o segundo numero '))

    if (op == '+'):
      resp = x +y
      print('voce escolheu soma esse é o resultado {} ' .format(resp))
      continue
    elif (op == '-'):
      resp = x - y
      print('voce escolheu subtração esse é o resultado {} ' .format(resp))
      continue
    elif (op == '*'):
      resp = x * y
      print('voce escolheu multiplicação esse é o resultado {} ' .format(resp))
      continue
    elif (op == '/'):
      resp = x / y
      print('voce escolheu divisão o resultado é {} ' . format(resp))
      continue
    elif (op == 'n'):
        break
     
    else:
      ('Você digitou as opções incorretas')
### usei o if pra caso o valor seja menor ou igual a 100 ele usa o cd que é igual ao valor // 100 que é o resultado inteiro

#Escreva um algoritmo que leia um valor e que imprima a quantidade de células necessarias para pagar esse mesmo valor. Para simplificar, vamos trabalhar apenas com valores inteiros com cedular de R 100,R  50, R 20,R  10, R 5eR  1



## e ele pegar o valor menos o resultado inteiro vzes o numero digitado e isso se repete nos outros
## mas pra complementar o exercicio usa-se ele mais o if not valor e o break para parar a conta se todas as notas foram contadas por expl
## 5 notas de 100 fecha a conta, se sim então para
valor = int(input('escreva o valor em Real '))

while True:
  if valor >= 100:
    cd100 = valor // 100
    valor = valor - cd100*100
    print('a quantidade de cedular de 100 foram {} ' .format(cd100))
    if not valor:
      break
  if valor >= 50:
    cd50 = valor // 50
    valor = valor - cd50 *50
    print('a quantidade de cedular de 50 foram {} ' .format(cd50))
    if not valor:
      break 
  if valor >= 20:
    cd20 = valor // 20
    valor = valor - cd20 *20 
    print('a quantidade de cedular de 20 foram {} ' .format(cd20))
    if not valor:
      break 
  if valor >= 10:
    cd10 = valor // 10
    valor = valor - cd10 *10
    print('a quantidade de cedular de 10 foram {} ' .format(cd10)) 
    if not valor:
      break 
  if valor >= 1:
    cd1 = valor // 1
    valor = valor - cd1 * 1
    print('a quantidade de cedular de 1 foram {} ' .format(cd1)) 
    if not valor:
      break 


##Um cinema Cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito, se tiver entre 3 e 12 anos, o ingresso custará 15 reais, se tiver mais de 12ano custará 30

total = 0
dinheiro = 0
while True:
  idade = (input('digite sua idade '))
  if idade == 'sair':
    break
  idade = int(idade)
  total += 1
  if idade < 3:
    ingresso = 0
  else:
    if idade > 12:
      ingresso = 30
    else:
      igresso = 15
  dinheiro +=ingresso

media = dinheiro /total  
print('total de pessoas: {} ' .format(total))
print('total arrecadado: {} ' .format(dinheiro))
print('média arrecadada: {} '.format(media))
                               




     




