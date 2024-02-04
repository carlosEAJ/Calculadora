def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calculadora():
    escolhadas_op = escolha_ope()
    
    if escolhadas_op == "0":
        print("Saindo...")
    
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    
    if escolhadas_op == "1":
        print(soma(a, b))
    elif escolhadas_op == "2":
        print(sub(a, b))
    elif escolhadas_op == "3":
        print(div(a, b))
    elif escolhadas_op == "4":
        print(mult(a, b))
    else:
        print("Opção inválida, por favor escolha uma das operações aritméticas.")

def escolha_ope():
    escolhadas_ops = input(" Escolha uma das opções: 1 = Soma, 2 = subtração,  3 = divisão e 4 = multiplicação e 0 = Sair: ")
    return escolhadas_ops

def main():
    while True:
        calculadora()
        
main()