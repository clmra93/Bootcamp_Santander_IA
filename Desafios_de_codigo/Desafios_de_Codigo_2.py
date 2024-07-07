'''Descrição
Neste desafio, você será solicitado a criar um algoritmo que avalia se um prompt fornecido pelo usuário está adequado. O programa solicitará ao usuário que insira um prompt e, em seguida, verificará se o prompt contém palavras-chave relevantes. As palavras-chave consideradas relevantes serão "inteligência artificial", "sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de tecnologia". Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informará que o prompt está adequado; caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

Entrada
O usuário será solicitado a inserir um prompt como entrada para o programa.

Saída
O programa exibirá feedback para o usuário com base na avaliação do prompt inserido. Se o prompt contiver palavras-chave relevantes, o programa informará que o prompt está adequado. Caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.'''


# Entrada do usuário
prompt_usuario = input()

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    
    # TODO: Aplique a condição necessária para verificar se o prompt está ou não adequado de acordo com o enunciado
    if any(palavra in prompt for palavra in palavras_chave):
        return "O prompt está adequado."
    else:
        return "O prompt não está adequado. Inclua palavras-chave relevantes."
# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_usuario)

# Exibir feedback
print(feedback_usuario)