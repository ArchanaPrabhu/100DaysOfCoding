class BIT:
    def __init__(self, nums):
        # Prepend a  zero to our array to use lowest set beit trick.
        self.tree = [0 for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            self.update(i +1, num)
        
    def update(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        total = 0 
        while index > 0:
            total += self.tree[index]
            index -= index & -index
            return total

    class Subscribers: 
        def __init__(self, nums):
            self.bit = BIT(nums)
            self.nums = nums

        def update(self, hour, value):
            self.bit.update(hour, value - self.nums[hour])
            self.nums[hour] = value

        def query(self, start, end):
            # shift start and end indices forward as our arrat is 1-based
            return self.bit.query(end + 1) - self.bit.query(start)
''' Note that in order for this trick to update to work, we must prepend a zero to our tree array. 
Otherwise the update operation would not work for the 0th index. since 0 &-0 = 0
Because we have decomposed each operation into binary ranges, both update and query are O(log n) time complexity
'''