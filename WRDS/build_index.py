import re
import fileinput
import sys
import json


def process_line_regex(line, regex):
    """Process a flat file line and returns matches with the input regex
    
    Arguments:
        line {string} -- input line from flat file
        regex {compiled regex} -- input compiled regex to search against
    
    Returns:
        {string} -- string matching regex
    """

    return regex.match(line).group()

def process_line_cols(line, col_indexes, delimiter=r'|'):
    """Processes a flat file line and returns an index string

    Index string created by concatenating the contents of each column with the input delimiter
    
    Args:
        line (string): input line from flat file 
        col_indexes (list of ints): integer indexes of columns to use to create the index
        delimiter (char, optional): Defaults to r'|'. delimiter used to join the different columns of the index
    
    Returns:
        [str]: [index string created by joining various indexes]
    """

    cols = line.split(delimiter)
    current_index = map(lambda index: cols[index], col_indexes)
    return delimiter.join(current_index)

def process_header(line, col_names_to_index, delimiter=r'|'):
    """Gets the index numbers of the columns to be used to index the files. 
    
    Args:
        line (string): input line from flat file 
        col_names_to_index (list): List of column names to use to create the index
        delimiter (char, optional): Defaults to r'|'. delimiter used to join the different columns of the index
    
    Returns:
        [list of ints]: index numbers of the columns to be used to index the files
    """

    cols = line.split(delimiter)
    col_indexes = []
    for col in col_names_to_index:
        col_indexes.append(cols.index(col))
    col_indexes = list(map(lambda col: cols.index(col), col_names_to_index))
    return col_indexes


def process_file(input_filename, col_names_to_index=[], delimiter=r'|',json_flag=False, bigger_output=False):
    
    json_dict = {}

    with open(input_filename) as infile:

        if not json_flag:
            sys.stdout.write('File: {0}\n'.format(input_filename))
        else:
            json_dict['file_pointer'] = input_filename

        first_line=True
        prev_byte_offset = ''
        regex = re.compile(r"\d+\|\d+|")

        for line in iter(infile.readline, ''):
            
            current_byte_offset = infile.tell()
            
            if first_line:
                first_line = False
                if col_names_to_index:
                    col_indexes = process_header(line, col_names_to_index, delimiter)

            else:
                if col_names_to_index:
                    current_index = process_line_cols(line,col_indexes, delimiter='|')
                else:
                    current_index = process_line_regex(line, regex)
                    
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
            
    return json_dict


def main(args):

    json_flag = False
    bigger_output = False
    index_by_col_names = False

    if len(args) >= 1:
        if len([s for s in args if '-j' in s]) > 0:
            json_flag=True
            args = [s for s in args if '-j' not in s]
        if len([s for s in args if '-b' in s]) > 0:
            bigger_output = True
            args = [s for s in args if '-b' not in s]
        if len([s for s in args if '-c' in s]) > 0:
            index_by_col_names=True
            args = [s for s in args if '-c' not in s]
        if len([s for s in args if '-h' in s]) > 0:
            print("""Use the -j flag to output a json representation of the index.
                     Use the -b flag to output a slightly larger representation of the index
                            containing also the number of bytes in each line
                     Required inputs: filename of index to produce
                     Outputs: json / index file to stdout. Remember to pipe this into a file!
                     Output Index Format:
                     <current_index> <start_byte_offset> <no_of_bytes_in_line>

                     eg: 
                     001011|1986 515572 2447
                     001011|1986 518019 1146
                     
                     """)

    if not args:
        args=[]
        args.append('test.txt')

    if len(args) > 1 and not index_by_col_names:
        raise OSError('Too many / too few arguments! usage: specify a filename to parse ')
    
    if index_by_col_names:
        json_dict = process_file(args[0], json_flag=json_flag, bigger_output=bigger_output, col_names_to_index=args[1:])
    else:
            json_dict = process_file(args[0], json_flag=json_flag, bigger_output=bigger_output, col_names_to_index=[])

    sys.stdout.write(json.dumps(json_dict))            

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))