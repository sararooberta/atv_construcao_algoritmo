def f(x, y):
    resultado = []
    for a, b in zip(x, y):
        resultado.extend([a, b])
    return resultado

#Utilizando os exemplos da questão
print(f(["a", "b", "c"], [1, 2, 3]))
