from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# B
with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokens = word_tokenize(text)

# print(tokens)
# print("Liczba słów:", len(tokens))



# C

# filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
# print(stopwords.words('english'))


# D

arr = ["mr", ",", ".", "``", "-", "''", "'", "'s"]
stop_words = stopwords.words('english')
stop_words.extend(arr)


filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# print(filtered_tokens)
# print("bez stop-words:", len(filtered_tokens))

# E
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token, pos='v') for token in filtered_tokens]

# print(lemmatized_tokens)
# print("liczba słów:", len(lemmatized_tokens))




# F

processed_text = ' '.join(lemmatized_tokens)

vectorizer = CountVectorizer()

X = vectorizer.fit_transform([processed_text])

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

word_counts = df.sum().sort_values(ascending=False)

top_10_words = word_counts.head(10)

plt.figure(figsize=(10, 6))
top_10_words.plot(kind='bar')
plt.xlabel('wyrazy')
plt.ylabel('liczba występowań')
plt.xticks(rotation=45)
plt.savefig("F.png")

# G

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(processed_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("G.png")