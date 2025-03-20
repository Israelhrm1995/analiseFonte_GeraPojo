import lizard

# Caminho para o arquivo Java que vamos analisar.
file_path = "C:/gitRepositories/sankhyaw/MGECom-Model/src/br/com/sankhya/mgecomercial/model/helper/PDVItensHelper.java"

# Analisa o código
analysis = lizard.analyze_file(file_path)

print(f"Arquivo: {file_path}")
print("=================================")

# Ordena as funções pela complexidade ciclomática (da mais alta para a mais baixa)
sorted_functions = sorted(analysis.function_list, key=lambda x: x.cyclomatic_complexity, reverse=True)

# Exibe a complexidade de cada função
for function in sorted_functions:
    print(f"Função: {function.name}")
    print(f"  Complexidade Ciclomática: {function.cyclomatic_complexity}")
    print(f"  Linhas de Código: {function.length}")
    print("---------------------------------")

if __name__ == "__main__":
    print("Análise de complexidade ciclomática concluída.")
