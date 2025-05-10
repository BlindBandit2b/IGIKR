from collections import Counter, defaultdict
import re
from statistics import median

def text_statistics(text, K=10, N=4):
    # Очистка текста от знаков препинания и перевод в нижний регистр
    clean_text = re.sub(r'[^\w\s]', '', text).lower()

    # Разделение на слова и предложения
    words = clean_text.split()
    sentences = re.split(r'[.!?]', text)

    # Подсчёт частоты слов
    word_count = Counter(words)

    # Среднее количество слов в предложении
    sentence_lengths = [len(re.findall(r'\w+', sentence)) for sentence in sentences if sentence]
    avg_words = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0

    # Медианное количество слов в предложении
    median_words = median(sentence_lengths) if sentence_lengths else 0

    # Генерация буквенных N-грамм
    ngrams = defaultdict(int)
    for word in words:
        for i in range(len(word) - N + 1):
            ngram = word[i:i+N]
            ngrams[ngram] += 1

    # Топ-K самых частых N-грамм
    top_ngrams = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:K]

    # Вывод результатов
    print(f"=== Статистика по тексту ===")
    print(f"\nЧастота слов:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print(f"\nСреднее количество слов в предложении: {avg_words:.2f}")
    print(f"Медианное количество слов в предложении: {median_words}")

    print(f"\nТоп-{K} самых частых {N}-грамм:")
    for ngram, count in top_ngrams:
        print(f"{ngram}: {count}")


# 📌 Ввод данных
text = input("Введите текст: ")
K = int(input("Введите количество топ-N-грамм (по умолчанию 10): ") or 10)
N = int(input("Введите размер N-грамм (по умолчанию 4): ") or 4)

# 📌 Запуск статистики
text_statistics(text, K, N)

input("\n Нажмите Enter для выхода...")

