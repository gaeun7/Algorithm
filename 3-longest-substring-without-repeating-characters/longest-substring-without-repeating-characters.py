class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 각 문자의 인덱스를 저장하는 딕셔너리
        char_index = {}
        # 현재 부분 문자열의 시작 인덱스
        start = 0
        # 가장 긴 부분 문자열의 길이
        max_length = 0
        
        for end, char in enumerate(s):
            # 만약 현재 문자가 이미 등장한 적이 있다면,
            # 그 이전에 나온 위치(start 이상) 중에서 가장 가까운 위치를 선택하여 start 갱신
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # 현재 문자의 인덱스를 갱신
            char_index[char] = end
            
            # 현재까지의 부분 문자열의 길이 갱신
            max_length = max(max_length, end - start + 1)
        
        return max_length
