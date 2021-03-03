import sys

if __name__ == '__main__':
    def utils(start, stop):
        if start > stop:
            sys.exit("Start is bigger than Stop")

        for i in range(start, stop):
            n = i
            while i != 0:
                last = i % 10
                if last % 2 != 0:
                    i = i // 10
                else:
                    break
            if i == 0:
                yield n

    print(*utils(int(sys.argv[1]), int(sys.argv[2])))
    # print(*utils(99, 11))
