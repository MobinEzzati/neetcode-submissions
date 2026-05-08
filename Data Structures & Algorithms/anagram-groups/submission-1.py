class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mygroup = {}

        for item in strs :
            myKey = "".join(sorted(item))
            if myKey not in mygroup :
                mygroup[myKey] = []
            
            mygroup[myKey].append("".join(item))
        
        return list(mygroup.values())
