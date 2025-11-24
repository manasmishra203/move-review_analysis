import random

# Very Basic Sentiment Analysis Program WITH randomness

positive_words = ["good", "great", "amazing", "fantastic", "wonderful"]
negative_words = ["bad", "boring", "terrible", "awful", "worst"]

positive_phrases = [
    "the movie was",
    "the acting was",
    "overall it was",
    "i really",
    "the film felt"
]

negative_phrases = [
    "the movie was",
    "the acting was",
    "overall it was",
    "i really",
    "the film felt"
]

# ---------------------------
# TRAINING COUNTS
# ---------------------------

pos_counts = {}
neg_counts = {}
pos_total = 0
neg_total = 0

# ---------------------------
# RANDOM DATASET GENERATION
# ---------------------------

positive_reviews = []
negative_reviews = []

# Generate 10 positive random reviews
for _ in range(10):
    phrase = random.choice(positive_phrases)
    word = random.choice(positive_words)
    sentence = phrase + " " + word
    positive_reviews.append(sentence)

# Generate 10 negative random reviews
for _ in range(10):
    phrase = random.choice(negative_phrases)
    word = random.choice(negative_words)
    sentence = phrase + " " + word
    negative_reviews.append(sentence)

# Count words from positive reviews
for review in positive_reviews:
    for w in review.split():
        pos_counts[w] = pos_counts.get(w, 0) + 1
        pos_total += 1

# Count words from negative reviews
for review in negative_reviews:
    for w in review.split():
        neg_counts[w] = neg_counts.get(w, 0) + 1
        neg_total += 1

# ---------------------------
# PREDICT FUNCTION
# ---------------------------

def predict(text):
    words = text.split()
    pos_score = 0
    neg_score = 0

    for w in words:
        pos_score += pos_counts.get(w, 0)
        neg_score += neg_counts.get(w, 0)

    if pos_score > neg_score:
        return "positive"
    elif neg_score > pos_score:
        return "negative"
    else:
        return "cannot decide"

# ---------------------------
# USER INPUT LOOP
# ---------------------------

while True:
    review = input("\nEnter a movie review (type 'exit' to stop): ").lower().strip()

    if review == "exit":
        print("Goodbye!")
        break

    if review == "":
        print("Please type something!")
        continue

    print("Prediction:", predict(review))
