from collections import Counter, defaultdict
import re
from statistics import median

def text_statistics(text, K=10, N=4):
    clean_text = re.sub(r'[^\w\s]', '', text).lower()

    words = clean_text.split()
    sentences = re.split(r'[.!?]', text)

    word_count = Counter(words)

    sentence_lengths = [len(re.findall(r'\w+', sentence)) for sentence in sentences if sentence]
    avg_words = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    median_words = median(sentence_lengths) if sentence_lengths else 0

    ngrams = defaultdict(int)
    for word in words:
        for i in range(len(word) - N + 1):
            ngram = word[i:i+N]
            ngrams[ngram] += 1

    top_ngrams = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:K]

    print(f"Частота слов:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
    print(f"\nСреднее количество слов в предложении: {avg_words:.2f}")
    print(f"Медианное количество слов в предложении: {median_words}")
    print(f"\nТоп-{K} самых частых {N}-грамм:")
    for ngram, count in top_ngrams:
        print(f"{ngram}: {count}")

text = input("Введите текст: ")
K = int(input("Введите количество топ-N-грамм: ") or 10)
N = int(input("Введите размер N-грамм: ") or 4)

text_statistics(text, K, N)

input("\n Нажмите Enter для выхода...")

