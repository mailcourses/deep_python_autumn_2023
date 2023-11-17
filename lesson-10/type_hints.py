from typing import Any, Callable, Generator, Iterable, Optional, Sequence, TypeVar

from add_numbers import add_numbers


UserData = dict[str, str | int]

T = TypeVar("T")
TRes = TypeVar("TRes")


# class StrInt(int, str):
#     pass
#
#
# class StrIntBool(int, str):
#     pass


def apply_function(
    fn: Callable[[T, T], TRes],
    left_operand: T,
    right_operand: T,
) -> TRes:
    return fn(left_operand, right_operand)


def gen() -> Generator[int, Any, str]:
    yield 10
    yield 20
    yield 30

    return "finish"  # StopIteration("finish")


class User:
    id = "user[99]"


def fetch_url(url: str) -> UserData:
    return {"name": "Steve", "age": 99}


def fetch_url_other(url: str) -> UserData:
    return {"name": "Rob", "age": 88}


def fetch_user_data(user: User) -> UserData | None:
    url: str = f"http://persons/?id={user.id}"

    resp: Optional[UserData] = None

    if url == "1":
        resp = fetch_url(url)
    elif url == "2":
        resp = fetch_url_other(url)

    return resp


class NotUser:
    id = "NotUser[1024]"


def get_max(ages: Iterable[int]) -> int | None:
    if not ages:
        return None

    return max(ages)


def get_first(ages: Sequence[int]) -> int | None:
    if not ages:
        return None

    return ages[0]


def run() -> None:
    print(add_numbers(1, 2))
    # print(add_numbers("1", "2"))  # wrong

    fetch_user_data(User())
    # fetch_user_data(NotUser())  # wrong

    print(get_max([1, 2, 3, 1]))
    print(get_max({1, 2, 3, 1}))
    # print(get_max(1231))  # wrong

    print(get_first([1, 2, 3, 1]))
    print(get_first([]))
    # print(get_first([1, "3"]))
    # print(get_first({1, 2, 3, 1}))

    res: int | None = get_first([1, 2, 3, 1])

    print(apply_function(add_numbers, 100, 99))
    print(apply_function(lambda x, y: x + y, "100", "99"))

    g = gen()
    next(g)
    g.send(123)


if __name__ == "__main__":
    run()
