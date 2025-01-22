def tempo_de_execucao(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.2f}s")
        return resultado
    return wrapper

@tempo_de_execucao
def soma(a, b):
    return a + b

print(soma(5, 3))
