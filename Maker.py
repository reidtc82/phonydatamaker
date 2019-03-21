"""
 Author: Reid Case
 Date: 3/19/19

 Just needed some practice data that wasnt from real people to test some ideas for
 customer bank clustering and product predictions.
"""

import pandas as pd
import numpy as np
import random
try:
    set
except NameError:
    from sets import Set as set

class Maker:
    def __init__(self, maxacct):
        self.used = set()
        self.cols = ['acct','credit_score','debt_income', 'profitability', 'total_bals_dep','total_bals_ln']
        for i in range(1,101):
            self.cols.append('week{0}'.format(i))
        self.df = pd.DataFrame(data=[self.get_data()], columns=self.cols)
        self.maxacct = maxacct

    def make_data(self):
        while len(self.df['acct']) < self.maxacct:
            newrow = pd.DataFrame(data=[self.get_data()], columns=self.cols)
            self.df = self.df.append(newrow, ignore_index=True)

        self.df.to_csv('../phonydatamaker/phonydata.csv', encoding='utf-8', index=False)

    def get_products(self, ret):

        for i in range(100):
            chance = random.random()
            if chance < 0.9:
                ret.append(0)
            else:
                ret.append(random.randint(1,100))

        return ret

    def get_data(self):
        ret = []
        shbal = int(np.random.normal(-25,50000000,None))/100
        while shbal < 0:
            shbal = int(np.random.normal(-25,50000000,None))/100

        lnbal = int(np.random.normal(2500000,5000000,None))/100
        if lnbal < 0:
            lnbal = 0

        accnum = random.randint(1,999999)
        while accnum in self.used:
            accnum = random.randint(1,999999)

        self.used.add(accnum)

        ret = [accnum, int(random.triangular(330,830,687)), int(random.triangular(1,80,40))/100, int(random.triangular(-50000,1000000,50000))/100, shbal, lnbal]
        ret = self.get_products(ret)

        return ret

mk = Maker(50000)
mk.make_data()
