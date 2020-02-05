# This program will use list comprehension to turn a sentance into
# camel case. For example:
# "This is a test sentence" would become "thisIsATestSentence"

def main():
    print("This program will convert a sentance into camelCase. Please write a sentance: \n")
    sentance = input()

    print(toCamelCase(sentance))

def toCamelCase(sentance):
    # Convert sentance to list
    # Modify first element in list to be lower case, all others capitalize first letter
    words = sentance.strip().split(" ")

    # Adapted from stack overflow,
    # https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase
    # Takes first word in list and converts to lower, then joins the rest of the words in the list in title case.
    return words[0].lower() + ''.join(word.title() for word in words[1:])

if __name__ == '__main__':
    main()