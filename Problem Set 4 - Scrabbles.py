# **Problem 1 - Word Scores**
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
