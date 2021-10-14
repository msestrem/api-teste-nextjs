import os
import pandas as pd
import glob
import csv
from datetime import datetime, timedelta

path = r'c:/repos/linkyou/Scripts/Tests/csv' 
#path = r'/Users/Sestrem/Library/Mobile Documents/com~apple~CloudDocs/Linkyou/Scripts/Tests/csv'
#path = '/root/linkyou/_work/linkyou/linkyou/Scripts/Tests/csv'                
all_files = glob.glob(os.path.join(path, "*.csv")) 
print(all_files)
df_from_each_file = (pd.read_csv(f, skipinitialspace=True, skip_blank_lines=True) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

total_rows = concatenated_df.shape[0]
print(total_rows)
concatenated_df.columns = concatenated_df.columns.astype(str).str.replace(' ', '')

concatenated_df['Numero'] = concatenated_df['Numero'].astype(str).str.replace(' ', '')
concatenated_df['Data'] = concatenated_df['Data'].astype(str).str.replace(' ', '')
concatenated_df['CallID'] = concatenated_df['CallID'].astype(str).str.replace(' ', '')
concatenated_df['Fila'] = concatenated_df['Fila'].astype(str).str.replace(' ', '')
concatenated_df['Atendente'] = concatenated_df['Atendente'].astype(str).str.replace(' ', '')
concatenated_df['Espera'] = concatenated_df['Espera'].astype(str).str.replace(' ', '')
concatenated_df['Duracao'] = concatenated_df['Duracao'].astype(str).str.replace(' ', '')

#for x in range(0, total_rows):
    #final_df = concatenated_df.iloc[x]
    #print()
    #print(final_df.to_string(index=True))
    #print()
#print(concatenated_df['Numero'].values)


for index, row in concatenated_df.iterrows():
    if '11959179073' in row['Numero']:
        print(row['Atendente'])

count = '11959179073' in concatenated_df['Numero'].values

print(count)