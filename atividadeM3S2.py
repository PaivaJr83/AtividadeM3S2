def decorator_imprimir(func):
    def imprimir(capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print(f"Parâmetros: Capital={capital}, Taxa={taxa}, Tempo={tempo}")
        print(f"Resultado: {resultado}")
        return resultado
    return imprimir


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    return juros

   
juros = juros_simples(1000, 0.1, 5)
