from getPatientRecord import get_current_goals
from graph_suggestion import graph_sugg
from search_medline import SearchMedline
from searching_ES import SearchES


goals = get_current_goals()
# print(goals)
suggestions = graph_sugg()
medline = SearchMedline(n_results=5).Medline()
#ES = SearchES(n_results=5).Search()

# print(goals + suggestions + medline + ES)
print(goals + suggestions + medline)