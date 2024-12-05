class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        sp = [(i, char) for i, char in enumerate(start) if char != "_"]
        tp = [(i, char) for i, char in enumerate(target) if char != "_"]

        for (start_idx, char), (target_idx, _) in zip(sp, tp):
            if char == "L" and target_idx > start_idx:
                return False
            if char == "R" and target_idx < start_idx:
                return False

        return True

        