#from nltk import regexp_tokenize

def read_file():
    fileName = input()
    file = open(fileName, "r", encoding="utf-8")
    data = file.read()
  #  tokenized = regexp_tokenize(data, "[0-9A-z'\"?!.…,]+")
    tokenized = data.split()
    file.close()
    return tokenized, len(tokenized), len(set(tokenized))

def is_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    tokenized_string, token_size, token_unique_size = read_file()
    print("Corpus statistics")
    print("All tokens: ", token_size)
    print("Unique tokens: " , token_unique_size)
    while(True):
        user_input = input()
        if user_input == "exit":
            break
        if is_integer(user_input):
            int_input = int(user_input)
            if int_input < token_size:
                print(tokenized_string[int_input])
            else:
                print("Index Error. Please input an integer that is in the range of the corpus.")
        else:
            print("Type Error. Please input an integer.")
