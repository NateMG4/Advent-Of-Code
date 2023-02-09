file = open('Data\Day10.txt', mode = "rt")
strings = file.readlines()
file.close()

chunkCharacters = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'}

errorScore = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137 
}
autocompleteScore = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4 
}
def partOne():

    chunkStack = []
    errorList = []
    for string in strings:
        charArray = list(string.split('\n')[0])

        for c in charArray:
            if c in chunkCharacters.keys():
                chunkStack.append(c)
                continue


            if c in chunkCharacters.values() and c == chunkCharacters.get(chunkStack[-1]):
                chunkStack.pop()
            else:
                errorList.append(c)
                chunkStack.pop()

    

    # calculate error score
    score = 0
    for e in errorList:
        score += errorScore.get(e)
    print(score)

def partTwo():

    incompleteLineCorrections = []
    for string in strings:
        charArray = list(string.split('\n')[0])
        chunkStack = []

        corrupted = False
        for c in charArray:
            if c in chunkCharacters.keys():
                chunkStack.append(c)
                continue

            
            if c in chunkCharacters.values() and c == chunkCharacters.get(chunkStack[-1]):
                chunkStack.pop()
            else:
                corrupted = True
                break
        
        if(len(charArray) != 0 and not corrupted):
            lineCorrection = []
            for open in reversed(chunkStack):
                lineCorrection.append(chunkCharacters.get(open))
            incompleteLineCorrections.append(lineCorrection)
        
                

    

    # calculate error score
    scores = []
    for line in incompleteLineCorrections:
        totalScore = 0
        for c in line:
            totalScore *= 5
            totalScore += autocompleteScore.get(c)
        scores.append(totalScore)
    scores.sort()
    print(scores[int(len(scores)/2)])





partTwo()