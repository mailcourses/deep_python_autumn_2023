# Домашнее задание #05 (стандартная библиотека)

### 1. LRU-кэш
Интерфейс:

```py
    class LRUCache:

        def __init__(self, limit=42):
            pass

        def get(self, key):
            pass

        def set(self, key, value):
            pass


    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"


    Если удобнее, get/set можно сделать по аналогии с dict:
    cache["k1"] = "val1"
    print(cache["k3"])
```

Сложность решения по времени в среднем должна быть константной O(1).
Реализация любым способом без использования OrderedDict.

### 2. Тесты в отдельном модуле

### 3. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
