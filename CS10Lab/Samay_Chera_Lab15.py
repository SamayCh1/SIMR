# Exercise 1
def base_freq(sequence) -> dict:
    """
    Calculate the frequency of each base pair in a DNA sequence string.

    Parameters:
    - sequence (str) or (lst): The DNA sequence string or list of entries.

    Returns:
    - dict: A dictionary with the base pair as the key and its frequency as the value.

    Examples:
    >>> base_freq("AAGTTAGTCA") == {"A": 4, "C": 1, "G": 2, "T": 3}
    True
    >>> result = base_freq([4, 4, 4, 5, 5, 5, 2, 2, 1])
    >>> result == {4: 3, 5: 3, 2: 2, 1: 1} #the number 4 appears 3 times
    True
    """
    if type(sequence) == str: 
        sequence = [sequence[i] for i in range(0,len(sequence))]

    unique = []   
    for i in range(0,len(sequence)): 
        if not sequence[i] in unique:
            unique.append(sequence[i])
    
    freq = []
    for i in range (0, len(unique)):
        freq.append(0)
    for item in sequence: 
        freq[unique.index(item)] += 1
    
    dic = {}
    for i in range(0, len(unique)): 
        dic[unique[i]] = freq[i]

    return dic




# Exercise 2
def substitute_chars(string, replacements) -> str:
    """
    Substitute characters in a string based on a dictionary of replacements.

    Parameters:
    - string (str): The original string to be modified.
    - replacements (dict): A dictionary of character replacements.

    Returns:
    - str: The modified string with characters substituted according to the replacements dictionary.
    Examples:
    >>> replacements = {"S":"Z", "E":"U", "T":"P", "A":"M"}
    >>> substitute_chars("SECRET MESSAGE", replacements)
    'ZUCRUP MUZZMGU'
    >>> replacements = {"P": "Pikachu, ", "B": "Bulbasaur, ", "C": "Charmander, ", "S": "Squirtle"}
    >>> result = substitute_chars("I choose you, PBCS!", replacements)
    >>> result
    'I choose you, Pikachu, Bulbasaur, Charmander, Squirtle!'
    """
    newword = [string[i] for i in range(0, len(string))]

    for i in range(0, len(newword)): 
        if newword[i] in replacements.keys():
            newword[i] = replacements.get(newword[i])

    return "".join(newword)

# print(substitute_chars("SECRET MESSAGE", {"S":"Z", "E":"U", "T":"P", "A":"M"}))

# Exercise 3
def invert_dict(original) -> dict:
    """
    Invert a dictionary, swapping keys and values.

    Parameters:
    - original (dict): The original dictionary to be inverted.

    Returns:
    - dict: The inverted dictionary, where the keys and values of the original dictionary are swapped.

    Examples:
    >>> invert_dict({})
    {}
    >>> result = invert_dict({'apple': 'manzana', 'banana': 'plátano', 'cherry': 'cereza'})
    >>> result == {'manzana': 'apple', 'plátano': 'banana', 'cereza': 'cherry'} 
    True
    >>> invert_dict(result) == {'apple': 'manzana', 'banana': 'plátano', 'cherry': 'cereza'}
    True
    >>> replacements = {"S":"Z", "E":"U", "T":"P", "A":"M"}
    >>> substitute_chars("ZUCRUP MUZZMGU", invert_dict(replacements))
    'SECRET AESSAGE'
    """
    orig_keys = list(original.keys())
    orig_values = list(original.values())

    new_keys = []
    for i in range(0, len(orig_values)): 
        if not orig_values[i] in new_keys: 
            new_keys.append(orig_values[i])
    for i in range(0, len(new_keys)):
         original.pop(orig_keys[i])

         original.update({new_keys[i]: orig_keys[i]})

    return original 


# print(invert_dict({'apple': 'manzana', 'banana': 'plátano', 'cherry': 'cereza'}))


# Exercise 4
def find_contact_by_name(contacts, name) -> tuple:
    """
    Returns the contact information (name, phone number, and email address) 
    for the given name in a flat tuple structure. If the contact is not found, 
    return None.

    Parameters:
    - contacts (list): A list of nested tuples
    - name (str): The name of the contact which is the first item of each tuple.

    Returns:
    - tuple: The contact information of a single contact as an unnested tuple.

    Examples:
    >>> find_contact_by_name([], "Victoria Phelps")
    None
    >>> contacts =  [("John Doe", ("123-456-7890", "john.doe@example.com")), ("Jane Smith", ("987-654-3210", "jane.smith@example.com")), ("Victoria Phelps", ("555-123-4567", "victoria.phelps@example.com"))]
    >>> find_contact_by_name(contacts, "Victoria Phelps")
    ('Victoria Phelps', '555-123-4567', 'victoria.phelps@example.com')
    >>> find_contact_by_name(contacts, "Andrew Rothman")
    None
    >>> find_contact_by_name(contacts, "Victoria")
    None
    >>> new_contacts = [("Alonzo", ("111-111-1111", "alonzo@example.com"))]
    >>> find_contact_by_name(new_contacts, "Alonzo")
    ('Alonzo', '111-111-1111', 'alonzo@example.com')
    >>> find_contact_by_name(new_contacts, "Victoria Phelps")
    None
    """

    
    for i in range(0, len(contacts)): 
        if contacts[i][0] == name:
            info = []
            for j in range(0, len(contacts[i][1])):
                info.append(contacts[i][1][j])
            return (name, info[0], info[1])
    names = []
    for i in range(0, len(contacts)):
        names.append(contacts[i][0]) 
    if not name in names: 
        return None

print(find_contact_by_name([("John Doe", ("123-456-7890", "john.doe@example.com")), ("Jane Smith", ("987-654-3210", "jane.smith@example.com")), ("Victoria Phelps", ("555-123-4567", "victoria.phelps@example.com"))], "Jane"))