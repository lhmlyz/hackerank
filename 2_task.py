if __name__ == '__main__':
    a = int(input())
    b = int(input())

    def calc(a,b):
        return '{}\n{}\n'.format(a//b, a/b)

print(calc(a,b))