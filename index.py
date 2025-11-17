def contar_bloques(n):
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)

print(contar_bloques(4))