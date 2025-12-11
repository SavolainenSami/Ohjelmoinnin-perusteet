def merge(
    PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True
) -> None:
    i = j = k = 0

    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            if PLeft[i] <= PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1
        else:
            if PLeft[i] >= PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1
        k += 1

    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return

    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    merge(left, right, PValues, PAsc)
