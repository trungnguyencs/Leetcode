class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            w = Word(word, freq)
            if len(heap) < k:
                heappush(heap, w)
            elif w > heap[0]:
                heapreplace(heap, w)
        return [w.word for w in sorted(heap, reverse=True)]

class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
    
    def __gt__(self, other):
        return self.freq > other.freq or (self.freq == other.freq and self.word < other.word)