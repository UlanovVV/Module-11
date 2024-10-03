from pprint import pprint


def introspection_info(obj):
    info = {}
    info['Тип'] = type(obj)
    info['Атрибуты'] = dir(obj)
    info['Методы'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['Модуль'] = obj.__module__ if hasattr(obj, '__module__') else "Неизвестно"
    return info


number_info = introspection_info(42)
pprint(number_info)

string_info = introspection_info('Hello World')
pprint(string_info)

list_info = introspection_info([1, 2, 3, 4, 5, 6])
pprint(list_info)
