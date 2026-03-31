import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Simple Movie Recommender System\n")

# Movie dataset
data = {
    "title": [
        "avengers", "iron man", "thor", "captain america",
        "spiderman", "venom", "batman", "superman",
        "interstellar", "inception", "gravity", "martian"
    ],
    "genre": [
        "action superhero", "action superhero", "action superhero", "action superhero",
        "action superhero", "action antihero", "dark action", "hero action",
        "science fiction space", "science fiction thriller", "space drama", "space survival"
    ]
}

df = pd.DataFrame(data)

# Convert text to vectors
tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(df["genre"])

# Similarity calculation
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie_name):
    name = movie_name.lower().strip()

    if name not in df["title"].values:
        print("Sorry, movie not found in database.")
        return

    index = df.index[df["title"] == name][0]
    scores = list(enumerate(similarity[index]))

    # Sort by similarity score (descending)
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nYou may also like:")
    suggestions = 0

    for i, score in sorted_scores:
        if i != index:
            print("-", df.iloc[i]["title"])
            suggestions += 1
        if suggestions == 3:
            break

# Main loop
while True:
    movie = input("\nEnter a movie name: ")
    recommend(movie)

    choice = input("\nWould you like another recommendation? (yes/no): ").lower()
    if choice not in ["yes", "y"]:
        print("Goodbye!")
        break
