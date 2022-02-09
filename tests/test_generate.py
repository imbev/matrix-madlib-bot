import sys, os; sys.path.append(os.getcwd())
import madlib_bot

def test_generate():
    source = "%aj, %vb, %av, %nn, %pn, %pl."

    adjective = ["1"]
    verb = ["2"]
    adverb = ["3"]
    noun = ["4"]
    pronoun = ["5"]
    place = ["6"]

    expected = "1, 2, 3, 4, 5, 6."

    generated = madlib_bot.generate(
        source, adjective, verb, adverb, noun, 
        pronoun, place) 

    print(expected)
    print(generated)

    assert generated == expected
