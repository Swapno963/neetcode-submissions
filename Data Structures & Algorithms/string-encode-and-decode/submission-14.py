class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(0, len(strs)):
            if strs[i] == "":
                strs[i] = "only_space"

        return "-".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = s.split("-")
        for i in range(0, len(strs)):
            if strs[i] == "only_space":
                strs[i] = ""
        return strs
