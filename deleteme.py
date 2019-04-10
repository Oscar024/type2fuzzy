from type2fuzzy import CrispSet
from type2fuzzy import Type1FuzzySet
from type2fuzzy import GeneralType2FuzzySet
import numpy


c = CrispSet(5,10)
print(c)


s= '0.1/1+0.2/2+0.3/3'
t = Type1FuzzySet.from_representation(s)
print(s)

sg = '(0.1/0.1+0.2/0.2+0.3/0.3)/1 + (0.1/0.1+0.2/0.2+0.3/0.3)/2'
g = GeneralType2FuzzySet.from_representation(sg)

print(g)