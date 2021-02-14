import edlib


class StringAnalysis:
    def __init__(self, streaming_string):
        self.streaming_string = streaming_string
        self.word_set = set()

    def _process_stream(self):
        for word in self.streaming_string:
            self.word_set.add(word)

    def get_most_similar_word(self, target_string):
        self._process_stream()
        matches = [(word, edlib.align(target_string, word)['editDistance'])
                   for word in self.word_set]
        return min(matches, key=lambda x: x[1])[0]

