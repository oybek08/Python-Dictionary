def most_common_char(text):
    from collections import Counter
    return Counter(text).most_common(1)[0][0]