import heapq


def maintain_median(file_handle):
    low = []
    high = []
    median = []
    lines = file_handle.read().split('\n')
    for k, l in enumerate(lines[:-1]):
        num = int(l)
        if not k:
            low.append(num)
            median.append(num)
        else:
            if num > median[k - 1]:
                high.append(num)
            if num <= median[k - 1]:
                low.append(num)
            if len(low) > len(high) + 1:
                low_highest = heapq.nlargest(1, low)[0]
                low = list(set(low) - set([low_highest]))
                high.append(low_highest)
            if len(high) > len(low) + 1:
                high_lowest = heapq.nsmallest(1, high)[0]
                high = list(set(high) - set([high_lowest]))
                low.append(high_lowest)

            if k % 2:  # even number of elements
                median.append(heapq.nlargest(1, low)[0])
            else:  # odd number of elements
                if len(low) > k / 2:
                    median.append(heapq.nlargest(1, low)[0])
                else:
                    median.append(heapq.nsmallest(1, high)[0])
    return median


fh = open('Median.txt', 'r')
medians = maintain_median(fh)
sum(medians) % 10000
fh.close()
