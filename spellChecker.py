from collections import Counter

# based on http://norvig.com/spell-correct.html
wordLibrary = ['apple', 'sauce']

WORDS = Counter(wordLibrary)

def correction(word, n=1):
    "Most probable spelling correction for word."
    if n < 0:
        raise ValueError("The nmber of changes away \"n\" has to be greater than 0")
    return max(canidates(word, n), key=P)


def P(word, N=sum(WORDS.values())):
    """Probability of `word`."""
    return WORDS[word] / N


def check(word, known, n):
    for i in range(1, n + 1):
        if val := known(editsN(word, i)):
            return val
    return False


def canidates(word, n):
    """Generate possible spelling corrections for word."""
    # first check if the wword is in the wordlibaray
    return (known([word]) or check(word, known, n) or [word])

def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS)

def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz:'  # characters we are allowed to use to edit a word
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def editsN(word, n):
    if n == 1:
        return edits1(word)
    return (e2 for e1 in editsN(word, n - 1) for e2 in edits1(e1))

print(correction("ap", 3))
