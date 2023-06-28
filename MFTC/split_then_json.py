import pandas as pd
from sklearn.model_selection import train_test_split
import json

combined_df = pd.read_excel('combined_dataset.xlsx')

label_columns = ['fairness', 'non-moral', 'purity', 'degradation', 'loyalty', 'care', 'cheating', 'betrayal', 'subversion', 'authority', 'harm']

#create separate datasets for each label
for label in label_columns:
    new_df = combined_df[['tweet_id', 'text', label]].copy()
    new_df.rename(columns={label: 'label'}, inplace=True)
    new_df.loc[:, ~new_df.columns.isin(['tweet_id', 'text', 'label'])] = 0

    #split into training and testing sets
    train_df, test_df = train_test_split(new_df, test_size=0.25, random_state=42)

    #save the training + test dataset to json files
    train_file_name = f'C:/Users/micha/Downloads/{label}_train.json'
    train_data = []
    for index, row in train_df.iterrows():
        row_data = {}
        row_data["label"] = str(row["label"])
        row_data["source"] = str(row["text"])
        train_data.append(row_data)
    with open(train_file_name, "w") as f:
        for entry in train_data:
            f.write(json.dumps(entry) + "\n")

    test_file_name = f'C:/Users/micha/Downloads/{label}_test.json'
    test_data = []
    for index, row in test_df.iterrows():
        row_data = {}
        row_data["label"] = str(row["label"])
        row_data["source"] = str(row["text"])
        test_data.append(row_data)
    with open(test_file_name, "w") as f:
        for entry in test_data:
            f.write(json.dumps(entry) + "\n")

