class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = ['']   
        for d in digits:
            temp = []
            for i in result:
                for ch in digit_to_letters[d]:
                    temp.append(i + ch)
            result = temp
        return result
        
        