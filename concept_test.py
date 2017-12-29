#inspired by ImGQfinder algorithm at http://imgqfinder.niifhm.ru/algorithm/
import re
import regex
import string
sequence="""
GGGTTTGGGTTTGGGTT TGGGT
TTTTTTTTTTGGTGTTTGGGTTTGGGTTTGGTGTTTTTTTTTTTTGTGTTTGGGTTTGGGTTTGGGTTTTTTTTTTGGTGTTTGGGTTTGGGTTTGGGTTTGGTG
"""


G3_L17_PMB_greedy_pattern=r"""  ( [G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,})) (\w{1,7}  (?(mis)[G]{3,}| ([G]{3,}|(?P<mis>[G]{1,}[ATC][G]{1,})) )){3,} """
C3_L17_PMB_greedy_pattern=r"""  ( [C]{3,} | (?P<mis>[C]{1,}[ATG][C]{1,})) (\w{1,7}  (?(mis)[C]{3,}| ([C]{3,}|(?P<mis>[C]{1,}[ATG][C]{1,})) )){3,} """
#finds al perfect, mismatched or buldged imperfect pG4s


G3_L17_PB_greedy_pattern=r"""  ( [G]{3,} | (?P<mis>[G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,})) (\w{1,7}  (?(mis)[G]{3,}| ([G]{3,}|(?P<mis>[G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,})) )){3,} """
C3_L17_PB_greedy_pattern=r"""  ( [C]{3,} | (?P<mis>[C]{2,}[ATG][C]{1,}|[C]{1,}[ATG][C]{2,})) (\w{1,7}  (?(mis)[C]{3,}| ([C]{3,}|(?P<mis>[C]{2,}[ATG][C]{1,}|[C]{1,}[ATG][C]{2,})) )){3,} """
#finds both perfect or bulged imperfect pG4s.

#G3_L17_PMB_greedy_pattern=r"""  ( [G]{3,} | (?P<mis>[G]{1,}[\w][G]{1,})) (\w{1,7}  (?(mis)[G]{3,}| ([G]{3,}|(?P<mis>[G]{1,}[\w][G]{1,})) )){3,} """

prog=regex.Regex(G3_L17_PB_greedy_pattern,regex.VERBOSE|regex.MULTILINE)


def func(sequence):
    result = prog.finditer(sequence)
    return result

sequence=sequence.translate(string.maketrans("","")," \n")
#cleans up unwanted white spaces and new lines. When collecting from file, use readlines()

result=func(sequence)

print sequence
for m in result:
    print " "*(m.start()-1)+sequence[m.start():m.end()]

