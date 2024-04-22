from random import choice

d = [
    ("Glava pred roko", "Tomo Omahna"),
    ("S katere hoste pa si ti pršu?", "Tomo Omahna")
]

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '/wisdom':
        izbran = choice(d)
        return f'```fix\n{izbran[0]}\n ~ {izbran[1]} ~```'

    return 'Za koksi kupil suknjič? Po dobavni ceni'


