class utils:
    def __init__(self):
        pass

    def reversed(self, num):
        if type(num) == int or type(num) == float:
            return int(str(num)[::-1])
        else:
            return None
    
    def formatter(self, num):
        if type(num) == int or type(num) == float:
            return bin(num), hex(num)
        else:
            return None, None
