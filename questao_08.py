def f(nums):
    n = len(nums)
    resultado = [1] * n
    
    prefixo = 1
    for i in range(n):
        resultado[i] = prefixo
        prefixo *= nums[i]
    
    sufixo = 1
    for i in range(n-1, -1, -1):
        resultado[i] *= sufixo
        sufixo *= nums[i]
    
    return resultado

#Utilizando os exemplos da questão
print(f([1,2,4,6]))
print(f([-1,0,1,2,3]))

