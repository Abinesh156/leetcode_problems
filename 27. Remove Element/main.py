class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)-nums.count(val)
        for i in range(nums.count(val)):
            nums.remove(val)
            nums.append("_")
        return k

