from treasure_hunter.dungeon import *

def test_probability_is_between_zero_and_one():
    trials = 100
    probability = success_chance(trials = trials)
    assert probability >= 0 and probability <= 1

test_probability_is_between_zero_and_one()
