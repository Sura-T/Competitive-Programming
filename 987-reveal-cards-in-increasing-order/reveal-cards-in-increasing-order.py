class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deq = deque()
        for card in sorted(deck, reverse=True):
            if deq:
                deq.appendleft(deq.pop())

            deq.appendleft(card)

        return list(deq)