from assessment_1 import *
def test_letter_reverser():
    assert letter_reverser("hello,world") == "olleh,dlrow"
    assert letter_reverser("abc,def,ghi") == "cba,fed,ihg"
    assert letter_reverser("a,b,c") == "a,b,c"
    assert letter_reverser("!@#,hello,$%^") == "!@#,olleh,$%^"
    assert letter_reverser("") == ""
    assert letter_reverser("singleword") == "drowelgnis"