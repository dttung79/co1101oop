class SearchResults:
    def __init__(self):
        self.total_occurrences = 0
        self.total_files = 0
        self.result_list = []

    def add(self, search_result):
        self.total_occurrences += search_result.occurrences
        self.result_list.append(search_result)

    def increment(self):
        self.total_files += 1
