deposito = 0
saque = 0
saldo = 0
total_saque = 0
extrato = ''
LIMITE_DIARIO = 3

while True:
    
    menu = int(input('''  
_____________________________________                                     
               Menu                
_____________________________________
                     
    [1] Depósito               
    [2] Saque
    [3] Extrato
    [4] Sair   
                                    
Qual operação voçê deseja realizar? '''))
    print ()

    if menu == 1:
        deposito = float(input(f'''Qual valor que você deseja depósitar? R$'''))
        if deposito > 0:
            saldo += deposito
            extrato += (f'Deposito: R${deposito:.2f} \n')    
        else:
         print(f'Erro!!!Coloque um valor válido...')
        

    elif menu == 2:
        saque = float(input(f'''Qual valor que você deseja sacar? R$'''))
        if saque > saldo :
            print(f'O valor de R${saque:.2f} é maior que o seu saldo diponivel que é de R${saldo:.2f}.') 
        elif saque < 0:
            print(f'Você colocou o valor de R$ {saque:.2f}. \nPor favor NÃO coloque valores negativos!!!')
        elif  saque > 500:
            print(f'Limite máximo de saque é de R$500,00.')  
        elif total_saque >= LIMITE_DIARIO:
         print(f'Você excedeu o limite de 3 saques diários.')  

        else:
            saldo -= saque
            total_saque +=1 
            extrato += (f'Saque:{"R$": >6}{saque:.2f}\n')
            


    elif menu == 3:
        print(f'-----------Extrato-----------------')
        print(f'Não foram realizadas movimentações' if not extrato else extrato)
        print(f'Saldo:{"R$": >6}{saldo:.2f}')
        print('------------------------------------')

    elif menu == 4:
        print('Operação encerrada...Obrigado!!!\n')
    
        break

    else:
        print(f'A opção {menu} é inválida...Tente novamente!')
    
    
    
           
    
