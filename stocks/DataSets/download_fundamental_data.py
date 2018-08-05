
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

    response = requests.get(COMPANIES_URL, params=params,stream=True)
    with open(output_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    gc.collect()


COMPANIES_URL = 'https://api.usfundamentals.com/v1/companies/xbrl'

params={
    'token':'rsBo2UXqVJdcI9bqeJqwHQ',
    'format':'csv'
}

save_file_from_request(COMPANIES_URL,params=params)



