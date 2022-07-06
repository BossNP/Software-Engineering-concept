from collections import Counter
import matplotlib.pyplot as plt

def sum_counters(counters):
    # Sum the inputted counters
    return sum(counters, Counter())

def plot_counter_most_common(top_items):
    top_words = []
    top_counts = []

    for item in top_items:
        top_words.append(item[0])
        top_counts.append(item[1])

    plt.bar(x=top_words, height=top_counts)
    plt.xticks(rotation=90)
    plt.show()

def plot_counter(counter, n_most_common=5):
    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)

    # Plot `top_items`
    plot_counter_most_common(top_items)



