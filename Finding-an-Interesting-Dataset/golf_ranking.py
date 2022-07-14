import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

golf_ranking = pandas.read_csv("OWGR_Ranking.csv")

print(golf_ranking)