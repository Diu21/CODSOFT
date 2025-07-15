import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load multi-type item dataset
data = {
    'title': [
        'Iron Man',
        'Avengers',
        'Titanic',
        'Captain America',
        'The Notebook',
        'Harry Potter',
        'Atomic Habits',
        'iPhone 14',
        'Samsung Galaxy',
        'Bluetooth Headphones'
    ],
    'category': [
        'Movie', 'Movie', 'Movie', 'Movie', 'Movie',
        'Book', 'Book',
        'Product', 'Product', 'Product'
    ],
    'description': [
        'A billionaire builds an armored suit.',
        'Heroes team up to save the world.',
        'A love story on a sinking ship.',
        'A soldier becomes a patriotic superhero.',
        'Romantic drama about love and memories.',
        'A young wizard discovers his magical destiny.',
        'A self-help guide to build better habits.',
        'Latest Apple smartphone with advanced camera.',
        'Android phone with high battery life.',
        'Wireless headphones with noise cancellation.'
    ]
}

df = pd.DataFrame(data)

# Step 2: Convert descriptions to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Step 3: Compute cosine similarity between all items
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 4: Define recommendation function
def recommend(title):
    if title not in df['title'].values:
        print("❌ Item not found!")
        return

    idx = df[df['title'] == title].index[0]
    input_category = df.iloc[idx]['category']

    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Boost similarity if category matches
    boosted_scores = []
    for i, score in sim_scores:
        if i == idx:
            continue  # Skip the same item
        if df.iloc[i]['category'] == input_category:
            score += 0.2  # Bonus for same category
        boosted_scores.append((i, score))
    
    # Sort and get top 3 results
    top_matches = sorted(boosted_scores, key=lambda x: x[1], reverse=True)[:3]

    print(f"\n📢 Recommendations for '{title}':")
    for i, score in top_matches:
        print(f" - {df.iloc[i]['title']} ({df.iloc[i]['category']})")

# Step 5: Take user input
item_name = input("🔍 Enter an item name (movie/book/product): ")
recommend(item_name)