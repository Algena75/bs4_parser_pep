class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ResponseIsNoneException(Exception):
    """Вызывается, когда ответ сервера не получен."""
    pass
