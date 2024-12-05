from problem_patterns import count_unique_values

def test_count_unique_values():
    assert count_unique_values([1, 1, 1, 1, 1, 2]) == 2
    assert count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]) == 7
    assert count_unique_values([]) == 0
    assert count_unique_values([1]) == 1
    assert count_unique_values([1, 2]) == 2
    assert count_unique_values([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert count_unique_values([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]) == 3
    assert count_unique_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert count_unique_values([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4
    assert count_unique_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 10