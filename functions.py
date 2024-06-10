from nltk.sentiment import SentimentIntensityAnalyzer


def get_sentiment(diary_paths):
    diary_score_map = {}
    # Initialize Sentiment Intensity Analyzer from NLTK
    analyzer = SentimentIntensityAnalyzer()
    # Calculate sentiment score of each diary, obtain date of each
    for path in diary_paths:
        with open(path) as file:
            diary = file.read()
        score = analyzer.polarity_scores(diary)
        diary_score_map[path.split('/')[1].split('.')[0]] = score

    return diary_score_map


def write_new_entry(diary):
    diary_entry = diary.read()
    with open(f"diary/{diary.name}", "wb") as file:
        file.write(diary_entry)
