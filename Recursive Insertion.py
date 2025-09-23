class RecursiveInsertion:

    def sort(self, subarray):
        if len(subarray) == 0:
            return "Not a valid length."
        if len(subarray) - 1 == 0:
            return subarray
        sortedSubarray = self.sort(subarray[0:len(subarray)-1])
        i = len(sortedSubarray) - 1
        sortedSubarray.append(sortedSubarray[-1])
        key = subarray[i + 1]
        while((i >= 0) and (key < sortedSubarray[i])):
            sortedSubarray[i + 1] = sortedSubarray[i]
            i -= 1
        sortedSubarray[i + 1] = key
        return sortedSubarray

mySorter = RecursiveInsertion()
sortedList = mySorter.sort([2, 1])
print(f"Sorted List: {sortedList}")