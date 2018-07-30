def count_words (text, words):
    return sum(w in text.lower() for w in words)


print(count_words(
    "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
    ["far", "word", "vokal", "count", "tries"]))
