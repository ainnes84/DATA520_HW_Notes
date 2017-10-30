def process_file(file, out_file):
    with open(file, 'r') as read_file:
        with open(out_file, 'w') as write_file:
            first_line = '"HSpecNo","GOL","NOL","BNL","XCB","M9","XFB","M11","AUB","ASB","BBH","M26","M27","M28","FRC","PAC","OCC","BPL","M43","ZYB","M46","NPH","DKB","M51","OBH","OBH","NLB","NLH","M55","MAB","MDH","MDB","U1","U2","U3","U4","U5","U6","U7","U8","U9","U10","U11","WNB","SIS","U12","ZMB","U13","U14"'
            write_file.write(first_line + '\n')
            line = read_file.readline().strip()
            write_line = '{0}'.format(line)
            write_file.write(write_line)
            for line in read_file:
                line = line.strip()
                if 'Specimen' not in line:
                    line = line.replace(' ', ',')
                    write_line = '{0},'.format(line)
                    write_file.write(write_line)
                else:
                    write_line = '\n{0},'.format(line)
                    write_file.write(write_line)

if __name__ == '__main__':
    process_file('Hanihara.txt', 'hanihara.csv')
