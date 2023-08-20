"""
сгрупировать слова sample input [eat, tea, tan, ate, nat]
sample output [ [ate, tea, eat], [nat, tan]
"""

def groupwords(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans
