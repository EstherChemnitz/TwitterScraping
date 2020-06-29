# Lets group all the csvs together to two big dataframes

import pandas as pd
from collections import defaultdict
import os

pms = os.listdir("pressemoeder")

df = pd.DataFrame()

for pm in pms:
    print(pm)
    df_aux = pd.read_csv(f"pressemoeder/{pm}/tweets.csv")
    df = pd.concat((df,df_aux), join="outer")
    
covid_tweets = df


ats = os.listdir("all-tweets")

df = pd.DataFrame()

for at in ats:
    print(at)
    df_aux = pd.read_csv(f"all-tweets/{at}/tweets.csv")
    df = pd.concat((df,df_aux), join="outer")
    
all_tweets = df

# Let's dump these two to csv's

covid_tweets.to_csv("covid_tweets.csv")
all_tweets.to_csv("all_tweets.csv")




