import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import warnings
import gdown


warnings.filterwarnings("ignore")

# Load and preprocess training data
url = 'https://drive.google.com/uc?id=1y_5mhEuzRG1GWMYrOsPeLFVyQY-0FrLh'
output = 'namo_train_labelled_example.csv'
gdown.download(url, output, quiet=False)
namo_train_data = pd.read_csv('namo_train_labelled_example.csv')
namo_train_data = namo_train_data.sort_values(by='Date', ascending=False)
namo_train_df = namo_train_data[["Date","Content", "Retweet-count", "Like-count", "Reply-count"]].copy()

analyzer = SentimentIntensityAnalyzer()

namo_train_df.loc[:, 'pos'] = namo_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['pos'])
namo_train_df.loc[:, 'neu'] = namo_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neu'])
namo_train_df.loc[:, 'neg'] = namo_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neg'])
namo_train_df.loc[:, 'compound'] = namo_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
namo_train_df.loc[:, 'polarity_category'] = namo_train_df['compound'].apply(lambda score: 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral')

# Load and preprocess testing data
url = 'https://drive.google.com/uc?id=1rdztzpMgmypr6gpRX4xmhQPcUAzY3BHn'
output = 'namo_test.csv'
gdown.download(url, output, quiet=False)
namo_test_data = pd.read_csv('namo_test.csv')
namo_test_data['Date'] = pd.to_datetime(namo_test_data['Date'], errors='coerce').dt.strftime('%d') # Convert to dd-mm format
namo_test_data = namo_test_data.dropna(subset=['Date']) # Remove rows with invalid dates
namo_test_data = namo_test_data.sort_values(by='Date', ascending=True)
namo_test_df = namo_test_data[['Date','Content']].copy()
analyzer = SentimentIntensityAnalyzer()
namo_test_df.loc[:, 'pos'] = namo_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['pos'])
namo_test_df.loc[:, 'neu'] = namo_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neu'])
namo_test_df.loc[:, 'neg'] = namo_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neg'])
namo_test_df.loc[:, 'compound'] = namo_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
namo_test_df.loc[:, 'polarity_category'] = namo_test_df['compound'].apply(lambda score: 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral')

# Fit a Linear Regression model to the training data
model = LinearRegression()
model.fit(namo_train_df[["pos", "neu", "neg"]], namo_train_df["compound"])

# Create predictions for the testing data using the trained model
namo_test_grouped = namo_test_df.groupby(['Date']).mean().reset_index()
namo_test_grouped['prediction'] = model.predict(namo_test_grouped[["pos", "neu", "neg"]])

# Calculate the average sentiment score across all days
avg_sentiment = namo_test_grouped['prediction'].mean()
# Get the predictions from the model
predictions = model.predict(namo_test_grouped[["pos", "neu", "neg"]])

# Calculate the r2_score
r2_score = r2_score(namo_test_grouped["compound"], predictions)

# Print the r2_score
print("Accuracy:", r2_score*100,"%")

#Create line plot
plt.figure(figsize=(10,6))
plt.xlabel("Date")
plt.ylabel("Sentiment Scores")

#Plot 'pos' line in dark green
plt.plot(namo_test_grouped['Date'], namo_test_grouped['pos'], color='#006400', linewidth=2, label='positive')

#Plot 'neu' line in dark blue
plt.plot(namo_test_grouped['Date'], namo_test_grouped['neu'], color='#00008B', linewidth=2, label='neutral')

#Plot 'neg' line in dark red
plt.plot(namo_test_grouped['Date'], namo_test_grouped['neg'], color='#8B0000', linewidth=2, label='negative')

# Add text for average sentiment score
plt.text(0.7, 0.24, 'Average Sentiment: {:.2f}'.format(avg_sentiment), transform=plt.gca().transAxes)

#Add horizontal lines at 0.05 and -0.05 sentiment scores
plt.axhline(y=1.0, color='gray', linestyle='--')
plt.axhline(y=0.8, color='gray', linestyle='--')
plt.axhline(y=0.6, color='gray', linestyle='--')
plt.axhline(y=0.4, color='gray', linestyle='--')
plt.axhline(y=0.2, color='gray', linestyle='--')
plt.axhline(y=0.0, color='gray', linestyle='--')
plt.title("Narendra Modi Twitter Sentiment in May,2019")
plt.legend()
plt.show()