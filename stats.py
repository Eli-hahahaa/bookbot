def count_words(text):
    return len(text.split())

def count_chars(text):
    char_freq = {}
    for c in text.lower():
        char_freq[c] = char_freq.get(c, 0) + 1
    return char_freq

def sort_chars_by_freq(raw_freqs):
    freqs = [{"char": k, "num": v} for k, v in raw_freqs.items()]
    freqs.sort(reverse=True, key=lambda x: x["num"])
    return freqs
