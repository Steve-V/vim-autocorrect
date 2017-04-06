#!/usr/bin/env python

import itertools, string

def sep(line):
    return line=='\n'

def isClean(word):
    good_chars = string.ascii_letters + string.digits
    for character in word:
        if character not in good_chars:
            return False
    return True

def main():

    #from collections import Counter
    #with open('pidgin') as f:
        #c = Counter()
        #for x in f:
            #c += Counter(x)
        #print c

    resultlist = []

    # opene file, read in lines
    with open("/home/steve/src/hg/sdv/vim-autocorrect/pidgin","r") as infile:
        #group lines separated by blanks
        for key,group in itertools.groupby(infile,sep):
            #print(key,list(group))
            if not key:
                resultlist.append( list(group) )
                
    resultlist = [eachitem[2:] for eachitem in resultlist]

    resultTuples = [tuple(eachitem) for eachitem in resultlist]

    for (bad,good) in resultTuples:
        bad = bad.rstrip()
        bad = bad[4:]
        good = good.rstrip()
        good = good[5:]

        if isClean(bad + good):
            output = ''.join( (bad,'->',good) )

    for eachitem in output:
        print(eachitem)



main()
