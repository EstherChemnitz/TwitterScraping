# TwitterScraping
Scripts for scraping twitter for #covid19dk conversations.

__Data selection process:__

We use 'twint', an unofficial python library that scrapes the twitter website, bypassing the 7-day restriction on historical tweets imposed by the official twitter API.
We are interested in the conversations happening on twitter, but neither twint nor the official Twitter allows the user to query directly for tweets and their replies. 
To mediate this short-coming, the data collection is split into two fases:
    - First we query all tweets that contain the hashtag "#covid19dk" (case-insensitive) and has a minimum of each reply posted since the start of each press conference in statsministeriet until midnight that same day. These queries fetched a total of 879 tweets.
    - Second, in order to collect the conversational context around the tweets using the hashtag, we query all tweets that are written in danish in the time period from press conference start till midnight. The extra languge constraint is a pragmatic way to limit the amount of tweets we need to fetch. These queries fetched a total of 362,053 tweets.
    
From each #covid19dk tweet we extract the "conversation_id", and query our large collection of danish tweets for posts with the same conversational id. The result of this filtering is 669 twitter conversations.
We sort all conversations by length descending, and for each infididual conversations, we sort them by time of tweet.

Conversation length statistics: 
avg: 5.2, median: 3, max: 66, min: 1

Sum of tweets in conversations: 3484
