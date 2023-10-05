# Домашнее задание #04 (дескрипторы, метаклассы, ABC)

### 1. Метакласс, который в начале названий всех атрибутов и методов, кроме магических, добавляет префикс "custom_"
  Подменяться должны атрибуты класса и атрибуты экземпляра класса, в том числе добавленные после выполнения конструктора (dynamic в примере).

```py
    class CustomMeta(...):
        pass


    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"


    assert CustomClass.custom_x == 50
    CustomClass.x  # ошибка

    inst = CustomClass()
    assert inst.custom_x == 50
    assert inst.custom_val == 99
    assert inst.custom_line() == 100
    assert str(inst) == "Custom_by_metaclass"

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка

    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
    inst.dynamic  # ошибка
```


### 2. Дескрипторы с проверками типов и значений данных
  Нужно сделать три дескриптора для какой-то области интереса (наука, финансы, хобби и тд), но если совсем не получается, то можно использовать шаблона ниже в качестве основы.

```py
    class Integer:
        pass

    class String:
        pass

    class PositiveInteger:
        pass

    class Data:
        num = Integer()
        name = String()
        price = PositiveInteger()

        def __init__(...):
            ....
```


### 3. Тесты метакласса и дескрипторов

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
