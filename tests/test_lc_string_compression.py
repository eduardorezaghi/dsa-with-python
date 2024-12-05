from leetcode_ws.string_compression import compress

def test_compress():
    chars = ["a", "a", "b", "b"]
    assert compress(chars) == 4
    assert chars[:4] == ["a", "2", "b", "2"]

    chars = ["a", "a", "a", "b", "b", "b", "c", "c", "c", "c"]
    assert compress(chars) == 6
    assert chars[:6] == ["a", "3", "b", "3", "c", "4"]

    chars = ["a"]
    assert compress(chars) == 1
    assert chars[:1] == ["a"]

    chars = ["a", "b", "c"]
    assert compress(chars) == 3
    assert chars[:3] == ["a", "b", "c"]

    chars = ["a", "a", "a", "a", "a"]
    assert compress(chars) == 2
    assert chars[:2] == ["a", "5"]