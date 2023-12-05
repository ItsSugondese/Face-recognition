from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# List of sentences
sentences = [
    "Congrats, You have won!! reply to our sms for a free nokia mobile + free camcorder.",  # spam
    "Congrats! 1 year special cinema pass for 2 is yours. reply to this sms to claim your prize.",  # spam
    "I am pleased to tell you that you are awarded with a 1500 Bonus Prize, reply to this sms to claim your prize.",  # spam
    "Dont worry. I guess he is busy.",  # not spam
    "Going for dinner. msg you later.",  # not spam
    "Ok, I will call you up when I get some cash."  # not spam
]

# Labels indicating whether each sentence is spam or not spam
labels = ["spam", "spam", "spam", "not spam", "not spam", "not spam"]

# Create a CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the sentences
X = vectorizer.fit_transform(sentences)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame
df = pd.DataFrame(X.toarray(), columns=feature_names)
df["Label"] = labels

# Save DataFrame to a CSV file
df.to_csv("count_vectorizer_output.csv", index=False)

# Display the DataFrame
print(df)
