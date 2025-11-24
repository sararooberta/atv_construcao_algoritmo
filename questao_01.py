def f(nums, alvo):
    vistos = {}
    
    for i, num in enumerate(nums):
        complemento = alvo - num
        if complemento in vistos:
            return (vistos[complemento], i)
        vistos[num] = i

print(f([2, 7, 11, 15], 9))
print(f([3, 2, 4], 6))
print(f([3, 3], 6))
