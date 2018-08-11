import json
import os, sys
import pandas as pd
import datetime

def load_index(input_filename):
    with open(input_filename) as infile:
        return json.loads(infile.read())

def get_from_file_as_df(index,search_indices, delimiter=r'|'):
    
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
        try:
            infile.seek(byte_offset,0)
            output_dict.append(infile.readline().strip().split(delimiter) )
        except TypeError:
            infile.seek(byte_offset[0],0)
            output_dict.append(infile.read(byte_offset[1]).strip().split(delimiter))
        
    
    return pd.DataFrame(data = output_dict, columns= cols.split(delimiter))


def main(args):

    indexes = {}

    if not args:
        args = ['bank_funda_index.json']

    for input_filename in args:
        indexes[os.path.splitext(input_filename)[0]] = load_index(input_filename)

    df = get_from_file_as_df(indexes['bank_funda_index'],['001178|19741231','001178|19771231','001178|19761231','001178|19851231'])

    for index in indexes.values():
        time_index = build_date_time_index_representation(index)

def build_date_time_index_representation(index, delimiter=r'|'):
    output_dict = {}
    for item in index.keys():
        if 'file_pointer' not in item:
            current_date = datetime.datetime.strptime(item.split(delimiter)[1] , '%Y%m%d')

            if current_date in output_dict:
                output_dict[current_date].append(item)
            else:
                output_dict[current_date] = [item]
    return output_dict

def get_query_from_time(time_indexes,start_date, end_date):
    # produce list of times
    no_days = end_date - start_date
    dates = [start_date + datetime.timedelta(day) for day in range(no_days.days)]
    
    output_list = []

    for date in dates:
        print(time_indexes.get(date,[]))

        output_list.extend(time_indexes.get(date,[]))

    return output_list

if __name__ == '__main__':
    
    indexes = {}

    if not sys.argv[1:]:
        args = ['bank_funda_index.json']

    for input_filename in args:
        indexes[os.path.splitext(input_filename)[0]] = load_index(input_filename)

    df = get_from_file_as_df(indexes['bank_funda_index'],['001178|19741231','001178|19771231','001178|19761231','001178|19851231'])

    for index in indexes.values():
        time_index = build_date_time_index_representation(index)#
        
    get_query_from_time(time_index,datetime.date(1960,12,31),datetime.date(1970,12,31))
    
    #sys.exit(main(sys.argv[1:]))