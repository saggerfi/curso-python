def run():
    mylist = [i for i in range(1, 100000) if i % 36 == 0]
    print(mylist)

if __name__ == '__main__':
    run()