import pandas as pd

db = pd.read_csv('database.csv',encoding='latin-1')

word = input("Enter a word: ")

print(db[db.isin([word]).any(axis=1)])

english = db[db.isin([word]).any(axis=1)]['English'].iloc[0]
cree = db[db.isin([word]).any(axis=1)]['Cree'].iloc[0]
ojib = db[db.isin([word]).any(axis=1)]['Ojibwe'].iloc[0]
mont = db[db.isin([word]).any(axis=1)]['Montagnais'].iloc[0]

print(english, cree, ojib, mont)

# update main python file to read from csv and get values - may not need translate.py