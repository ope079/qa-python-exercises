def array123(nums):
    nums_string = "".join(str(i) for i in nums)
    if "123" in nums_string:
        return True
    else:
        return False

