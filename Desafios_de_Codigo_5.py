'''Desafio
Você faz parte de uma equipe que está desenvolvendo modelos de Machine Learning para identificar a probabilidade de inadimplência em empréstimos concedidos por uma instituição financeira. Após treinar os modelos, sua tarefa é avaliar seu desempenho usando algumas métricas de avaliação. Nesse contexto, o desafio é criar um algoritmo que receba n matrizes de confusão e retorne o índice, precisão e acurácia da matriz que apresenta o melhor desempenho com base no cálculo dessas métricas. Lembrando que:

• Acurácia é calculada pela fórmula: (VP + VN) / (VP + FP + FN + VN)
• Precisão é calculada pela fórmula: VP / (VP + FP)

Onde:

• VP (Verdadeiro Positivo): Casos em que o modelo previu corretamente a classe positiva.
• FP (Falso Positivo ou Erro Tipo I): Casos em que o modelo previu incorretamente a classe positiva.
• FN (Falso Negativo ou Erro Tipo II): Casos em que o modelo previu incorretamente a classe negativa.
• VN (Verdadeiro Negativo): Casos em que o modelo previu corretamente a classe negativa.

Entrada:
A entrada consiste em uma string composta por: n, representando o número de matrizes de confusão, seguido dos valores que compõem as n matrizes.

Cada matriz consiste em quatro valores, onde os dois primeiros representam a primeira linha da matriz, composta por verdadeiros positivos (VP) e falsos positivos (FP); os dois últimos valores representam a segunda linha, que é composta por falsos negativos (FN) e verdadeiros negativos (VN). As duas linhas e os valores que as compõem estão separados por vírgulas.

Saída:
O resultado esperado inclui o valor do índice, acurácia e precisão (arredondada para duas casas decimais) da matriz com melhor desempenho com base no cálculo dessas métricas.'''

n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))

# TODO: Create a function to calculate accuracy and precision metrics
def calculate_metrics(VP, FP, FN, VN):
  accuracy = (VP + VN) / (VP + FP + FN + VN) if (VP + FP + FN + VN) != 0 else 0
  precision = VP / (VP + FP) if (VP + FP) != 0 else 0 
  
  return accuracy, precision 
# TODO: Create a function to find the matrix index with the best combined accuracy and precision

def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        
        matrix = [int(x) for x in matrix]
        
        VP = matrix[0]
        FP = matrix[1]
        FN = matrix[2]
        VN = matrix[3]
        
        accuracy, precision = calculate_metrics(VP, FP, FN, VN)
        
        if (accuracy + precision) > (best_accuracy + best_precision):
          best_index = index
          best_accuracy = accuracy
          best_precision = precision
       
       
    return best_index, best_accuracy, best_precision
    
def format_metric(value):
    
    formatted_value = f"{value:.2f}"
  
    if formatted_value.endswith('00'):
      formatted_value = formatted_value[:-1]
    elif formatted_value.endswith('0'):
      formatted_value = formatted_value[:-1]
    return formatted_value
  
best_index, best_accuracy, best_precision = best_performance(matrices)
index = best_index + 1

print(f'Índice: {index}')
print(f'Acurácia: {format_metric(best_accuracy)}')
print(f'Precisão: {format_metric(best_precision)}')

# Print the results