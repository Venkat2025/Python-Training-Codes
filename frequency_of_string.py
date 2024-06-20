from collections import Counter
def min_magicString(S):
    frequency=Counter(S)
    max_freq=max(frequency.values())
    min_steps=len(S)-max_freq
    return min_steps
S='aaabbbbbccccdddd'
print(min_magicString(S))