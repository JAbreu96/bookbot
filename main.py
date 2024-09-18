
def countChar(words):
    charFreq = {}

    for word in words:
        for char in word:
            dict = {"char": char, "num": 1}
            char = char.lower()
            if charFreq.get(char):
                charFreq[char]["num"] += 1
            else:
                charFreq[char] = dict
    return charFreq

def sort_on(freqs):
    return freqs["num"]

def printCharFreqs(freqs_list):
    for dict in freqs_list:
        string = f"the '{dict['char']}' character was found {dict['num']} times"
        print(string)

with open('books/frankenstein.txt') as file:

    file_content = file.read()
    words = file_content.split()

    freqs = countChar(words)
    sortedChars = list(freqs.values())
    sortedChars.sort(reverse=True, key=sort_on) 
    printCharFreqs(sortedChars)
                   

