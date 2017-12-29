#inspired by ImGQfinder algorithm at http://imgqfinder.niifhm.ru/algorithm/
import re
import regex
sequence="""
GGGTTTGGGTTTGGGTTTGGGTTTTTTTTTTTTGGTGTTTGGGTTTGGGTTTGGGTTTTTTTTTTTTGGGTTTGGGTTTGGGTTTGTGTTTTTTTTTTGGTGTTTGGGTTTGGGTTTGGGTTTGGTG
"""


G3_PMB_greedy_pattern=r"""  ( [G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,})) (\w{1,7}  (?(mis)[G]{3,}| ([G]{3,}|(?P<mis>[G]{1,}[ATC][G]{1,})) )){3,} """
#G3_PB_greedy_pattern=r"""( [G]{3,} | (?P<mis>([G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,}))) ( \w{1,7} (?(mis)[G]{3,} | (?P<mis>([G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,})) )){2,} ( \w{1,7} (?(mis)[G]{3,} | ([G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,}|[G]{3,}) ))"""

#G3_PMB_nongreedy_pattern=r"""( [G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,})) ( \w{1,7} (?(mis)[G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,}) )){3} """



prog=regex.Regex(G3_PMB_greedy_pattern,regex.VERBOSE|regex.MULTILINE)
#finds all perfect, mismatched or buldged imperfect pG4s


#prog=regex.Regex(G3_PB_greedy_pattern,regex.VERBOSE|regex.MULTILINE)
#finds both perfect or bulged imperfect pG4s.


def func():
    result = prog.finditer(sequence)
    return result

result=func()
print sequence
for m in result:
    print " "*(m.start()-1),sequence[m.start():m.end()]

