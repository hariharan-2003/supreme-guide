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

output = 'raga_train_labelled_example.csv'
gdown.download(url, output, quiet=False)
raga_train_data = pd.read_csv('raga_train_labelled_example.csv')
raga_train_data = raga_train_data.sort_values(by='Date', ascending=False)
raga_train_df = raga_train_data[["Date","Content", "Retweet-count", "Like-count", "Reply-count"]].copy()

analyzer = SentimentIntensityAnalyzer()

raga_train_df.loc[:, 'pos'] = raga_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['pos'])
raga_train_df.loc[:, 'neu'] = raga_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neu'])
raga_train_df.loc[:, 'neg'] = raga_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neg'])
raga_train_df.loc[:, 'compound'] = raga_train_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
raga_train_df.loc[:, 'polarity_category'] = raga_train_df['compound'].apply(lambda score: 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral')

# Load and preprocess testing data
url = 'https://drive.google.com/u/0/uc?id=1y_5mhEuzRG1GWMYrOsPeLFVyQY-0FrLh&export=download'
output = 'raga_test.csv'
gdown.download(url, output, quiet=False)

raga_test_data = pd.read_csv('raga_test.csv')
raga_test_data['Date'] = pd.to_datetime(raga_test_data['Date'], errors='coerce').dt.day # Extract the day of the month
raga_test_data = raga_test_data[(raga_test_data['Date'] >= 21) & (raga_test_data['Date'] <= 30)] # Keep only rows where the day of the month is between 21 and 30
raga_test_data = raga_test_data.sort_values(by='Date', ascending=True)

raga_test_df = raga_test_data[['Date','Content']].copy()

analyzer = SentimentIntensityAnalyzer()

raga_test_df.loc[:, 'pos'] = raga_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['pos'])
raga_test_df.loc[:, 'neu'] = raga_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neu'])
raga_test_df.loc[:, 'neg'] = raga_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['neg'])
raga_test_df.loc[:, 'compound'] = raga_test_df['Content'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
raga_test_df.loc[:, 'polarity_category'] = raga_test_df['compound'].apply(lambda score: 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral')


# Fit a Linear Regression model to the training data
model = LinearRegression()
model.fit(raga_train_df[["pos", "neu", "neg"]], raga_train_df["compound"])

# Create predictions for the testing data using the trained model
raga_test_grouped = raga_test_df.groupby(['Date']).mean().reset_index()
raga_test_grouped['prediction'] = model.predict(raga_test_grouped[["pos", "neu", "neg"]])

# Calculate the average sentiment score across all days
avg_sentiment = raga_test_grouped['prediction'].mean()
# Get the predictions from the model
predictions = model.predict(raga_test_grouped[["pos", "neu", "neg"]])

# Calculate the r2_score
r2_score = r2_score(raga_test_grouped["compound"], predictions)

# Print the r2_score
print("Accuracy:", r2_score*100,"%")
# Create line plot
plt.figure(figsize=(10,6))
plt.xlabel("Date")
plt.ylabel("Sentiment Scores")

# Plot 'pos' line in dark green
plt.plot(raga_test_grouped['Date'], raga_test_grouped['pos'], color='#006400', linewidth=2, label='positive')

# Plot 'neu' line in dark blue
plt.plot(raga_test_grouped['Date'], raga_test_grouped['neu'], color='#00008B', linewidth=2, label='neutral')

# Plot 'neg' line in dark red
plt.plot(raga_test_grouped['Date'], raga_test_grouped['neg'], color='#8B0000', linewidth=2, label='negative')

# Add horizontal lines at 0.05 and -0.05 sentiment scores
plt.axhline(y=1.0, color='gray', linestyle='--')
plt.axhline(y=0.8, color='gray', linestyle='--')
plt.axhline(y=0.6, color='gray', linestyle='--')
plt.axhline(y=0.4, color='gray', linestyle='--')
plt.axhline(y=0.2, color='gray', linestyle='--')
plt.axhline(y=0.0, color='gray', linestyle='--')

# Add text for average sentiment score
plt.text(0.7, 0.24, 'Average Sentiment: {:.2f}'.format(avg_sentiment), transform=plt.gca().transAxes)
plt.title("Rahul gandhi Twitter Sentiment in May,2019")
plt.legend()
plt.show()