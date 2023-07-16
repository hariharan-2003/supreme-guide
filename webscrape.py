pip install git+https://github.com/JustAnotherArchivist/snscrape.git
import snscrape.modules.twitter as sntwt
import pandas as pd
from datetime import datetime
from tqdm.notebook import tqdm

start_time = datetime.now()

q1 = "(#namo OR #modi OR #narendramodi OR #bjp OR " \
     "#bjp4nation OR #modi2.0 OR #ModiMatBanao OR #chowkidaar "

q2 = "OR #chowkidaarchorhai OR #PhirEkBaarModiSarkar " \
     "OR #ModiOnceMore OR #MainBhiChowkidar "

q3 = "OR #ModiHaiToMumkinHai OR #NaMoAgain OR #ModiMustResign " \
     "OR #KamalKaPhoolBadiBhool "

q4 = "OR #GoBackModi OR #ModiFail OR #ModiMadeDisaster " \
     "OR #ModiFailsEconomy OR #ModiLies "

q5 = "OR #ChowkidarChorHai) until:2019-05-31 " \
     "since:2019-05-21 -filter:links -filter:replies"

query1 = q1 + q2 + q5
query2 = q3 + q4 + q5
query_list = [query1, query2]

tweets = []
limit = 20000
cnt = 0

for query in query_list:
    cnt = 0 # reset counter
    try:
        for tweet in tqdm(sntwt.TwitterSearchScraper(query).get_items()):
            cnt += 1
            if(cnt == limit+1):
                cnt = 0
                break
            else:
                tweets.append([tweet.date, 
                               tweet.lang,
                               tweet.rawContent])
    except Exception as e:
        print(f"Exception occurred: {e}")
        continue

df = pd.DataFrame(tweets, columns=['Date', 'Language', 'Content'])
df.to_csv('C:/Desktop/namonamo.csv', index=False, encoding='utf-8')

end_time = datetime.now()
print(f'Duration: {end_time - start_time}')
#
import snscrape.modules.twitter as sntwt
import pandas as pd
from datetime import datetime
from tqdm.notebook import tqdm

# scraping tweets posted by handle @RahulGandhi on twitter
# tweets containing hashtags related to RG
start_time = datetime.now()
q1 = "(#raga OR #rahulgandhi OR #rahul OR #inc OR #gandhi OR #rahulgandhi OR #rahulgandhimemes OR #rahulgandhiforpm OR #Gandhi "
q2 = "OR #rahulgandhi2019 OR #rahulgandhijokes OR #rahulgandhitrolled OR #rahulgandhiofficial OR #rahulgandhimeme OR #rahulgandhitroll "
q3 = "OR #rahulgandhifunny OR #rahulgandhiji OR #rahulgandhinextpm OR #rahulgandhifans OR #rahulgandhiinbahrain OR #rahulgandhiinuae "
q4 = "(#rahulgandhizindabad OR #accordingtorahulgandhi OR #rahulgandhitrolls OR #rahulgandhifor OR #shameonrahulgandhi "
q5 = "OR #rahulgandhi_inc OR #rahulgandhinews OR #rahulgandhipappu OR #rahulgandhiinjabalpur OR #rajwelcomesrahulgandhi "
q6 = "OR #rahulgandhicongresspresident OR #rahulgandhispeech OR #rahulgandhiinlondon OR #rahulgandhicomedy OR #rahulgandhiingwalior "
q7 = "(#rahulgandhiwithhal OR #telanganawithrahulgandhi OR #rahulgandhirohitkhanna OR #rahulgandhifunnyvideos "
q8 = "OR #rohitandrahulgandhi OR #rahulgandhifunnyspeech OR #rahulgandhispeeches OR #modivsrahulgandhi OR #rohitansrahulgandhi "
q9 = "OR #rahulgandhiâ) until:2019-05-31 since:2019-03-21 -filter:links -filter:replies"
query1 = q1 + q2 + q3 + q9
query2 = q4 + q5 + q6 + q9
query_list = [query1, query2]
tweets = []
limit = 20000
cnt = 0
for query in query_list:
    for tweet in tqdm(sntwt.TwitterSearchScraper(query).get_items()):
        cnt += 1
        if cnt == limit + 1:
            cnt = 0
            break
        else:
            tweets.append([tweet.date, tweet.lang, tweet.rawContent])
df = pd.DataFrame(tweets, columns=['Date', 'Language', 'Content'])
df.to_csv('C:\\Desktop\\ragaraga.csv', index=False, encoding='utf-8')

end_time = datetime.now()
print(f'Duration: {end_time - start_time}')