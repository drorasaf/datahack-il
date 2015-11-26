# -*- coding: utf-8 -*-
import difflib
from fuzzywuzzy import fuzz


def rank_code_snippet_in_rep(code_rep, code_snippet):
    """ assuming code rep is already filtered by extension
        returns a float(1 - 100) that represents the matching criteria
    """
    match_counter = 0
    for current_file in code_rep:
    	with open(current_file) as f:
            lines = f.readlines()
	    ratio_accumulator = 0
	    prev_match_ix = -1
	    snippet_counter = 0
            for snippet_code_line in code_snippet.split('\n'):
		snippet_code_line = str.lower(snippet_code_line.decode('utf-8').encode('ascii', 'ignore').strip())
		if len(snippet_code_line) < 2:		   
		    continue
                max_match_ratio, max_match_ix, match = find_best_match(snippet_code_line, lines)
		if not (max_match_ix >= prev_match_ix and max_match_ix <= prev_match_ix + 10):
		    snippet_counter +=1
		    continue
		if max_match_ratio>50:
		    # print(snippet_code_line)
		    # print(match)
	            # print(max_match_ratio)
		    prev_match_ix = max_match_ix
	            ratio_accumulator += 1
	    	snippet_counter += 1
	    matched_weight = float(ratio_accumulator) / float(snippet_counter) 
            if matched_weight > 0.75:
	       match_counter += matched_weight
    return match_counter

def find_best_match(snippet_code_line, target_lines):

   max_match_ratio = 0
   max_match_ix = 0
   target_counter =  0
   for code_line in target_lines:
       target_code_line = str.lower(code_line.decode('utf-8').encode('ascii', 'ignore').strip())
       if len(target_code_line) < 2:
           target_counter += 1
           continue
       ratio = fuzz.ratio(snippet_code_line, target_code_line)
       #sm = difflib.SequenceMatcher(a=snippet_code_line, b=target_code_line, autojunk = False)
       #ratio = sm.ratio()
       if ratio > max_match_ratio:
           max_match_ratio, max_match_ix, match = ratio, target_counter, target_code_line
           target_counter += 1
   return max_match_ratio, max_match_ix, match

