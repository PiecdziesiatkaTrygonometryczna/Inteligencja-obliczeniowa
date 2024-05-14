from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup

positive_review = """
Our stay at the hotel was absolutely fantastic! From the moment we arrived, we were greeted with 
warm smiles and exceptional service. The room was spacious, beautifully decorated, 
and had breathtaking views of the city. The bed was incredibly comfortable, 
and we slept like royalty every night. The staff went above and beyond to 
make our stay memorable, recommending great restaurants and arranging tickets 
for local attractions. The breakfast buffet was delicious, with a wide variety
 of fresh, tasty options. We couldn't have asked for a better experience and can't wait to come back again!

"""

negative_review = """
Our stay at this hotel was a nightmare! The room was filthy, with stains on the carpet and walls. 
The bed was lumpy and uncomfortable, and the sheets looked like they hadn't been changed in weeks. 
The bathroom was disgusting, with mold and mildew everywhere, and a broken shower that only produced 
scalding hot water. The noise from the street kept us up all night, and the staff were rude and unhelpful 
when we complained. To top it off, the breakfast was inedible, with stale pastries and cold coffee. 
We will never stay here again and strongly advise others to avoid this hotel at all costs!
"""


analyzer = SentimentIntensityAnalyzer()
positive_scores = analyzer.polarity_scores(positive_review)
negative_scores = analyzer.polarity_scores(negative_review)

print("Pozytywna recenzja:", positive_scores)
print("Negatywna recenzja:", negative_scores)
