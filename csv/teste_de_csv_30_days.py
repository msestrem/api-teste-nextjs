from datetime import datetime, timedelta 
import os
import pandas as pd
import glob
import csv
from datetime import datetime, timedelta
from datetime import date
from sys import exit

data_atual = date.today()
x = int(30) # número de dias a contar da data atual para trás

path = r'c:/repos/api-teste-nextjs/csv/csv' 

#path = r'/Users/Sestrem/Library/Mobile Documents/com~apple~CloudDocs/Linkyou/Scripts/Tests/csv'
#path = '/root/linkyou/_work/linkyou/linkyou/Scripts/Tests/csv'                
all_files = glob.glob(os.path.join(path, "*.csv")) 
#print(all_files)
arquivos_recentes = []
for f in all_files:
    f_1 = f.replace('.csv', '')
    f_2 = f_1.replace('c:/repos/api-teste-nextjs/csv/csv', '')
    f_date = datetime.strptime(f_2, '\%Y-%m-%d').date()
    
    if data_atual <= f_date + timedelta(days=x):
        arquivos_recentes.append(f)
        continue 
       
if arquivos_recentes == [ ]:
    print("Não há registros a serem considerados no período entre a data atual até ", x, "dia(s) atrás.")
    print()
    exit()
        
df_from_each_file = (pd.read_csv(f, skipinitialspace=True, skip_blank_lines=True) for f in arquivos_recentes)
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




for index, row in concatenated_df.iterrows():
    if '11959179073' in row['Numero']:
        print(row['Atendente'])

count = '11959179073' in concatenated_df['Numero'].values

print(count)
print()
print()