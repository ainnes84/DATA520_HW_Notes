import os.path
def file_editor(writefile):

    while os.path.isfile(writefile):
        rename = input('The file exists. Do you want to rename the file? (y/n)')
        if rename == 'y':
            print ('I will rename the ' + writefile + ' file.')
            filename = input('Please give new file name (In .txt format)')
            new_file = filename + '.txt'
            rename_file = open(new_file,'w')
            for line in open (writefile):
                rename_file.write(line)
            rename_file.close()
            print ('Renaming file')
            break
        elif rename == 'n':
            overwrite = input('Will not rename file. Would you like to overwrite the file? (y/n)')
            if overwrite == 'y':
                print ('I will overwrite the ' + writefile + ' file.')
                with open(writefile, 'w') as file:
                    new_file = input ('Enter info to overwrite the file.')
                    file.write(new_file)
                    print ('Overwritting file')
                break
            elif overwrite == 'n':
                cancel = input('Would you like to cancel? (y/n)')
                if cancel == 'y':
                    print('I will cancel file editor!')
                    break
                elif cancel == 'n':
                    print ('You chose not to cancel. Restarting program.')
                    continue
                else:
                    print ('Invalid key pressed')
                    continue

            print ('Writing over file')

        else:
            print ('Invalid Key Pressed')
            continue


if __name__=='__main__':
    file_editor('file_example.txt')
            
                
