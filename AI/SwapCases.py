
sentence = input('Enter the sentence : ')

def swap_case(sentence):
    new_sentence = ''
    for letter in sentence:
        if letter.islower():
            letter = letter.upper()
        else:
            letter = letter.lower()
        new_sentence += letter
    return new_sentence
            
print(swap_case(sentence))
