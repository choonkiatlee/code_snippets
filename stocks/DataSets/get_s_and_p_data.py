#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 19:05:54 2018

@author: ckl41
"""

import datapackage as dp

import pandas as pd

class s_and_p_symbols:
    url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

    def get_s_and_p_symbols(self):
    
        package = dp.Package(self.url)
    
        # print list of all resources:
        print(package.resource_names)
        
        storage_dict = self.convert_to_dfs(package)
        
        df = storage_dict['constituents']
        
        return df['Symbol'].drop_duplicates()

    def convert_to_dfs(self,package):
            
        storage_dict= {}
        
        # print processed tabular data (if exists any)
        for resource in package.resources:
            if resource.tabular:        
                storage_dict[resource.name] = pd.read_csv(resource.descriptor['path'])
                
        return storage_dict
    
if __name__ == "__main__":
    sp = s_and_p_symbols()
    package = dp.Package(sp.url)
    storage_dict = sp.convert_to_dfs(package)
    df = storage_dict['constituents']
    df.to_csv('s_and_p_500_companies_list.csv')