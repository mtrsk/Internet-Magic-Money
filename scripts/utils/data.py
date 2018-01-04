import os
import pickle
from datetime import datetime

import quandl


def get_quandl_data(quandl_id, data_path):
    '''
        Gets data from Quandl API.
    '''
    now = datetime.now()
    filename = '{}-{}-{}-{}.pkl'.format(
        quandl_id.replace('/', '-'), now.year, now.month, now.day)
    path = os.path.join(data_path, filename)
    print(path)
    try:
        f = open(path, 'rb')
        df = pickle.load(f)
    except (IOError, OSError):
        df = quandl.get(quandl_id, returns='pandas')
        # pickles df so it doesnt have to download
        # data from the same day again.
        df.to_pickle(path)
    return df


def format_quandl_data(market, curr):
    '''
        returns BCHARTS/{MARKET}{CURRENCY}
    '''
    return "BCHARTS/{0}{1}".format(market.upper(), curr.upper())
