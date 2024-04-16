# Напишите функцию, принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление.


def key_params(**kwargs) -> dict:
    """
    Возвращает словарь, собранный из ключевых входящих ключевых параметров,
    в котором ключами являются значения или их строковые представления,
    а значениями ключи. None хэшируется! При повторении значений в
    словаре по ключу будет возвращен список ключей параметров.
    :param kwargs: Любые ключевые параметры
    :return: Словарь вида ключ: значения.
    """
    result = {}
    for key in kwargs:
        value = kwargs.get(key)
        try:
            _ = result[value]
            result[value] = list(result[value])
            result[value].append(key)
        except KeyError:
            result[value] = key
        except TypeError:
            result[str(value)] = key

    return result


print(key_params(a=None, b=0, c=None))
