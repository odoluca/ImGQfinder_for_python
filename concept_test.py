#inspired by ImGQfinder algorithm at http://imgqfinder.niifhm.ru/algorithm/
import re
import regex
sequence="TTTGGGTTTTTGTGGTTTGGGTTTTTGGGTTTGGTGTTTTTGtGG"

prog=regex.Regex(r"""( [G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,})) ( \w{1,7} (?(mis)[G]{3,} | (?P<mis>[G]{1,}[ATC][G]{1,}) )){3,} """,regex.VERBOSE|regex.MULTILINE)
#finds all perfect, mismatched or buldged imperfect pG4s


prog=regex.Regex(r"""( [G]{3,} | (?P<mis>([G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,}))) ( \w{1,7} (?(mis)[G]{3,} | (?P<mis>([G]{2,}[ATC][G]{1,}|[G]{1,}[ATC][G]{2,})) )){3,} """,regex.VERBOSE|regex.MULTILINE)
#finds both perfect or bulged imperfect pG4s.


def func():
    result = prog.finditer(sequence)
    return result

result=func()
print sequence
for m in result:
    print " "*(m.start()-1),sequence[m.start():m.end()]

