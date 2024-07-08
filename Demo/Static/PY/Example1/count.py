class Count:

    count = 0

    def __init__(self):
        Count.count += 1

    def get_count(self):
        return Count.count
