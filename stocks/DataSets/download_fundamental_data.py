import pandas as pd


def check_or_create_file(file):
    try:
        os.makedirs(os.path.dirname(file))
        return True
    except FileExistsError:
        return False

def save_file_from_request(url,params={},output_filename='test.csv'):
    """
    Get a file from the specified url and save it with output_filename
    
    Args:
        url (str): url to fetch from 
        params (dict, optional): Defaults to {}. 
            Provide query string parameters for requests
        output_filename (str, optional): Defaults to 'test.csv'.
            Save file with this filename
    """

    import shutil
    import requests
    import gc

    response = requests.get(url, params=params,stream=True)
    with open(output_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    gc.collect()


def download_list_of_s_and_p_500_companies(output_filename):
    COMPANIES_URL = 'https://api.usfundamentals.com/v1/companies/xbrl'
    
    companies_params={
        'token':'rsBo2UXqVJdcI9bqeJqwHQ',
        'format':'csv'
    }
    
    save_file_from_request(COMPANIES_URL,params=companies_params,output_filename=output_filename)


def download_indicators(output_file_dir=None, combined_table_filename='combined.csv', split_data=False):

    import os    

    combined_table = pd.read_csv(combined_table_filename,index_col='Symbol')
    
    company_ids = combined_table['company_id'].drop_duplicates().to_dict()
    
    INDICATORS_URL = 'https://api.usfundamentals.com/v1/indicators/xbrl'
    
    if not output_file_dir:
        output_file_dir = os.getcwd()
    
    if split_data:
        counter = 0
        for symbol,company_id in company_ids.items():
            indicators_params={
                    'token'        : 'rsBo2UXqVJdcI9bqeJqwHQ',
                    'frequency'    : 'q',
                    'period_type'  :'end_date',
                    'companies'    : company_id
                    #'companies' : ','.join(company_ids)        
                    }
            
            
            output_filename = os.path.join(output_file_dir,'indicators/{0}_indicators.csv'.format(symbol))
            check_or_create_file(output_filename)
            
            save_file_from_request(INDICATORS_URL,params = indicators_params, output_filename=output_filename)
            
            counter += 1
            print('Completed Downloading Data for {0}% of companies'.format(counter*100 / len(company_ids)))
            
            
    else:
        indicators_params={
                    'token'        : 'rsBo2UXqVJdcI9bqeJqwHQ',
                    'frequency'    : 'q',
                    'period_type'  :'end_date',
                    'companies' : ','.join(company_ids.values())        
                    }
        
        output_filename = os.path.join(output_file_dir,'indicators/indicators.csv')
        check_or_create_file(output_filename)
        save_file_from_request(INDICATORS_URL,params = indicators_params, output_filename=output_filename)

    

if __name__ == '__main__':

    import os
    
    download_list_of_s_and_p_500_companies('test.csv')
    
    download_indicators(output_file_dir = os.path.join(os.getcwd(),'data/'),split_data=True)



