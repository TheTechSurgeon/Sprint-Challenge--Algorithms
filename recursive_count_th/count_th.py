'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC if string doesnt have less than 2 letters can't work.
    if len(word) < 2:
        return 0
    # see if th is in the NEXT 2 indices
    if word[:2] == "th":
    #if it is increase the count
        count = count_th(word[2:])
        return count + 1
    else:
        count = count_th(word[1:])
        return 0 + count
  
