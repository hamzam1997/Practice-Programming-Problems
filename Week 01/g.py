def frame(lst):
    lenlst = []
    for i in lst:
        lenlst.append(len(i))
    maximumWordLength = max(lenlst)

    for i in range(maximumWordLength+2):
        print("*", end = "")
    print("")
    for i in lst:
        print("*" + i + str((maximumWordLength - len(i)) * " ") + "*")
    for i in range(maximumWordLength+2):
        print("*", end = "")

frame(["Hello", "Worlfdsfdfdfdfdfdfdfd", "In", "a", "Frame"])


def song():
    str1 = " bottles of beer"
    str11 = " bottle of beer"
    str2 = " on the wall"
    str3 = "Take one down and pass it around, "
    for i in range(99,-1,-1):
        strf = str(i) + str1
        strf2 = ""
        strf3 = strf
        if i == 1:
            strf = str(i) + str11
            strf2 = 'no more' + str1
            
        elif i == 0:
            strf = 'No more' + str1
            strf3 = 'no more' + str1
            str3 = 'Go to the store and buy some more, '
            strf2 = '99' + str1
        else:
            strf2 = str(i-1) + str1
            if (i-1) == 1:
                strf2 = str(i-1) + str11
    
        print(strf + str2 + ', ' + strf3 + '.\n' + str3 + strf2 + str2 + '.\n' )
song()
