# Dario Melconian 251044493 Assign 3
from sentiment_analysis import compute_tweets

# ask the user to input files name
file1 = input("Enter the \"tweets\" file name: ")
file2 = input("Enter the \"keywords\" file name: ")

try:
    computed_tweets = compute_tweets(file1, file2)
    # create variable for each tuple returned from the function compute_tweets
    eastern = computed_tweets[0]
    central = computed_tweets[1]
    mountain = computed_tweets[2]
    pacific = computed_tweets[3]

    # print statements to show results
    print("The average happiness score in Eastern Standard Timezone is: ", "%.4f" % eastern[0])
    print("The total number of Eastern Standard Timezone keyword-tweets is: ", eastern[1])
    print("The total number of Eastern Standard Timezone tweets is: ", eastern[2])
    print()
    print("The average happiness score in Central Standard Timezone is: ", "%.4f" % central[0])
    print("The total number of Central Standard Timezone keyword-tweets is: ", central[1])
    print("The total number of Central Standard Timezone tweets is: ", central[2])
    print()
    print("The average happiness score in Mountain Standard Timezone is: ", "%.4f" % mountain[0])
    print("The total number of Mountain Standard Timezone keyword-tweets is: ", mountain[1])
    print("The total number of Mountain Standard Timezone tweets is: ", mountain[2])
    print()
    print("The average happiness score in Pacific Standard Timezone is: ", "%.4f" % pacific[0])
    print("The total number of Pacific Standard Timezone keyword-tweets is: ", pacific[1])
    print("The total number of Pacific Standard Timezone tweets is: ", pacific[2])

# errors in case file is non-existent
except IOError:
    print("Error: File does not exist.")
    print([])

except RuntimeError:
    print("Runtime Error")

# errors in case files inputted are invalid
except ValueError:
    print("Error: File is invalid.")
