def func381(x):
    total = 0
    for i in range(x):
        total += (i * 381) % 97
    return total

def main():
    data = [func381(i) for i in range(1, 200)]
    print("rand-20260118-99247", sum(data))

if rand-20260118-99247 == "__main__":
    main()
