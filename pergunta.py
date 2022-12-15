import random

def escolher_aleatorio():
    lista = [
        'Quem é o mais provável de sair com a/o ex de seu amigo?', 'Quem é mais provável de namorar um parente seu?', 
        'Acordamos em uma ilha deserta e sem nenhum alimento. Quem irá propor canibalismo?', "Quem é mais provável de ser preso por um crime que não cometeu?",
        "Quem entre noís é mais provável ser um traficante", "Somos parte de um grupo de foragidos no Velho Oeste. A cabeça de quem vale menos?",
        'Jamais encostaria na roupa íntima de...', 'Cada um de nós é responsável por uma equipe de uma empresa. Quem mais maltrata os seus funcionários?',
        'Quem é o(a) mais iludido(a)?', 'Estamos em um Apocalipse Zumbi! Quem é o primeiro a morrer?', 
        "Ganhamos na loteria e dividimos o prêmio entre todos nós. Quem é o primeiro a gastar toda a sua parte?",
        "Um de nós, secretamente, deseja a morte dos outros. Quem?", 'Quem apresenta uma vida dupla?', "Quem é mais provável de se perder no shopping?",
        "Quem é o mais provável de se esquecer do aniversário de alguém?", 'Quem é mais provável de contar um segredo?', 'Você tem que socar a cara de um de nós. Quem você escolhe?',
        "O serviço militar agora é obrigatório para todos. Quem é o primeiro a atirar no próprio pé para não servir?", 'Quem de nós você jamais se atreveria a deixar irritado?',
        "Quem fez xixi na piscina?", "Todos fazem academia, quem seria o primeiro a deistir dela?"
    ]
    return [random.choice(lista), 1]

def quantidade1():
    lista = [
        'Quem é o mais provável de sair com a/o ex de seu amigo?', 'Quem é mais provável de namorar um parente seu?', 
        'Acordamos em uma ilha deserta e sem nenhum alimento. Quem irá propor canibalismo?', "Quem é mais provável de ser preso por um crime que não cometeu?",
        "Quem entre noís é mais provável ser um traficante", "Somos parte de um grupo de foragidos no Velho Oeste. A cabeça de quem vale menos?",
        'Jamais encostaria na roupa íntima de...', 'Cada um de nós é responsável por uma equipe de uma empresa. Quem mais maltrata os seus funcionários?',
        'Quem é o(a) mais iludido(a)?', 'Estamos em um Apocalipse Zumbi! Quem é o primeiro a morrer?',
        "Ganhamos na loteria e dividimos o prêmio entre todos nós. Quem é o primeiro a gastar toda a sua parte?",
        "Um de nós, secretamente, deseja a morte dos outros. Quem?", 'Quem apresenta uma vida dupla?', "Quem é mais provável de se perder no shopping?",
        "Quem é o mais provável de se esquecer do aniversário de alguém?", 'Quem é mais provável de contar um segredo?', 'Você tem que socar a cara de um de nós. Quem você escolhe?',
        "O serviço militar agora é obrigatório para todos. Quem é o primeiro a atirar no próprio pé para não servir?", 'Quem de nós você jamais se atreveria a deixar irritado?',
        "Quem fez xixi na piscina?", "Todos fazem academia, quem seria o primeiro a deistir dela?"
    ]
    return len(lista)