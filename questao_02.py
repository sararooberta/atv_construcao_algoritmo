def f(nums):
    n = len(nums)
    soma_esperada = n * (n + 1) // 2
    soma_real = sum(nums)
    
    vistos = set()
    for num in nums:
        if num in vistos:
            duplicado = num
            break
        vistos.add(num)
    
    faltante = soma_esperada - (soma_real - duplicado)
    
    return (duplicado, faltante)

print(f([1, 2, 2, 4]))
print(f([1, 1]))
