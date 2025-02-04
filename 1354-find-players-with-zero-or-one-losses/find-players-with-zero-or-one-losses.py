class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = []
        winners = []
        for left in matches:
            losers.append(left[1])
            winners.append(left[0])
        
        cnt = Counter(losers)
        win = []
        for i in range(len(winners)):
            if winners[i] not in cnt and winners[i] not in win:
                win.append(winners[i])
        lose = []
        for i in cnt:
            if cnt[i] == 1:
                lose.append(i)
        win.sort()
        lose.sort()

        return [win,lose]