

TABLE = 'USStockInfo'

import pandas as pd
import os, sys
import platform
if 'Windows' in platform.platform():
    PATH = "\\".join( os.path.abspath(__file__).split('\\')[:-1])
else:
    PATH = "/".join( os.path.abspath(__file__).split('/')[:-1])
sys.path.append(PATH)
from BasedClass import query

class ClassUSStockInfo:
    def __init__(self):
        pass

    def load_all(self,status = 'package'):
        colname = query( 'SHOW COLUMNS FROM {}'.format( TABLE ) )
        colname = [ c[0] for c in colname if c[0] not in  ['id','url'] ]     
        colname.remove('date')
        sql = 'select `{}` from {}'.format( '`,`'.join( colname ) ,TABLE)
        tem = query(sql)
        data = pd.DataFrame( list(tem) )
        data.columns = colname
        '''
        if status == 'package':
            sql = 'SELECT DISTINCT stock_id FROM `USStockPrice`'
            tem = query(sql)
            stock_id = [ te[0] for te in tem ]
            bo = [ True if x in stock_id else False for x in data['stock_id'] ]
            data = data[bo]
            data.index = range(len(data))
        '''
        return data

def USStockInfo(select = [],date = '',status = 'package'):
    
    self = ClassUSStockInfo()  
    data = self.load_all(status)
        
    return data


