def complement(sequence):
    """ (str) -> str

    Return the complement of the given sequence.

    >>> complement('ACTCGCTTCGCTATAAGCTAGGCAT')
    'TGAGCAAGCGATATTCGATCCGTA'
    """

    # Create a dictionary of the letters in the sequence.
    sequence_dict = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
    # Get the complement of the sequence inputed by the user.
    complement = ''

    # Use a for loop that reads the complement given and adds it to
    # the original dictionary.
    for letter in sequence:
        complement = complement + sequence_dict[letter]
        
    # Finally return the new sequence with the complemented letters.
    return complement
    
