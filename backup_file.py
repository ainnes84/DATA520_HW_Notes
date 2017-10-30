def backup_file(filename,new_file):
    """(orginalfile, newfile, str) -> NoneType
    """
    filename = input('Which file would you like to backup?')
    new_file = filename + '.bak'
    backup = open(new_file, 'w')

    for line in open(filename):
        backup.write(line)

    backup.close()
    
