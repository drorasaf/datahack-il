# -*- coding: utf-8 -*-
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
	    #snippet_code_line = str.lower(snippet_code_line.decode('utf-8').encode('ascii', 'ignore').strip())
	    snippet_code_line = str.lower(snippet_code_line.strip())
	    if len(snippet_code_line) < 2:		   
	        continue

            max_match_ratio, max_match_ix, match = find_best_match(snippet_code_line, lines)
#	    if prev_match_ix>0:
#		if  max_match_ix <= prev_match_ix or max_match_ix <= (prev_match_ix + 5):
#	            snippet_counter += 1
#		    prev_match_ix= -1
#	            continue

	    if max_match_ratio>70:
	        # print(snippet_code_line)
	        # print(match)
	        # print(max_match_ratio)
	        prev_match_ix = max_match_ix
	        ratio_accumulator += 1
		# print(ratio_accumulator)
	    snippet_counter += 1
	# if ratio_accumulator>0:
        #     print('meow {0} {1}'.format(ratio_accumulator, snippet_counter))
	matched_weight = float(ratio_accumulator) / float(snippet_counter)

        if matched_weight > 0.6:
           print('Mabsoot alecha, matched_weight={0}'.format(matched_weight))
	   match_counter += matched_weight
    return match_counter

def find_best_match(snippet_code_line, target_lines):

   max_match_ratio = 0
   max_match_ix = 0
   target_counter =  0
   # print(target_lines)
   for code_line in target_lines:
       #target_code_line = str.lower(code_line.decode('utf-8').encode('ascii', 'ignore').strip())
       target_code_line = str.lower(code_line.strip())
       if len(target_code_line) < 2:
           target_counter += 1
           continue
       ratio = fuzz.ratio(snippet_code_line, target_code_line)
       if ratio > max_match_ratio:
           max_match_ratio, max_match_ix, match = ratio, target_counter, target_code_line
       target_counter += 1
   return max_match_ratio, max_match_ix, match

