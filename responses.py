from random import choice
from citati import vegova, fri

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '/help':
        return f'```fix\n/vegova``` -> vrne random vegova quote\n```fix\n/fri``` -> vrne random fri quote\n```fix\n/sexy``` -> vrne random sexy fotko\n```fix\nIn par easter egg-ov če rečeš točno določeno besedo```\n```fix\n/tomo``` -> vrne random tomo slikco\n```fix\n/zlebnik``` -> vrne random zlebnik slikco'

    if p_message == 'ok':
        return f'```fix\nNe ni ok\n ~ Katja Lasbaher ~```'

    if p_message in ['dan', 'dober dan']:
        return f'```fix\nDOOOBEEER DAAAN\n ~ Špela Pretnar ~```'

    if p_message == 'ane':
        return f'```fix\nAne\n ~ Dušan Sitar ~```'    

    if p_message == '/vegova':
        izbran = choice(vegova)
        return f'```fix\n{izbran[0]}\n ~ {izbran[1]} ~```'

    if p_message == '/fri':
        izbran = choice(fri)
        return f'```fix\n{izbran[0]}\n ~ {izbran[1]} ~```'        

    return ""


