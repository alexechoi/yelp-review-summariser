import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# Define Yelp URL
yelp_url = 'https://www.yelp.com/biz/the-victoria-paddington'

# Send HTTP request to Yelp URL
response = requests.get(yelp_url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the review text
reviews = [review.text for review in soup.select('.css-qgunke span')]

# Define an array to store the keywords
keywords = []

# Extract the keywords from the reviews
for review in reviews:
    # Convert review text to lowercase
    text = review.lower()

    # Split text into words
    words = re.findall(r'\b\w+\b', text)

    # Filter out short words and common words
    filtered_words = [word for word in words if len(word) > 3 and word not in ['the', 'and', 'for', 'with', 'you', 'was', 'but', 'that', 'have', 'are', 'not', 'this']]

    # Add filtered words to keywords array
    keywords += filtered_words

# Count the frequency of each keyword
word_counts = Counter(keywords)

# Print the top 20 keywords
print('Top 20 Keywords:')
for word, count in word_counts.most_common(20):
    print(word, count)
