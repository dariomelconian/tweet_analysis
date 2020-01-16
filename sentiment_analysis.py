def compute_tweets(file1, file2):

    # counters for each regions tweets, keyword-tweets, and score
    easternZoneTweets = 0  # count of tweets in eastern
    easternKeywords = 0  # count of keywords in eastern
    easternScore = 0  # sentiment score in eastern

    centralZoneTweets = 0  # count of tweets in central
    centralKeywords = 0  # count of keywords in central
    centralScore = 0  # etc

    mountainZoneTweets = 0
    mountainKeywords = 0
    mountainScore = 0

    pacificZoneTweets = 0
    pacificKeywords = 0
    pacificScore = 0

    keywordsList = []  # list of all keywords
    keywordValues = []  # list of their sentiment scores in same order

    # this function determines if the tweet and its coordinates even qualify in ANY timezone
    def InTimezone(lat, long):
        lat = float(lat)
        long = float(long)
        if lat < 49.189787 and lat > 24.660845:
            if long < -67.444574 and long > -87.518395:
                return True
            elif long < -87.518395 and long > -101.998892:
                return True
            elif long < -101.998892 and long > -115.236428:
                return True
            elif long < -115.236428 and long > -125.242264:
                return True

    # this function determines the location of each tweet by timezone, after knowing it is in 1 of the 4 timezones
    def TimezoneDeterminent(lat, long):
        a = 0
        if lat < 49.189787 and lat > 24.660845:
            if long < -67.444574 and long > -87.518395:
                a = 1
                # "Eastern"
            elif long < -87.518395 and long > -101.998892:
                a = 2
                # "Central"
            elif long < -101.998892 and long > -115.236428:
                a = 3
                # "Mountain"
            elif long < -115.236428 and long > -125.242264:
                a = 4
                # "Pacific"
        return a

    # this function computes the keyword score per tweet, and returns a happiness score
    def getKeywordScore(tweet):
        score = 0
        keywordsPerTweet = 0
        happiness = 0
        for q in range(len(tweet)):
            for j in range(len(keywordsList)):
                if tweet[q].lower() == keywordsList[j]:
                    keywordsPerTweet += 1
                    score += keywordValues[j]
                    happiness = score / keywordsPerTweet

        return happiness

    # open files #
    # then, if issue with files, exception, and raise it back to main function to deal with error based on its type (value or IOError)
    try:
        tweets = open(file1, "r", encoding="utf‐8")
        keywords = open(file2, "r", encoding="utf-8")
    except:
        raise

    # this for loop goes through each line in "keyword.txt" and puts it in 2 lists (keywords and their values)
    for line in keywords:
        line = line.rstrip()
        line = line.rsplit(",")
        keywordsList.append(line[0])  # now have list of keywords from keywords.txt
        keywordValues.append(line[1])  # now have list of keyword VALUES from keywords
        for i in range(0, len(keywordValues)):
            keywordValues[i] = int(keywordValues[i])

    # sentiment analysis #
    # this for statement begins the breaking down of elements in "tweets.txt" for every line and creates a word list
    for line in tweets:
        tweetContents = []
        line = line.lower()
        line = line.strip('[],!>}{+=_-`\;*|#:$%^&<*()=@_~-/.?"/"')
        line = line.rstrip()
        line = line.split(" ", 5)
        text = line[5]
        wordList = text.split()
        for i in range(len(wordList)):
            wordList[i] = wordList[i].lower()
            wordList[i] = wordList[i].rstrip("!\'!@#$%^&}<*]>`()\"~_:;{=//+|[-.,?[\]'")
            wordList[i] = wordList[i].lstrip("!\'!@#$%^&}<*]>`()\"~_:;{=//+|[-.,?[\]'")
        tweetContents.append(line[0].strip('[],'))
        tweetContents.append(line[1].strip('[],'))
        tweetContents.append(wordList)  # wordList becomes third item in tweetContents list
        tweetContents[0] = float(tweetContents[0])
        tweetContents[1] = float(tweetContents[1])

        # this uses the above functions to compute scores for each region knowing if each tweet is in a timezone,
        # its region, and its keyword count, tweet count, as well as happiness score
        if InTimezone(tweetContents[0], tweetContents[1]):
            timeZoneNum = TimezoneDeterminent(tweetContents[0], tweetContents[1])

            if timeZoneNum == 1:
                easternZoneTweets += 1
                tempScore = getKeywordScore(tweetContents[2])  # pass the wordList in to generate score
                if(tempScore > 0):
                    easternKeywords += 1
                    easternScore += tempScore

            elif timeZoneNum == 2:
                centralZoneTweets += 1
                tempScore = getKeywordScore(tweetContents[2])
                if(tempScore > 0):
                    centralKeywords += 1
                    centralScore += tempScore

            elif timeZoneNum == 3:
                mountainZoneTweets += 1
                tempScore = getKeywordScore(tweetContents[2])
                if (tempScore > 0):
                    mountainKeywords += 1
                    mountainScore += tempScore

            elif timeZoneNum == 4:
                pacificZoneTweets += 1
                tempScore = getKeywordScore(tweetContents[2])
                if (tempScore > 0):
                    pacificKeywords += 1
                    pacificScore += tempScore

    # this determines the average for each happiness score in each region
    if easternKeywords == 0:
        easternAverage = 0
    else:
        easternAverage = (easternScore / easternKeywords)

    if centralKeywords == 0:
        centralAverage = 0
    else:
        centralAverage = (centralScore / centralKeywords)
    if mountainKeywords == 0:
        mountainAverage = 0
    else:
        mountainAverage = (mountainScore / mountainKeywords)
    if pacificKeywords == 0:
        pacificAverage = 0
    else:
        pacificAverage = (pacificScore / pacificKeywords)

    # append each value as a list of tuples of 3 (score, keyword-tweets, and total tweets) in each region
    # now create tuples to return your values from compute_tweets function to main() to be printed
    tuple1 = []
    tuple2 = []
    tuple3 = []
    tuple4 = []
    tuple1.append(easternAverage)
    tuple1.append(easternKeywords)
    tuple1.append(easternZoneTweets)
    tuple2.append(centralAverage)
    tuple2.append(centralKeywords)
    tuple2.append(centralZoneTweets)
    tuple3.append(mountainAverage)
    tuple3.append(mountainKeywords)
    tuple3.append(mountainZoneTweets)
    tuple4.append(pacificAverage)
    tuple4.append(pacificKeywords)
    tuple4.append(pacificZoneTweets)

    return [tuple1, tuple2, tuple3, tuple4]

