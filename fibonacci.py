
num = int(input("Digite um número inteiro: "))

a = 0
b = 1

pertence = False


while b <= num:
    if b == num:
        pertence = True
        break
    a, b = b, a + b

if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.") 