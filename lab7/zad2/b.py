from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup

positive_review = """
The room is new, nice, and modern. bed is super comfortable. The apartment is super clean and quiet.
New building. The heating is great. It is possible to rent the parking spot (which I recommend,
just 12 EUR + deposit for the pilot), this will save you much time.
"""

negative_review = """No bed, just a sofa (back folds flat, no mattress), dirty bedding, only 1 curtain for
2 windows so 1 window not covered, occasional noise from busy road, no free toiletries, communication
slow and only in polish"""


analyzer = SentimentIntensityAnalyzer()
positive_scores = analyzer.polarity_scores(positive_review)
negative_scores = analyzer.polarity_scores(negative_review)

print("Pozytywna recenzja:", positive_scores)
print("Negatywna recenzja:", negative_scores)
