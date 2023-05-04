print('App Eduardo Filipe Albuquerque Pereira')

print('escreva o codigo od produto, 100 para Cachorro-quente, 101 Cachorro Quente duplo, 102 X-egg 103 X-Salada, 104 X-Bacon, 105 X-TUDO, 200 Refrigerante lata, 201 Chá Gelado')
print('Os preços são Cachorro-Quente R$ 9,00 , Cachorro-Quente Duplo R$ 11,00, X-Egg 12,00, X-Salada R$ 13,00, X-Bacon R$ 14,00, X-Tudo R$ 17,00, Refrigerante Lata R$ 5,00, Chá Gelado R$ 4,00')

conta = 0
## usando o while true pra fazer a repetição caso seja satisfeita a condição ele da o preco que no caso é o codigo
while True:
  NovoPedido = input('Deseja Fazer um Novo Pedido? digite sim ou nao: ')

  if (NovoPedido == 'nao'):
     break
  elif NovoPedido == 'sim':
    codigo = int(input('Escolha o codigo '))
    if (codigo == 100):
      preco = 9.00
    elif (codigo == 101):
      preco = 11.00
    elif (codigo == 102):
        preco = 12.00       
    elif (codigo == 102):
      preco = 12.00
    elif (codigo == 103):
        preco = 13.00
    elif(codigo == 104):
        preco = 14.00
    elif(codigo == 105):
       preco = 17.00
    elif(codigo == 200):
        preco = 5.00
    elif(codigo == 201):
        preco = 4.00
    else:
       print('voce escolheu a opcao errada')
       continue
##aqui ele faz a conta que começa em 0 la em cima e vai somando com o preco do que foi escolhido
    conta += preco 
    
  

print('a sua conta ficou {} ' .format(conta))


    
