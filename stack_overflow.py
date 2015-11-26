# -*- coding: utf-8 -*-

#sample = "import numpy as np \
#from sklearn.preprocessing import normalize \
#\

sample ="protected void changeMatch(RouteMatch match) {\n\
List<String> requestList = SparkUtils.convertRouteToList(match.getRequestURI());\n\
List<String> matchedList = SparkUtils.convertRouteToList(match.getMatchUri());\n\
\n\
params = getParams(requestList, matchedList);\n\
splat = getSplat(requestList, matchedList);\n\
}"


def code_snippet_get_language(code_snippet):
   return 'Java'

def so_get_code(answer):
   # TODO: find <code> </code> the internal is the actual code
   return answer

def so_get_interesting_answers():
   """ returns a list of possible answers """
   # TODO: load so data and cut it down to interesting ones
   # TODO: define filter
   return [sample]
