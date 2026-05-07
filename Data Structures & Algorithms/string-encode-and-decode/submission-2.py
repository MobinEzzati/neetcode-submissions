from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for cr in strs:
            result += str(len(cr)) + "#" + cr

        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the position of '#'
            while s[j] != '#':
                j += 1
            # Extract the length of the string
            length = int(s[i:j])
            # Extract the string using the length
            res.append(s[j + 1:j + 1 + length])
            # Move the index forward
            i = j + 1 + length

        return res

def main():
    # Example usage of the Solution class
    solution = Solution()
    encoded = solution.encode(["we", "say", ":", "yes", "!@#$%^&*()"])
    print(f"Encoded: {encoded}")

    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")

if __name__ == "__main__":
    main()

