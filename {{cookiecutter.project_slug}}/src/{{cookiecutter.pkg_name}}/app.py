from more_itertools import map_reduce

# Scrabble letter values
_SCRABBLE_LETTER_VALUES = {
    **dict.fromkeys(list("AEIOULNRSTaeioulnrst"), 1),
    **dict.fromkeys(list("DGdg"), 2),
    **dict.fromkeys(list("BCMPbcmp"), 3),
    **dict.fromkeys(list("FHVWYfhvwy"), 4),
    **dict.fromkeys(list("Kk"), 5),
    **dict.fromkeys(list("JXjx"), 8),
    **dict.fromkeys(list("QZqz"), 10),
}


def scrabble_score(word: str) -> int:
    """
    Calculate the Scrabble score for a word using map_reduce from more_itertools.
    """

    def key_func(_: str) -> int:
        return 0  # All letters go to the same group

    def value_func(letter: str) -> int:
        return _SCRABBLE_LETTER_VALUES.get(letter, 0)

    def reduce_func(scores: list[int]) -> int:
        return sum(scores)

    # map_reduce returns a dict of {key: reduced_value}, so we extract the value
    result = map_reduce(word, key_func, value_func, reduce_func)
    return result.get(0, 0)
