from random import choice
from citati import vegova as d

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'ok':
        return f'```fix\nNe ni ok\n ~ Katja Lasbaher ~```'

    if p_message == 'ane':
        return f'```fix\nAne\n ~ Dušan Sitar ~```'    

    if p_message == '/wisdom':
        izbran = choice(d)
        return f'```fix\n{izbran[0]}\n ~ {izbran[1]} ~```'

    return 'Uporab: /wisdom'


