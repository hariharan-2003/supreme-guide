import pandas as pd
import re
import string

def clean_text(text):
    """
    Utility function to clean text by removing non-English characters, urls, and punctuations.
    """
    # remove urls
    text = re.sub(r"http\S+", "", text)
    
    # remove non-English characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # remove punctuations
    punctuations = string.punctuation.replace("#", "") # remove '#' from the list of punctuations to be removed
    text = text.translate(str.maketrans("", "", punctuations))
    
    # remove other symbols
    text = re.sub(r'[^a-zA-Z0-9@# ]+', '', text)
    
    # remove hindi words in english script
    hindi_words = ['abhi', 'aam', 'aadmi', 'aandolan', 'aarakshan', 'aadhaar', 'achhe', 'adhikar', 'aazadi', 'aayog', 'aayojit', 'ahankar', 'ajadi', 'akhand', 'akhil', 'akhilesh', 'akshar', 'alag', 'aligarh', 'aql', 'arajakta', 'arthvyavastha', 'asangathit', 'asmita', 'atank', 'atankwad', 'atmavishwas', 'avadharna', 'avishkar', 'awas', 'awas-yojana', 'ayodhya', 'azadi', 'baad', 'baatcheet', 'badlaav', 'badlav', 'bahujan', 'bahumat', 'bajpa', 'bali', 'balidan', 'bandook', 'bandookbaaz', 'banjar', 'banwas', 'barbaadi', 'barood', 'batakh', 'bayaan', 'bazaru', 'bebas', 'bemisaal', 'bhagwa', 'bhajapa', 'bhakti', 'bhandaar', 'bharat', 'bhasha', 'bhedbhav', 'bhinnata', 'bhookh', 'bhool', 'bhrashtachar', 'bhukamp', 'bhrasht', 'bhushan', 'bhutiya', 'bijli', 'bikhar', 'bilaspur', 'bin', 'biradari', 'bismil', 'bjp', 'bjym', 'bomb', 'brahman', 'bramh', 'brutality', 'buddhijeevi', 'budhi', 'budhijivi', 'budhiman', 'budhivanta', 'budget', 'bujurg', 'bulaava', 'burai', 'chakra', 'chamatkaar', 'chamcha', 'chamchagiri', 'chamka', 'charitraheen', 'chaukidar', 'chaurahe', 'chetavani', 'chhapaak', 'chheen', 'chunav', 'chunavi', 'chuppi', 'communal', 'congress', 'corona', 'covid', 'dalit', 'dam', 'daridrata', 'daroga', 'darpan', 'das', 'dastavej', 'dattak', 'deewar', 'dehshat', 'dekha', 'democracy', 'dhakkam', 'dhan', 'dhansampada', 'dharmnirpeksh', 'dharma', 'dhokha', 'dhruv', 'dhul', 'dilli', 'diwali', 'doosra', 'draupadi', 'dravya', 'drona', 'drushtikon', 'dukh', 'dushkarm', 'dushman', 'ekta', 'ekatmata', 'etawa', 'faisala', 'faisle', 'fauji', 'feku', 'gaddar', 'gadar', 'gair', 'galti', 'gandagi', 'gandhi', 'garib', 'garibi', 'gaum','accha', 'agar', 'aisa', 'aur', 'bahut', 'dosto', 'hai', 'ho', 'ka', 'kar', 'ke', 'ki', 'ko', 'kyun', 'kyunki', 'me', 'nahi', 'ne', 'nhi', 'ni', 'se', 'to', 'ya', 'ye']
    regex_pattern = '|'.join(map(re.escape, hindi_words))
    text = re.sub(regex_pattern, '', text, flags=re.IGNORECASE)
    
    return text.strip()

# read the csv file into a pandas dataframe
df = pd.read_csv(r"C:/Desktop/raga_crude.csv")

# apply the clean_text function to the 'Content' column
df['Content'] = df['Content'].apply(clean_text)

