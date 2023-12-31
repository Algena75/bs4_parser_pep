# utils.py
import logging

from requests import RequestException

from exceptions import ParserFindTagException, ResponseIsNoneException


def get_response(session, url, whats_new_list=None):
    """Перехватывает ошибку загрузки страницы при парсинге."""
    message = f'Возникла ошибка при загрузке страницы {url}'
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        if response is None and whats_new_list is None:
            raise ResponseIsNoneException(message)
        return response
    except RequestException:
        logging.exception(
            message,
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    """Перехватывает ошибку отсутствия тега в 'супе'."""
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def logging_wrong_statuses(wrong_statuses):
    """Обрабатывает логирование несоответствия статусов."""
    if wrong_statuses:
        message = 'Несовпадающие статусы:\n'
        for item in wrong_statuses:
            message = message + (
                f'{item[0]}\nСтатус в карточке: {item[1]}\n'
                f'Ожидаемые статусы: {item[2]}\n'
            )
        logging.info(message)
