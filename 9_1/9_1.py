def main():
    inputs = open("test_input.txt")

    for line in inputs:
        previous_numbers = [int(i) for i in line.strip().split()]
        current_numbers = []

        while sum(previous_numbers) != 0:
            print(previous_numbers)
            for i in range(len(previous_numbers)-1):
                current_numbers.append(previous_numbers[i+1]-previous_numbers[i])
            previous_numbers = current_numbers
            current_numbers = []
        print(previous_numbers)


if __name__ == "__main__":
    main()
