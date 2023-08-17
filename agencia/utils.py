from bardapi import Bard


def pergunta(pergunta):
    bard = Bard(token_from_browser=True)
    resposta = bard.get_answer(pergunta)['content']
    print(resposta)
