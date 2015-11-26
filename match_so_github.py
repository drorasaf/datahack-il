# -*- coding: utf-8 -*-
from github import github_get_repositories
from stack_overflow import so_get_code, so_get_interesting_answers, code_snippet_get_language
from rank_code import rank_code_snippet_in_rep

# TODO: configure get_repositories using more parameters
popular_languages = ['Python', 'Java']

if __name__ == '__main__':
   code_list = []
   rank_list = []
   hub = {}

   for l in popular_languages:
       hub[l] = github_get_repositories(l)

    # TODO: define filters, define amount of answers to get
   answers = so_get_interesting_answers()
   for answer in answers:
	code_list.append(so_get_code(answer))

   for code_snippet in code_list:
	language = code_snippet_get_language(code_snippet)
        rank_list.append((code_snippet, rank_code_snippet_in_rep(hub[language], code_snippet)))

   print (rank_list)

