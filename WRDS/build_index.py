import re
import fileinput
import sys
import json


def process_line(line, regex):
    return regex.match(line).group()


def main(args):

    json_flag = False
    json_dict = {}
    bigger_output = False

    if len(args) > 1:
        if len([s for s in args if '-j' in s]) > 0:
            json_flag=True
            args = [s for s in args if '-j' not in s]
        if len([s for s in args if '-b' in s]) > 0:
            bigger_output = True
            args = [s for s in args if '-b' not in s]

    if not args or len(args) > 1:
        raise OSError('Too many / too few arguments! usage: specify a filename to parse ')

    regex = re.compile(r"\d+\|\d+|")

    with open(args[0]) as infile:

        if not json_flag:
            sys.stdout.write('File: {0}'.format(args[0]))
        else:
            json_dict['file_pointer'] = args[0]

        first_line=True
        prev_byte_offset = ''
        prev_index = ''
        for line in iter(infile.readline, ''):
            
            current_index = process_line(line, regex)
            current_byte_offset = infile.tell()

            if first_line:
                first_line = False
            else:
                if current_index:
                    if not json_flag:
                        if bigger_output:
                            sys.stdout.write( '{0} {1} {2}\n'.format(current_index, prev_byte_offset, int(current_byte_offset) - int(prev_byte_offset)) )
                        else:
                            sys.stdout.write( '{0} {1}\n'.format(current_index, prev_byte_offset))
                    else:
                        if bigger_output:
                            json_dict[current_index] = (prev_byte_offset,int(current_byte_offset) - int(prev_byte_offset))
                        else:
                            json_dict[current_index] = prev_byte_offset


            prev_byte_offset = current_byte_offset
            prev_index = current_index

        
        sys.stdout.write(json.dumps(json_dict))            

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))