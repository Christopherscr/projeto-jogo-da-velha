# Implementação do jogo da velha para dois jogadores em Python.

''' Vamos criar o tabuleiro usando um dicionário
    no qual as chaves serão as posições (ou seja, superior-esquerdo, meio-direita, etc.)
    e inicialmente seus valores serão espaços em branco e, depois de cada movimento,
    iremos alterar o valor de acordo com a escolha do jogador. '''

tabuleiro = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

chaves_tabuleiro = []

for chave in tabuleiro:
    chaves_tabuleiro.append(chave)

''' Precisamos imprimir o tabuleiro atualizado após cada movimento no jogo e,
    portanto, criaremos uma função na qual definiremos a função printTabuleiro
    para que possamos facilmente imprimir o tabuleiro sempre chamando esta função. '''

def printTabuleiro(tabuleiro):
    print(tabuleiro['7'] + '|' + tabuleiro['8'] + '|' + tabuleiro['9'])
    print('-+-+-')
    print(tabuleiro['4'] + '|' + tabuleiro['5'] + '|' + tabuleiro['6'])
    print('-+-+-')
    print(tabuleiro['1'] + '|' + tabuleiro['2'] + '|' + tabuleiro['3'])

# Agora escreveremos a função principal que possui todas as funcionalidades do jogo.
def jogo():

    turno = 'X'
    contagem = 0

    for i in range(10):
        printTabuleiro(tabuleiro)
        print("É a sua vez, " + turno + ". Mova-se para qual posição?")

        movimento = input()

        if tabuleiro[movimento] == ' ':
            tabuleiro[movimento] = turno
            contagem += 1
        else:
            print("Essa posição já está preenchida.\nMova-se para qual posição?")
            continue

        # Agora iremos verificar se o jogador X ou O ganhou, após cada movimento após 5 movimentos. 
        if contagem >= 5:
            if tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] != ' ': # na parte superior
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")                
                break
            elif tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] != ' ': # no meio
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break
            elif tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] != ' ': # na parte inferior
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break
            elif tabuleiro['1'] == tabuleiro['4'] == tabuleiro['7'] != ' ': # na esquerda
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break
            elif tabuleiro['2'] == tabuleiro['5'] == tabuleiro['8'] != ' ': # no meio
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break
            elif tabuleiro['3'] == tabuleiro['6'] == tabuleiro['9'] != ' ': # na direita
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break 
            elif tabuleiro['7'] == tabuleiro['5'] == tabuleiro['3'] != ' ': # diagonal
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break
            elif tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] != ' ': # diagonal
                printTabuleiro(tabuleiro)
                print("\nFim de Jogo.\n")                
                print(" **** " + turno + " venceu. ****")
                break

        # Se nem X nem O ganharem e o tabuleiro estiver cheio, declararemos o resultado como 'empate'.
        if contagem == 9:
            print("\nFim de Jogo.\n")                
            print("É um Empate!!")

        # Agora temos que alternar o jogador após cada movimento.
        if turno == 'X':
            turno = 'O'
        else:
            turno = 'X'        
    
    # Agora vamos perguntar se o jogador quer reiniciar o jogo ou não.
    reiniciar = input("Você deseja jogar novamente? (s/n)")
    if reiniciar == "s" or reiniciar == "S":  
        for chave in chaves_tabuleiro:
            tabuleiro[chave] = " "

        jogo()

if __name__ == "__main__":
    jogo()
