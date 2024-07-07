'''Descrição
Imagine que você foi designado a criar um algoritmo para analisar o sentimento de um comentário fornecido pelo usuário, simulando analises de sentimentos, um assunto muito comentado dentro do Machine Learning. O programa solicitará ao usuário que insira um comentário, e em seguida, dividirá esse comentário em palavras individuais.

Após isso, ele contará o número de palavras positivas, negativas e neutras dentro do comentário, baseando-se em uma lista pré-definida de palavras-chave. As palavras consideradas positivas incluem "bom", "ótimo", "excelente", "maravilhoso", "gostei" e "incrível" enquanto as palavras negativas incluem "ruim", "péssimo", "horrível", "terrível" e "odeio". Já as palavras neutras incluem "mas", "deixou", "apesar" e "embora"

Depois de calcular as contagens de palavras positivas e negativas, o programa determinará o sentimento predominante do comentário. Se houver mais palavras positivas do que negativas, o sentimento será considerado positivo. Se houver mais palavras negativas do que positivas, o sentimento será considerado negativo. Caso contrário, se houver um número igual de palavras positivas e negativas, o sentimento será neutro.

Entrada
O usuário será solicitado a fornecer um comentário como entrada para o programa.

Saída
O programa exibirá o sentimento do comentário inserido pelo usuário, que pode ser "Positivo", "Negativo" ou "Neutro", dependendo da análise das palavras-chave no comentário.'''

# Importa o módulo re, que é a biblioteca de expressões regulares do Python. 
import re

def analyze_sentiment():
    # Entrada do usuário
    comentario = input()

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    # TODO: Conte quantas palavras neutras estão presentes no comentário.  
    count_neutro = sum(palavra in neutras for palavra in palavras)
    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    # TODO: Complete a codição para determinar o sentimento com base na contagem de palavras
    if count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    if count_negativo == count_positivo and count_neutro == 0:
        return "Neutro"
    if count_neutro > count_positivo and count_negativo < count_neutro:
        return "Neutro"
# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)