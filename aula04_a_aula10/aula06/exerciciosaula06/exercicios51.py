num = 1
soma = 0

while num != 0:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    soma += num

print(f'O valor total da soma é {soma}')