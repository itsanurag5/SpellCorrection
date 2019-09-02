import os
import re
from flask import Flask, render_template, request, jsonify
from numpy.core.defchararray import lower
from symspellpy.symspellpy import SymSpell, Verbosity
from textblob import Word

app = Flask(__name__)


@app.route('/spellCorrect', methods=["GET", "POST"])
def spellCorrect():
    if request.method == 'POST':
        input_term = request.form['text'].lower()
        input_term = re.sub('[^A-Za-z0-9]+', '', input_term)

        # the below 'spellcheck' from textblob library will help to identify the
        # incorrect words and give the correct words.
        words = Word(input_term).spellcheck()
        print("words: ", words)
        res = []
        counter = 0
        for w in words:
            if counter < 5:
                res.append(w[0])
                counter += 1

        # adding another functions from SymSpell library for more robust result
        max_edit_distance_dictionary = 2
        prefix_length = 7
        # create object
        sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
        # load dictionary
        dictionary_path = os.path.join(os.path.dirname(__file__),
                                       "frequency_dictionary_en_82_765.txt")
        term_index = 0  # column of the term in the dictionary text file
        count_index = 1  # column of the term frequency in the dictionary text file
        if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
            print("Dictionary file not found")
            return "Dictionary file not found"

        max_edit_distance_lookup = 2
        suggestion_verbosity = Verbosity.CLOSEST  # TOP, CLOSEST, ALL

        # the below 'lookup' function will help to identify the correct spelling
        # using the SymSpell library.
        suggestions = sym_spell.lookup(input_term, suggestion_verbosity,
                                       max_edit_distance_lookup)
        # display suggestion term, term frequency, and edit distance
        for suggestion in suggestions:
            print("{}, {}, {}".format(suggestion.term, suggestion.distance,
                                      suggestion.count))
            res.append(suggestion.term)
        print("res: ", res)

        # the below 'lookup_compound' function will help to identify the correct spelling
        # if there is any space is missing or extra spaces are given.
        suggestions = sym_spell.lookup_compound(input_term,
                                                max_edit_distance_lookup)
        for suggestion in suggestions:
            print("{}, {}, {}".format(suggestion.term, suggestion.distance,
                                      suggestion.count))
            res.append(suggestion.term)
        print("res: ", res)

        # remove duplicates from the list
        result = []
        for r in res:
            if r not in result:
                result.append(r)

        return jsonify(result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()