num = 600851475143
count = 2



while True:
    if num % count == 0:
        num /= count
        print(num)
        if num == 1:
            print(count)
            break
    count += 1