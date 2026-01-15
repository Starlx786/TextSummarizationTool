import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

def summarize_text(text, summary_ratio=0.3):
    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Tokenize words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Word frequency calculation
    word_freq = defaultdict(int)
    for word in filtered_words:
        word_freq[word] += 1

    # Normalize word frequencies
    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] /= max_freq

    # Sentence scoring
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]

    # Select top sentences
    summary_length = int(len(sentences) * summary_ratio)
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:summary_length]

    # Preserve original order
    summary = " ".join([sentence for sentence in sentences if sentence in summary_sentences])

    return summary


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    input_text = """
    Artificial Intelligence is transforming industries by enabling machines to learn from data.
    It is widely used in healthcare, finance, education, and transportation.
    AI helps automate repetitive tasks, improve decision making, and increase efficiency.
    However, ethical concerns such as data privacy and bias must be addressed.
    The future of AI depends on responsible development and regulation.
    """

    print("ORIGINAL TEXT:\n")
    print(input_text)

    print("\nSUMMARY:\n")
    summary = summarize_text(input_text)
    print(summary)
