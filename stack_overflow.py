# -*- coding: utf-8 -*-

sample = "import numpy as np \
from sklearn.preprocessing import normalize \
\
x = np.random.rand(1000)*10 \
norm1 = x / np.linalg.norm(x) \
norm2 = normalize(x[:,np.newaxis], axis=0).ravel() \
print np.all(norm1 == norm2)"

def code_snippet_get_language(code_snippet):
   return 'Python'

def so_get_code(answer):
   # TODO: find <code> </code> the internal is the actual code
   return answer

def so_get_interesting_answers():
   """ returns a list of possible answers """
   # TODO: load so data and cut it down to interesting ones
   # TODO: define filter
   return [sample]
