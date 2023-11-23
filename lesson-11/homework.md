# Домашнее задание #11 (Расширения на C)

## Реализовать библиотеку для парсинга и сериализации json (с помощью C API)
- Нужно написать модуль cjson, который имел бы хотя бы два метода: loads и dumps;
- Методу loads на вход подаётся строка в формате JSON. Ограничения:
    * JSON-сообщение в виде набор пар ключ-значение (читай как python-словарь);
    * Ключём в JSON **всегда** является строка в двойных кавычках;
    * Значением может выступать либо число, либо строка. Если захотелось приключений, то можно сделать поддержку и других типов;
    * Если входная строка не является JSON-объектом, то возвращаем исключение
       ```C
       ...
       PyErr_Format(PyExc_TypeError, "Expected object or value");
       return NULL;
       ```
    * Возвращать мы должны объект типа dict. Например, это можно сделать так:
        ```C
        PyObject *dict = NULL;
        if (!(dict = PyDict_New())) {
            printf("ERROR: Failed to create Dict Object\n");
            return NULL;
        }

        PyObject *key = NULL;
        PyObject *value = NULL;
        if (!(key = Py_BuildValue("s", "hello"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (!(value = Py_BuildValue("i", 10))) {
            printf("ERROR: Failed to build integer value\n");
            return NULL;
        }
        if (PyDict_SetItem(dict, key, value) < 0) {
            printf("ERROR: Failed to set item\n");
            return NULL;
        }
        if (!(key = Py_BuildValue("s", "world"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (!(value = Py_BuildValue("s", "100500"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (PyDict_SetItem(dict, key, value) < 0) {
            printf("ERROR: Failed to set item\n");
            return NULL;
        }

        return dict;
        ```
- Методу dumps в качестве аргумента передаётся объект типа dict и возвращает строку. Ограничения как у loads только наоборот;

### Написать Makefile
При выполнении команды make происходит следующее:
- Создаваться и активироваться виртуальное окружение в папку venv с установкой всех необходимых библиотек;
- Компиляция кода и установка модуля (выполнялся бы setup.py install);
- Должна быть цель test, которая запустит тесты (перед запуском цели test всегда будет выполняться команда make).

### Написать тесты
Нужно написать тесты корректности работы методов loads и dumps на языке Python, проверяющие корректность парсинга и дампа (с помощью unittest);
```Python
#! /usr/bin/env python3

import json

import ujson

import cjson

def main():
    json_str = '{"hello": 10, "world": "value"}'
    json_doc = json.loads(json_str)
    ujson_doc = ujson.loads(json_str)
    cjson_doc = cjson.loads(json_str)
    assert json_doc == ujson_doc == cjson_doc
    assert json_str == cjson.dumps(cjson.loads(json_str))

if __name__ == "__main__":
    main()
```
Использование модуля **unittest** или **pytest** является обязательным.

### Написать тест производительности
Сравнивать скорость работы своей реализации с json и ujson на одних и тех же данных. Данные должны быть большие (как количество JSON, так и размер каждого JSON). Требование: выполнение тестов не менее 100 мс.

Для генерации тестовых JSON можно использовать статический найденный на просторах интернета JSON. Если с этим будет беда, то постучитесь к лектору, он скинет дамп.

Для особо любознательных: можно попробовать использовать библиотеку [Faker](https://faker.readthedocs.io/en/master/) для генерации данных.
