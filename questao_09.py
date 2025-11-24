def f(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

#Utilizando os exemplos da questão
print(f([10,1,5,6,7,1]))
print(f([10,8,7,5,2]))

