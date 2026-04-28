class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        j,k = 0, len(people)-1
        count = 0
        while(j <= k):
            # print(j , " ", k)
            if j == k:
                count += 1 
                break
            if people[j] + people[k] <= limit:
                count += 1
                j += 1
                k -= 1
            elif people[j] + people[k] > limit:
                k -= 1
                count += 1    
        return count