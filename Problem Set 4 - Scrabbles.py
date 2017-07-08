# Problem 1 - Word Scores
# Calculate the score for a single word. 
# The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
def getWordScore(word, n):
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    finalscore = score *len(word)
    if len(word) == n:
        finalscore = finalscore + 50
    return finalscore

# Problem 2 - Dealing with Hands
# A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. 
# In our program, a hand will be represented as a dictionary:
# the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand.
# The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up
# Implement the function updateHand, which takes in two inputs - a hand and a word (string). 
# updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining.
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_new = hand.copy()
    for k in word:
        if k in hand_new.keys():
            hand_new[k] -= 1
    return hand_new

#Problem 3 - Valid Words
# Write a code to verify that a word given by a player obeys the rules of the game. 
# A valid word is in the word list; and it is composed entirely of letters from the current hand. 
# Implement the isValidWord function.
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_new = hand.copy()
    for letter in word:
        if letter not in hand_new or hand_new[letter] <= 0:
            return False
        else:
            hand_new[letter] -= 1
    if word in wordList:
        return True
    return False

# Problem 4 - Hand Length
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    for letter in hand:
        length += hand[letter]
    return length

# Problem 5 - Playing a Hand
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
   
    updatedscore = 0
    # Keep track of the total score
    while calculateHandlen(hand):
        # As long as there are still letters left in the hand:
        displayHand(hand)
        # Display the hand
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # Ask user for input
        if word == '.':
            # If the input is a single period:
            break
            # End the game (break out of the loop)
        else:
            # Otherwise (the input is not a single period):
            if not isValidWord(word, hand, wordList):
                # If the word is not valid:
                print('Invalid word, please try again.')
                # Reject invalid word (print a message followed by a blank line)
            else:
                # Otherwise (the word is valid):
                updatedscore += getWordScore(word, n)
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print(word + 'earned ' + str(getWordScore(word, n)) + 'points.' + 'Total: ' + str(updatedscore) + ' points.')
                hand = updateHand(hand, word)
                # Update the hand 
    if calculateHandlen(hand) > 0:
        print('Goodbye! Total score: ' + str(updatedscore))
    else:
        print('Run out of letters. Total score: ' + str(updatedscore))
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    
    # Problem 6 - Playing a Game
    # A game consists of playing multiple hands. 
    # Implement one final function to complete our word-game program. 
    # Write the code that implements the playGame function. 
    # Read through the specification and make sure you understand what this function accomplishes. 
    # For the game, use the HAND_SIZE constant to determine the number of cards in a hand.
    
    key = ''
    hand = ''
    while True:
        key = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if key == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif key == 'r':
            if hand == '':
                print('You have not played a hand yet. Please play a new hand first!')
                continue
            playHand(hand, wordList, HAND_SIZE)
        elif key == 'e':
            break
        else:
            print('Invalid command.')




