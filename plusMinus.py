arr = [1,1,0,-1,-1]

def main(array):
    positive = [n for n in array if n > 0]
    negative = [n for n in array if n < 0]
    zero = [n for n in array if n == 0]
    print(format(len(positive) / len(array), '.6f'))
    print(format(len(negative) / len(array), '.6f'))
    print(format(len(zero) / len(array), '.6f'))


if __name__ == '__main__':
    main(arr)