Spelling error is quite common while typing. To give the suggestions for the misspelled word below approaches are tried:

1. Textblob Library 

While looking for the library to correct the misspelled word, i found the 'textblob' library which is used to correct the misspelled words. There are two main functions which are used for spell correction.
a.  correct() function: Given the word or sentence, this function will return the correct spelling if any word is misspelled.
b. spellcheck() function: Given the word or sentence, this function will returns a list of (word, confidence) tuples with spelling suggestions, where word is the correct word and confidence is the probability of word being correct.

limitation of textblob: textblob library was not working when the space is missing between the words or space is entered by mistake between a correct word. To overcome this limitation i used the below library.

2. Symspell library
Symspell is the another library which is used for spelling correction. This library overcomes the limitation of textblob as well as it's give the output faster. There are mainly three functions for spellcheck
a. lookup() function: This method can correct the spelling of the misspelled word but this method is not efficient if the spaces are missing or extra space is given.
b. lookup_compound() function: this method can insert only a single space into a token (string fragment separated by existing spaces). It is intended for spelling correction of word segmented text but can fix an occasional missing space. It is faster and the quality of the correction is usually better.
c. word_segmentation() function: this method can insert as many spaces as required into a token. Therefore it is suitable also for long strings without any space. The drawback is a slower speed and correction quality.

Final Result:

In my final web app, I have used below functions:
1. spellcheck() from textblob
2. lookup() from the symspell
3. lookup_compound() from the symspell

And after that I have combined the result that these three functions return and display in the json format.



Packages to be install to run this code:

1. Flask
2. textblob
3. symspellpy
4. numpy



Future Scope:

1. Currently the API is showing multiple outputs for some words, we can restrict the number of suggestion to n as per the business requirement.
2. Currently more focused has been given to build the API and the less for the html page to enter and display the result, as per the business requirement more user friendly UI can be build and it can show the result on the same page.