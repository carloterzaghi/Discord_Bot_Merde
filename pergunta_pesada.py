import random

def escolha_pergunta_pesada():
    lista = [
        'Quem é mais provável de comer a ex do(a) amigo(a)', 'Você precisa apagar um de nós da memória. Quem?', "Quem é mais provável de namorar um parente seu?",
        "Quem você menos gostaria de ver pelado(a)?"
        ]
    return [random.choice(lista), 3]

def quantidade3():
    lista = [
        'Quem é mais provável de comer a ex do(a) amigo(a)', 'Você precisa apagar um de nós da memória. Quem?', "Quem é mais provável de namorar um parente seu?",
        "Quem você menos gostaria de ver pelado(a)?"
        ]
    return len(lista)