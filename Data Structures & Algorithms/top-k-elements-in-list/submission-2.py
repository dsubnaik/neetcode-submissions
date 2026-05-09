class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        # Count frequencies
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        result = []

        # Find max k times
        for _ in range(k):

            max_key = None
            max_value = 0

            for key in hashmap:
                if hashmap[key] > max_value:
                    max_value = hashmap[key]
                    max_key = key

            result.append(max_key)

            # Remove it so next max can be found
            del hashmap[max_key]

        return result