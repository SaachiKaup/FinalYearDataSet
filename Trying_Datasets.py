import pandas as pd
from datasets import Dataset

# Assuming you have your data in a Pandas dataframe 'df'
df = pd.read_csv("Reccomend_train_final.csv")

dataset = Dataset.from_pandas(df)


# Access data using dataset['column_name']
print(dataset["after_merge"])