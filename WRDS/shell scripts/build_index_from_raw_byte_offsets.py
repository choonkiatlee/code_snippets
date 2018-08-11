import fileinput
import sys
import re

def get_byte_offset(line):
    index = line.index(':')
    return line[:index], line[index+1:]

def main(args):

    current_filename=None
    is_not_first_line=False
    prev_byte_offset=''
    prev_index=''
    
    for input_line in fileinput.input():
        if fileinput.filename != current_filename:
            current_filename = fileinput.filename
            is_not_first_line=True
            prev_byte_offset, prev_index = get_byte_offset(input_line)
        if is_not_first_line:
            current_byte_offset, current_index = get_byte_offset(input_line)
            sys.stdout.write('{0} {1} {2}'.format(prev_index,prev_byte_offset,(int(current_byte_offset)-int(prev_byte_offset))))
            prev_byte_offset,prev_index = current_byte_offset, current_index
    else:
        sys.stdout.write('{0} {1}'.format(prev_index,prev_byte_offset))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))