import pandas as pd

df = pd.read_csv('Top 50 Youtube Channels.csv')



def func(col: pd.Series):
    '''
    here you get a Series of all the elements as a 
    '''
    # print(type(col))
    # print(col.name)
    # print(col)
    col = col.apply(lambda v: str(v).split(' ')[0])
    return col

cols = ['Network', 'Channel name']
df.loc[:, cols] = df.loc[:, cols].apply(func)

