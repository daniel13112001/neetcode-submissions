class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for s in strs:
            ssorted = "".join(sorted(s))
            if ssorted in groups:
                groups[ssorted].append(s)
            else:
                groups[ssorted] = [s]
        a = [groups[i] for i in groups]
        return a
        