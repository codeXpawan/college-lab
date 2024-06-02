sentence = input('Enter the Sentence : ')

def count_character(sentence):
    character_dict = {}
    for characters in sentence:
        if characters not in character_dict:
            character_dict[characters] = 1
        else:
            character_dict[characters] += 1
    return character_dict

print(count_character(sentence))