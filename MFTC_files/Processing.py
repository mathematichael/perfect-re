import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('combined_dataset.csv')

#ONE HOT ENCODING
#we combine the class columns from the third onwards into a single class column
df["onehot"] = df.iloc[:, 2:].astype(str).apply(' '.join, axis=1)

#have to assign these unique labels to an integer system
df["classlab"] = df['onehot'].astype('category').cat.codes

#train test 70:30 split
train, test = train_test_split(df, test_size=0.3, random_state=42)

#convert to json using pandas
train[['classlab', 'text']].rename(columns={'classlab': 'label', 'text': 'source'}) \
    .to_json("train.json", orient='records', lines=True)
test[['classlab', 'text']].rename(columns={'classlab': 'label', 'text': 'source'}) \
    .to_json("test.json", orient='records', lines=True)

#create verbalizers to assign meaning to our integer classifications
df["verbalizers"] = df.iloc[:, 2:13].apply(
    lambda row: ','.join([col for col, val in zip(df.columns[2:13], row) if val]), axis=1)

df = df.sort_values(by="classlab")

#the following will print the verbalizers as a list, which you can then copy and paste into a txt document for the verablizers file.
#automating this part isnt easy since you cant save a python list into a text file. easy fix!
#ours was saved as "onehot_verbalized" and you can find it in the fewshot folder.
df["verbalizers"].unique()

