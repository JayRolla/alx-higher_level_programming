def complex_delete(a_dictionary, value):
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
complex_delete(a_dictionary, 'C')
print(a_dictionary)
