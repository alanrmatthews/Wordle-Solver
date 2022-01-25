def load_words(filename):
    words = [line.rstrip() for line in open(filename)]
    return words

def get_word_length():
    while True:
        try:
            length = int(input("Enter the word size: "))
        except ValueError:
            print("Not a number!")
            continue
        else:
            return length

def filter_by_length(words, length):
    filtered = list()

    for word in words:
        if len(word) == length:
            filtered.append(word)

    return filtered

def filter_by_response(words, guess, response):
    for idx,chr in enumerate(guess):
        if response[idx] == ".":
            words = [word for word in words if not chr in word]
        elif response[idx] == chr.upper():
            words = [word for word in words if word[idx] == chr]
        elif response[idx] == chr:
            words = [word for word in words if word[idx] != chr and chr in word]

    return words

words = load_words("words.txt")
print("Wordle Solver")

length = get_word_length()
words = filter_by_length(words, length)

while True:
    guess = words[0]
    print(guess)
    response = input("Enter the response: ")

    if ("." not in response and response == response.upper()):
        print("The answer is " + response)
        break
    else:
        words = filter_by_response(words, guess, response)