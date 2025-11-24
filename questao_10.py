def f(nums):
    return len(nums) != len(set(nums))

#Utilizando os exemplos da questão
print(f([1,2,3,3]))
print(f([1,2,3,4]))
