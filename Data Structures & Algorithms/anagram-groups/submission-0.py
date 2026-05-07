class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyLIst = {}

        finalList = []

        for item in strs:
            sorted_val = sorted(item)
            joined ="".join(sorted_val)
            if joined not in keyLIst:
                keyLIst[joined] = []
            
            keyLIst[joined].append(item)

        finalRes = list(keyLIst.values())
        return finalRes
        

                

        


        