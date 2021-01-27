class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop - self.start:
            tot_sec = self.start + index
            hour = tot_sec // (60*60) # 3600 으로 나누면 시간
            tot_sec %= 60*60
            minute = tot_sec // 60 # 60으로 나누면 분
            tot_sec %= 60
            return "%02d:%02d:%02d"%(hour % 24, minute, tot_sec)
        else:
            raise IndexError

start, stop, index = map(int, input().split())   

for i in TimeIterator(start, stop): 
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
