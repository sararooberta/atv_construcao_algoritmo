def f(lista, busca):
    for numero, nome in lista:
        if numero == busca:
            return nome
    return None

#Utilizando os exemplos da questão
print(f([(18, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (3, 'Daniela')], 15))  

print(f([(187, 'Isabela'), (13, 'João'), (199, 'Karen'), (201, 'Leonardo')], 199))  
