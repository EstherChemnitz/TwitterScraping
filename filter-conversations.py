# Filter out conversations with #covid19dk

import pandas as pd

c19 = pd.read_csv("covid_tweets.csv")
all = pd.read_csv("all_tweets.csv")
print(len(c19))
print(len(all))

# Get all the unique "conversation_ids" in the tweets with #covid19dk

con_ids = c19["conversation_id"].unique()
print(len(con_ids))


from tqdm import tqdm
con_dfs = []

for con_id in tqdm(con_ids):
    df = all.loc[all["conversation_id"] == con_id]
    if len(df) > 0:
        con_dfs.append((len(df), df))


# Save a backup
import pickle

pickle.dump(con_dfs, open("con_dfs.pickle","wb"))



# Sorting the list by conversation length
print(con_dfs[0][0])
con_dfs.sort(reverse=True, key=lambda t: t[0])
print(con_dfs[0][0])


# Collect in one big data-frame and dump to csv

all_cons = pd.DataFrame()
for l,df in tqdm(con_dfs):
    df.sort_values("created_at", inplace=True)
    empty = pd.DataFrame([[None]*len(df.columns)]*3, columns=df.columns)
    all_cons = pd.concat((all_cons,df,empty), join="outer")
    
all_cons.to_csv("covid19-conversations.csv", index=False)


# Do simple statistics on the conversation length

from statistics import median

lens = [t[0] for t in con_dfs] 
avg_len = sum(lens)/len(lens)
med_len = median(lens)
print(f"Conversation length - avg: {round(avg_len,1)}, median: {med_len}, max: {max(lens)}, min: {min(lens)}")
print(f"Sum of tweets in conversations: {sum(lengths)}")



