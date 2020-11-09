import pytest


def validate_card(card_code: list) -> bool:
    code = card_code
    for n in range(len(card_code)):
        if n % 2 == 0:
            multiplicator = 2
        else:
            multiplicator = 1

        if code[n] * multiplicator < 10:
            code[n] *= multiplicator
        else:
            temp = code[n] * multiplicator
            temp = str(temp)
            code[n] = int(temp[0]) + int(temp[1])

    if sum(code) % 10 == 0:
        return True
    else:
        return False


def test_validate_card():
    # given
    card = [3, 3, 7, 9, 5, 1, 3, 5, 6, 1, 1, 0, 8, 7, 9, 5]

    # when
    result = validate_card(card)

    # then
    assert result
