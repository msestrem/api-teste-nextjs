import pandas as pd
import glob

path = r'c:/repos/linkyou/Scripts/Tests/csv'  
all_files = glob.glob(path + "*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, encondig = "UTF-8")
    li.append(df)

frame_df = pd.concat(li, axis=0, ignore_index=True)

total_rows = frame_df.shape[0]

for x in range(0, total_rows):
    final_df = frame_df.iloc[x]
    print(final_df.to_string(index=True))
    print()
frame.info()
print()