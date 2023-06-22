import os
from operator import attrgetter

from search_outcome05 import SearchOutcome
from search_results05 import SearchResults

default_root_path = os.path.expanduser("~" + os.sep + "Documents")
recursive = True
case_sensitive = False
match_phrase = False
extensions = ["py", "txt"]
print_depth = 1
debug = False


def readlines(path):
    """Return contents of text file as a list of lines."""
    with open(path) as file:
        try:
            return file.readlines()
        except UnicodeDecodeError:
            print(f" unicode error in {path}")
            return []


def index_and_search(dirname, root_path_length, search_strings, depth, results, extensions):
    if debug:
        print(dirname)
    try:
        filenames = os.listdir(dirname)
    except PermissionError:
        return
    for filename in filenames:
        path = dirname + os.sep + filename
        if os.path.isdir(path):
            if recursive:
                if depth < print_depth:
                    print(path)
                index_and_search(path, root_path_length, search_strings, depth + 1, results, extensions)
        else:
            if "." not in filename:
                continue
            extension = filename.split(".")[-1]
            if extension not in extensions:
                continue
            lines = readlines(path)
            search_outcome = SearchOutcome(path, search_strings)
            for line in lines:
                if not case_sensitive:
                    line = line.lower()
                all_found = True
                for string in search_strings:
                    count = line.count(string)
                    if count > 0:
                        search_outcome.include(string, count)
                    else:
                        all_found = False
                if all_found:
                    search_outcome.add(line)
            search_matches, search_weighting, search_occurrences = search_outcome.get_summary(search_strings)
            if search_weighting > 0:
                results.add(search_outcome)
                if debug:
                    print(f"{search_occurrences:4} {path[root_path_length:]}")
            results.increment()
    if depth == 0:
        result_list = results.result_list
        # sorting - see https://docs.python.org/3/howto/sorting.html (Sort Stability and Complex Sorts)
        result_list = sorted(result_list, key=attrgetter('occurrences'), reverse=True)
        result_list = sorted(result_list, key=attrgetter('weighting'), reverse=True)
        result_list = sorted(result_list, key=attrgetter('matches'), reverse=True)
        print()
        print("FINAL RESULTS")
        for search_result in result_list:
            info = search_result.get_info(prune=root_path_length)
            print(info)
        print(f" {results.total_occurrences:,} occurrences in "
              f"{len(results.result_list):,} / {results.total_files:,} files")


while True:
    print()
    search_string = input("Search string? ")
    if search_string == "":
        break
    if not case_sensitive:
        search_string = search_string.lower()
    if not match_phrase:
        search_strings = search_string.split()
    else:
        search_strings = [search_string]
    root_path = default_root_path
    print(f"using extensions {extensions}")
    results = SearchResults()
    if os.path.isdir(root_path):
        index_and_search(root_path, len(root_path) + 1, search_strings, 0, results, extensions)
