from searching_ES import SearchES
from search_medline import SearchMedline


def RunSearch(n_results=5):
    SearchMedline(n_results=n_results)
    SearchES(n_results=n_results)