def f(x, y):
    import numpy as np
    coef = np.polyfit(x, y, 1)
    return coef.tolist()

#Utilizando os exemplos da questão
print(f([-2, -2, -1, -1, 0, 0, 1, 1, 2, 2], [0, 0, 2, 3, 4, 4, 5, 6, 8, 8]))
