def f(lista):
    return sum(1 for num in lista if num % 2 == 0)

#Utilizando os exemplos da questão
print(f([2, 4, 7, 8, 10, 95]))
