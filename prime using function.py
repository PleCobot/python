from primeornot import check
def  main():
    n=int(input('Enter the range: '))
    print("Prime nos are ")
    for i in range(1,n+1):
        if check(i):
            print(f"{i}",end=",")






if __name__ == "__main__":
    main()