# language list
language = ['French', 'English', 'German']

# another list of language
language1 = ['Spanish', 'Portuguese']

language.extend(language1)

# Extended List


# language list
language = ['French', 'English', 'German']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending element of language tuple
language.extend(language_tuple)

print('New Language List: ', language)

# appending element of language set
language.extend(language_set)

print('Newest Language List: ', language)