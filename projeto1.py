game =input ('Quer jogar um jogo de adivinhação? (s/n): ') 
if game == 's':
    print('Seja bem vinda ao Jogo de Adivinhacao!')
    print('Quanto mais se tira, maior fica. O que é?')
    resposta_1 = input('Digite sua resposta: ')
    if resposta_1 in ('buraco', 'um buraco', 'o buraco', 'Buraco', 'Um buraco', 'O buraco', 'buraco.','um buraco.','o buraco.','Buraco.','Um buraco.','O buraco.'):
        print('Boa meu parceiro voce acertou!')
    else:
        print('Ai nao meu mano\n A resposta correta é "buraco".')
elif game == 'n':
    print('Que pena, Ate a proxima!')



game_2 = input ('Quer jogar de novo? (s/n): ')
if game_2 == 's':
        print('Bora pra mais um rodada entao!')
        print('O que é, o que é? Mesmo que seja seu, os outros usam mais que você.')
        resposta_2 = input('Digite sua resposta: ')
        if resposta_2 in ('seu nome', 'nome', 'Seu nome', 'Nome', 'o nome', 'O nome', 'meu nome', 'Meu nome', 'o meu nome', 'O meu nome'):
            print('Boa meu parceiro voce acertou!')
        else:
            print('Ai nao meu mano \n A resposta correta é "Nome".')
elif game_2 == 'n':
        print('Obrigado por jogar, Ate a proxima!')


game_3 = input ('Eae topa mais uma rodada? (s/n): ')
if game_3 == 's':
        print('Bora pra mais um rodada entao!')
        print('O que é, o que é? Cai em pé e corre deitado.')
        resposta_3 = input('Digite sua resposta: ')
        if resposta_3 in ('chuva', 'Chuva', 'a chuva', 'A chuva', 'uma chuva', 'Uma chuva', 'chuva','Chuva','a chuva','A chuva','uma chuva','Uma chuva','gota de chuva','Gota de chuva','gota de chuva.','Gota de chuva.','gota'):
            print('Boa meu parceiro voce acertou!')
        else:
            print('Ai nao meu mano \n A resposta correta é "Chuva".')
elif game_3 == 'n':
        print('Obrigado por jogar, Ate a proxima!')



print('Pra finalizar com chave de ouro, mais uma pergunta estremamente dificil, quer prosseguir (ou nao) depende de voce!: ')
game_4 = input ('Quer respoder? (s/n): ')
if game_4 == 's':
     print('Quem é melhor: Palmeiras(1) ou Corinthians(2)?')
     print('Escolha sabiamente, pois sua escolha definirá o rumo do universo!')
     resposta_4 = input('Qual é melhor: ')
     if resposta_4 == '1':
         print('Parabens, voce escolheu sabiamente! O universo agradece sua decisao!')
     else:
         print('Infelizmente voce escolheu o lado errado da forca. O universo esta em colapso por sua causa!')
elif game_4 == 'n':
     print('Voce escolheu sabiamente, o universo agradece sua decisao!')
print('Obrigado por jogar, Ate a proxima!')


