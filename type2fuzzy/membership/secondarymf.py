from type2fuzzy.membership.type1fuzzyset import Type1FuzzySet

class SecondaryMembershipFunction(Type1FuzzySet):
	'''
	A secondary membership function is a vertical slice of mu(X=x, u)

	Reference:
	----------
	J. M. Mendel and R. I. B. John, “Type-2 fuzzy sets made simple,” IEEE
	Trans. Fuzzy Syst., vol. 10, no. 2, pp. 117–127, Apr. 2002.
	'''

	def __init__(self):
			super().__init__()

	def union(self, other_smf):
		resultant_set = set.intersection(set(self._elements), set(other_smf._elements))

		resultant_smf = {}
		for  domain_val in resultant_set:
			resultant_smf[domain_val] = max(self._elements[domain_val], other_smf.elements[domain_val])

		return resultant_smf

	def intersection(self, other_smf):
		'''
		'''
		resultant_set = set.intersection(set(self._elements), set(other_smf._elements))

		resultant_smf = {}
		for  domain_val in resultant_set:
			resultant_smf[domain_val] = min(self._elements[domain_val], other_smf.elements[domain_val])

		return resultant_smf


