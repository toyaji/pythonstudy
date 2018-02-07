import pandas as pd

df = pd.read_csv('./LQ.csv')

def ranktrim(df):
    tf = df.groupby(['year', 'crop']).sum().reset_index()

    db = {}
    cums = {}
    for y in tf.year.unique().tolist():
         tt = tf[tf.year == y].sort_values(['area'], ascending=False)
         tt['cumulative_area'] = tt.area.cumsum() / tt.area.sum()
         db[y] = tt.crop[:10].values
         cums[y] = tt.cumulative_area[:10].values

    top10 = pd.DataFrame(db)
    cum10 = pd.DataFrame(cums)
    return (top10, cum10)