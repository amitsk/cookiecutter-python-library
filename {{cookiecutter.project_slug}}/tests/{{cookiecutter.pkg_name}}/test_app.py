from {{cookiecutter.pkg_name}}.app import scrabble_score


def test_scrabble_score_basic():
	assert scrabble_score("cat") == 5  # c=3, a=1, t=1
	assert scrabble_score("quiz") == 22  # q=10, u=1, i=1, z=10
	assert scrabble_score("JAZZ") == 29  # J=8, A=1, Z=10, Z=10
	assert scrabble_score("hello") == 8  # h=4, e=1, l=1, l=1, o=1

def test_scrabble_score_empty():
	assert scrabble_score("") == 0

def test_scrabble_score_non_letters():
	assert scrabble_score("cat!") == 5  # '!' ignored
	assert scrabble_score("123") == 0
	assert scrabble_score("a b c") == 7  # spaces ignored
