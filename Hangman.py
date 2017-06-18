# Implement a variation of the classic wordgame Hangman.

# Problem 1
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

# Problem 2
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for i in secretWord:
        if i in lettersGuessed:
            result += i
        else:
            result += '_'
    return result

# Problem 3
def getAvailableLetters(lettersGuessed):
     '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    '''
    import string
    result = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            result += i
    return result

#implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer.

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    lettersGuessed = ''
    numGuesses = 0
    print("-----------")
    while numGuesses < 8:
        print('You have ' + str(8 - numGuesses) + ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        guess = input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            if guess in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                numGuesses += 1
        print("-----------")
        if numGuesses == 8:
            print("Sorry, you ran out of guesses. The word was" + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations! You won!")
            break
