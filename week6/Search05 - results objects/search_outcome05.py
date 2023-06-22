class SearchOutcome():
    def __init__(self, path, search_strings):
        self.path = path
        self.lines = []
        self.dict = {}
        for string in search_strings:
            self.dict[string] = 0

    def add(self, line):
        self.lines.append(line)

    def include(self, string, count):
        self.dict[string] += count

    def get_summary(self, search_strings):
        self.matches = len(self.lines)
        self.weighting = 1
        self.occurrences = 0
        for string in search_strings:
            count = self.dict[string]
            self.weighting *= count
            self.occurrences += count
        return self.matches, self.weighting, self.occurrences

    def get_info(self, prune=0):
        return f" {self.matches:4} {self.weighting:6} {self.occurrences:4} {self.path[prune:]}"
