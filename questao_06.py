def f(x=100):
    from itertools import product
    nums = "123456789"
    operadores = ["", "+", "-"]
    resultados = []
    
    for ops in product(operadores, repeat=len(nums)-1):
        expr = "".join(num + op for num, op in zip(nums, ops + ("",)))
        if eval(expr) == x:
            resultados.append(expr + "==" + str(x))
    return resultados

#Utilizando os exemplos da questão
for eq in f(100):
    print(eq)
