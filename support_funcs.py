import logging


def get_arguments(*args, **kwargs):
    """Функция формирует информацию об аргументах"""
    if args and kwargs:
        arguments = f'Аргументы: {args} {kwargs}'
    else:
        if args:
            arguments = f'Аргументы: {args}'
        elif kwargs:
            arguments = f'Аргументы: {kwargs}'
        else:
            arguments = 'Аргументов нет'
    return arguments


def setup_logger(name, log_file, level=logging.INFO):
    """Функция настраивает регистраторы"""

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(log_file, encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)

    return logger
