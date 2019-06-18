import pytest
import random
import time

from app import generate_code

ONE_WEEK = 60*60*24*7

ALPHABETS = [
    map(chr, range(ord('a'), ord('z')+1)),  # lowercase alphabet
    map(chr, range(ord('0'), ord('9')+1)),  # base-10 digits
    [i for i in 'abcdef0123456789'],        # base-16 digits
]


@pytest.mark.parametrize('now', [0, random.randint(0,10000) * ONE_WEEK])
def test_week_boundaries(now):
    today = generate_code(now, period=ONE_WEEK)
    still_this_week = generate_code(now + ONE_WEEK - 1, period=ONE_WEEK)
    next_week = generate_code(now + ONE_WEEK, period=ONE_WEEK)
    assert today == still_this_week
    assert today != next_week
    assert still_this_week != next_week


def test_current_time():
    now = time.time()
    next_week_boundary = now + (float(ONE_WEEK) - (now % float(ONE_WEEK)))
    today = generate_code(now, period=ONE_WEEK)
    still_this_week = generate_code(next_week_boundary - 1, period=ONE_WEEK)
    next_week = generate_code(next_week_boundary + 1, period=ONE_WEEK)
    assert today == still_this_week
    assert today != next_week
    assert still_this_week != next_week


@pytest.mark.parametrize('period', [1, ONE_WEEK/7, ONE_WEEK, ONE_WEEK*52])
@pytest.mark.parametrize('length', range(4, 10))
@pytest.mark.parametrize('alphabet', ALPHABETS)
def test_current_time_non_defaults(period, length, alphabet):
    now = time.time()
    args = {'period': period, 'length': length, 'alphabet': alphabet}
    next_period_boundary = now + (float(period) - (now % float(period)))
    today = generate_code(now, **args)
    still_this_period = generate_code(next_period_boundary - 1, **args)
    next_period = generate_code(next_period_boundary + 1, **args)
    assert today == still_this_period
    assert today != next_period
    assert still_this_period != next_period

@pytest.mark.parametrize('alphabet', ALPHABETS)
def test_code_string_contains_only_alphabet_members(alphabet):
    now = time.time()
    code = generate_code(now, alphabet=alphabet)
    for char in str(code):
        assert char in alphabet