# save the modified dataframe to a new csv file
df.to_csv(r"C:\Desktop\raga_test.csv", index=False)
#######
import pandas as pd
import re
import string

def clean_text(text):
    """
    Utility function to clean text by removing non-English characters, urls, and punctuations.
    """
    # remove urls
    text = re.sub(r"http\S+", "", text)
    
    # remove non-English characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # remove punctuations
    punctuations = string.punctuation.replace("#", "") # remove '#' from the list of punctuations to be removed
    text = text.translate(str.maketrans("", "", punctuations))
    
    # remove other symbols
    text = re.sub(r'[^a-zA-Z0-9@# ]+', '', text)
    
    # remove hindi words in english script
    hindi_words = ['abhi', 'aam', 'aadmi', 'aandolan', 'aarakshan', 'aadhaar', 'achhe', 'adhikar', 'aazadi', 'aayog', 'aayojit', 'ahankar', 'ajadi', 'akhand', 'akhil', 'akhilesh', 'akshar', 'alag', 'aligarh', 'aql', 'arajakta', 'arthvyavastha', 'asangathit', 'asmita', 'atank', 'atankwad', 'atmavishwas', 'avadharna', 'avishkar', 'awas', 'awas-yojana', 'ayodhya', 'azadi', 'baad', 'baatcheet', 'badlaav', 'badlav', 'bahujan', 'bahumat', 'bajpa', 'bali', 'balidan', 'bandook', 'bandookbaaz', 'banjar', 'banwas', 'barbaadi', 'barood', 'batakh', 'bayaan', 'bazaru', 'bebas', 'bemisaal', 'bhagwa', 'bhajapa', 'bhakti', 'bhandaar', 'bharat', 'bhasha', 'bhedbhav', 'bhinnata', 'bhookh', 'bhool', 'bhrashtachar', 'bhukamp', 'bhrasht', 'bhushan', 'bhutiya', 'bijli', 'bikhar', 'bilaspur', 'bin', 'biradari', 'bismil', 'bjp', 'bjym', 'bomb', 'brahman', 'bramh', 'brutality', 'buddhijeevi', 'budhi', 'budhijivi', 'budhiman', 'budhivanta', 'budget', 'bujurg', 'bulaava', 'burai', 'chakra', 'chamatkaar', 'chamcha', 'chamchagiri', 'chamka', 'charitraheen', 'chaukidar', 'chaurahe', 'chetavani', 'chhapaak', 'chheen', 'chunav', 'chunavi', 'chuppi', 'communal', 'congress', 'corona', 'covid', 'dalit', 'dam', 'daridrata', 'daroga', 'darpan', 'das', 'dastavej', 'dattak', 'deewar', 'dehshat', 'dekha', 'democracy', 'dhakkam', 'dhan', 'dhansampada', 'dharmnirpeksh', 'dharma', 'dhokha', 'dhruv', 'dhul', 'dilli', 'diwali', 'doosra', 'draupadi', 'dravya', 'drona', 'drushtikon', 'dukh', 'dushkarm', 'dushman', 'ekta', 'ekatmata', 'etawa', 'faisala', 'faisle', 'fauji', 'feku', 'gaddar', 'gadar', 'gair', 'galti', 'gandagi', 'gandhi', 'garib', 'garibi', 'gaum','accha', 'agar', 'aisa', 'aur', 'bahut', 'dosto', 'hai', 'ho', 'ka', 'kar', 'ke', 'ki', 'ko', 'kyun', 'kyunki', 'me', 'nahi', 'ne', 'nhi', 'ni', 'se', 'to', 'ya', 'ye']
# read the csv file into a pandas dataframe
df = pd.read_csv(r"C:\Desktop\namonamo.csv")

# apply the clean_text function to the 'Content' column
df['Content'] = df['Content'].apply(clean_text)

df.to_csv(r"C:\Desktop\namo_test.csv", index=False)
