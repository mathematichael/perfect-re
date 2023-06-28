import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('combined_dataset.csv')

#ONE HOT ENCODING
#we combine the class columns from the third onwards into a single class column
df["OneHotLabels"] = df.iloc[:, 2:].astype(str).apply(' '.join, axis=1)

#have to assign these unique labels to an integer system
df["OneHotInts"] = df['OneHotLabels'].astype('category').cat.codes

#train test 70:30 split
train, test = train_test_split(df, test_size=0.3, random_state=42)

#convert to json using pandas
train[['OneHotInts', 'text']].rename(columns={'OneHotInts': 'label', 'text': 'source'}) \
    .to_json("train.jsonl", orient='records', lines=True)
test[['classLabels', 'text']].rename(columns={'classLabels': 'label', 'text': 'source'}) \
    .to_json("test.jsonl", orient='records', lines=True)

#create verbalizers to assign meaning to our integer classifications
df["verbalizers"] = df.iloc[:, 2:13].apply(
    lambda row: ','.join([col for col, val in zip(df.columns[2:13], row) if val]), axis=1)

df = df.sort_values(by="OneHotInts")

#the following will print the verbalizers as a list, which you can then copy and paste into a txt document for the verablizers file.
#automating this part isnt easy since you cant save a python list into a text file. easy fix!
#ours was saved as "onehot_verbalizers" and you can find it in the utils folder.
df["verbalizers"].unique()

