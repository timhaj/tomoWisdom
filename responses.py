def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'S katere hoste pa si ti prsu?'

    if p_message == '/wisdom':
        return 'Glava pred roko'

    return 'Za koksi kupil suknjič? Po dobavni ceni'


