def check_relation(net, first, second, visited=tuple()):
    list_relation = list(filter(lambda el: first in el, net))
    visited = list(visited)
    visited.append(first)
    to_visit = [name for el in list_relation for name in el if name != first]
    res = list(set(to_visit) - set(visited))
    if res:
        if second in res:
            return True
        answer = any([check_relation(net, el, second, tuple(visited)) for el in res])
        return answer
    else:
        return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
