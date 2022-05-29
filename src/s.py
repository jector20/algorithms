

class TestAdA():

    def test_AA7(self):
        a = [2, 6, 4, 8, 10, 9, 15]
        b = 5
        #print([dx for dx in range(len(a))])
        # print(a)
        #print(f"{start=}, {end=}")
        assert b == AA(a)
        # print("==")

    def test_AA9left(self):
        a = [6, 4, 8, 10, 9, 15, 34, 35, 65]
        b = 5
        #print([dx for dx in range(len(a))])
        # print(a)
        #print(f"{start=}, {end=}")
        assert b == AA(a)
        # print("==")

    def test_AA7r(self):
        a = [2, 3, 3, 2, 4]
        b = 3
        assert b == AA(a)

    def test_AA4(self):
        a = [1, 2, 3, 4]
        b = 0

        #print([dx for dx in range(len(a))])
        # print(a)
        #print(f"{start=}, {end=}")
        assert b == AA(a)
        # print("==")

    def test_AA1(self):
        a = [0]
        b = 0

        #print([dx for dx in range(len(a))])
        # print(a)
        #print(f"{start=}, {end=}")
        assert b == AA(a)
        # print("==")


def ncenter(n, groupLength):
    groups = int(n / groupLength)
    lastNumber = n - (groups * groupLength)
    if lastNumber != 0:
        groups = groups + 1
        lastPole = int((lastNumber)/2)
    pole = int((groupLength) / 2)

    firstGroup = 0
    secondaryGroup = groups - 1 - firstGroup

    while firstGroup <= secondaryGroup:

        element = firstGroup * groupLength

        if lastNumber != 0 and (firstGroup == secondaryGroup or firstGroup == secondaryGroup - 1):
            element += lastPole
        else:
            element += pole

        yield element

        if firstGroup != secondaryGroup:
            element = secondaryGroup * groupLength + pole
            yield element

        firstGroup = firstGroup + 1
        secondaryGroup = groups - 1 - firstGroup


def pair(iterable):

    iterable


def AA(nums):

    # n
    start_candidate = [dx for dx in range(
        len(nums)-1) if nums[dx] > nums[dx+1]]
    if len(start_candidate) == 0:
        return 0
    elif len(start_candidate) == 1:
        start = start_candidate[0]
        end = start_candidate[0]+1
    else:
        start = start_candidate[0]
        end = start_candidate[-1]+1

    candidateMin = 10**5 - 1
    candidateMax = -10**5 + 1

    # n
    for candidate in start_candidate:
        candidateMax = max(candidateMax, nums[candidate], nums[candidate+1])
        candidateMin = min(candidateMin, nums[candidate], nums[candidate+1])

    for l in range(start):
        if nums[l] > candidateMin:
            start = l
            break
    for r in range(len(nums)-1, end-1, -1):
        if nums[r] < candidateMax:
            end = r
            break

    return end - start + 1


def BB(prices):
    def keyOfIndex(p):
        return prices[p]

    a = sorted(range(len(prices)), key=keyOfIndex)
    if a[0] > a[-1]:
        return a[-1] - a[0]
    else:
        print(a)


if __name__ == "__main__":
    BB([2, 4, 2, 3, 43, 2, 3])
