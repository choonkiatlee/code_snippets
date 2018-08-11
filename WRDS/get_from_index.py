import json
import os, sys
import pandas as pd
from datetime import datetime

def load_index(input_filename):
    with open(input_filename) as infile:
        return json.loads(infile.read())

def get_from_file_as_df(index,search_indices):
    
    # assemble list of indices
    index_mapping_list = []
    for search_index in search_indices:
        index_mapping_list.append(index[search_index])
    index_mapping_list.sort()

    # open input file
    infile = open(index['file_pointer'],'r')
    cols = infile.readline().strip() # cols list is usually the 1st line

    output_dict = []
    for byte_offset in index_mapping_list:
        infile.seek(byte_offset,0)
        output_dict.append(infile.readline().strip().split('|') )
    
    return pd.DataFrame(data = output_dict, columns= cols.split('|'))


def main(args):

    indexes = {}

    for input_filename in args:
        indexes[os.path.splitext(input_filename)[0]] = load_index(input_filename)

    df = get_from_file_as_df(indexes['test'],['001000|19611231','001000|19621231','001000|19631231','001000|19641231'])

    print((df))

    time_index = build_date_time_index_representation(df)




def build_date_time_index_representation(index):
    output_dict = {}
    for item in index.keys():
        print(item)
        try:
            current_date = datetime.strptime(item.split('|')[1] , '%Y%m%d')
        except IndexError:
            print(item.split('|'))
            raise IndexError
        if current_date in output_dict:
            output_dict[current_date].append(item)
        else:
            output_dict[current_date] = [item]
    return output_dict

def get_query_from_time(time_indexes,start_date, end_date):
    # produce list of times
    no_days = end_date - start_date
    dates = [start_date + datetime.time_delta(day) for day in range(no_days)]

    output_list = []

    for date in dates:
        output_list.extend(time_indexes[date])

    return output_list

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))