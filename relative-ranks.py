class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range (len(score)):
            score[i] = (score[i], i)
        score.sort(reverse = True)
        result = [0]*len(score) 
        for i in range(len(score)):
            _, athlete = score[i]
            rank = ""
            match i:
                case 0:
                    rank = "Gold Medal"
                case 1:
                    rank = "Silver Medal"
                case 2:
                    rank = "Bronze Medal"
                case _:
                    rank = str(i+1)
            result[athlete] = rank
        return result

        