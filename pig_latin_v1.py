from ast import NotIn


vowels = 'AaEeIiOoUu'
finished_list = 'Qq'
count = 0
translate_list = []
translated_words = open('translations.txt', 'a')


# Have the user add words to the list to be translated
def add_words():
    words = 'a'
    while words not in finished_list:
        words = input('Please write a word or sentence you wish to add to the translation list, write \'Q\' if you are finished: ')
        words_split = words.split()
        if words in finished_list:
            break
        else:
            translate_list.extend(words_split)


#Function to check if the word is a consonant or a vowel and modify it accordingly
def check_word():
    global translate
    global vowels
    con_cluster = []
    while translate[0] not in vowels:
        first_letter = translate[0]
        con_cluster.extend(translate[0])
        translate = translate.replace(first_letter, '',1)
    else:
        cluster = ''.join(con_cluster)
        translate = translate + '-' + cluster + 'ay'

# Main section of code, checks each word in the list and saves translated word back to the list
# Also sends the list of words from the user to the file
print('Welcome to the Pig-Latin translator.')
add_words()
translated_words.write(str(translate_list) + '\n')
translate = translate_list[count]
while count <= (len(translate_list) -1):
    translate = translate_list[count]
    check_word()
    translate_list[count] = translate
    count += 1

# Writes the translated words to the file and gives the user the option to also see it on screen
print('Contratulations your translation is complete, see file \'translations.txt\' for the translated word list')
results = input('To view this sessions translations here type \'today\' to see all translations in the file type \'all\': ')
translated_words.write(str(translate_list) + '\n\n')
translated_words.close
translated_words = open('translations.txt', 'r')
if results == 'today':
    read_list = translated_words.readlines()
    print(read_list[-3] + read_list[-2])
elif results == 'all':
    print(translated_words.read())
else:
    print('Thank you')