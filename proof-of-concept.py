import nltk
from nltk.util import ngrams
from collections import defaultdict
import random

# N-gram from the NLTK brown corpus.
nltk.download('brown')
nltk.download('punkt')

sentences = nltk.corpus.brown.sents()

# placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in sentences:
    for w1, w2, w3 in ngrams(sentence, 3, pad_left=True, pad_right=True):
        model[(w1, w2)][w3] += 1

for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# Now, given some beginning words, we can generate some text, similar to example 1.

text = ["I", "am"]
sentence_finished = False

while not sentence_finished:
    # random probability threshold 
    r = random.random()
    accumulator = 0.0

    for word in model[tuple(text[-2:])].keys():
        accumulator += model[tuple(text[-2:])][word]

        if accumulator >= r:
            text.append(word)
            break

    if text[-2:] == [None, None]:
        sentence_finished = True

print(' '.join([t for t in text if t]))

# Some executions:
# I am only a slight one , I know , Angelo Petrini , Frank ! !
# I am an attorney for the equipment and personnel , ritual , which was open to us

# This kind of text generation could be used to implement a business chatbot.