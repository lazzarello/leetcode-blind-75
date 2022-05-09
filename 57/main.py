# TODO: Visulize this as a stack of lines with different lengths
class Solution:
    def __init__(self):
        self.start = 0
        self.end = 0
        
    def flatten_list(self, i):
        return [item for sublist in i for item in sublist]

    def get_overlap(self, a, b):
        return max(0, min(a[1], b[1]) - max(a[0], b[0]))

    def find_overlaps(self, intervals, newInterval):
        # searching for "python merge overlapping ranges" resulted in an answer to this
        # specific quiz item
        # https://stackoverflow.com/questions/43600878/merging-overlapping-intervals
        # append the new range to the list and sort it by start
        intervals.append(newInterval)
        intervals.sort()
        # unmerged = []
        # copy the first item in the list and loop over intervals
        merged = [intervals[0]]
        print(f'Merged list {merged}')
        for current in intervals:
            # set previous. I forgot that python lists can have a single negative index.
            # this wraps so on the first iteration previous = merged[len(merged)]
            # Q: why does this work?
            # A: this works because in the first iteration, merged has only one item.
            previous = merged[-1]
            print(f'Previous: {previous}')
            # check that the start of the current iteration is less or equal to the
            # end of the previous iteration.
            if current[0] <= previous[1]:
                # set the end of the previous iteration to the highest between
                # the end of the previous or the end of the current
                print(f'start less then or equal to previous end: {previous}')
                previous[1] = max(previous[1], current[1])
                print(f'previous end set to: {previous[1]}')
            else:
                # if the start of the current iteration is greater then the end of the
                # previous, append the current range to the merged array.
                # this works because merged is sorted and the previous only shuffles
                # things around.
                print(f'start greater then previous end: {current}')
                merged.append(current)
        '''
        for i in intervals:
            for o in newInterval:
                if o > i[0] and o < i[1]:
                    self.start = i[0]
                    self.end = i[0]
                    unmerged.append([i[0],newInterval[1]])
                    idx = intervals.index(i)
                    intervals.pop(idx)
                    break
        '''
        # return intervals
        return merged

def main():
    intervals = [[1,3],[6,9]]
    # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [2,5]
    # newInterval = [4,8]
    s = Solution()
    print(s.find_overlaps(intervals, newInterval))

if __name__ == "__main__":
    main()
