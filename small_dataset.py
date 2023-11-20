import pandas as pd

df = pd.read_csv(r'emails.csv')
df = df.iloc[:10]
df.to_csv('small_emails.csv')
print('Done')
