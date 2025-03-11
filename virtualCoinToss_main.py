import random
def coin_toss():
    return random.choice(['Heads', 'Tails'])

def toss_multiple_times(num_flips):
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = coin_toss()
        print(f"Result: {result}")
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def main():
    print("Welcome to the Virtual Coin Toss Program!")

    while True:
        try:
            flips = int(input("Enter the number of coin flips: "))
            if flips <= 0:
                print("Please enter a positive integer.")
                continue

            heads, tails = toss_multiple_times(flips)

            print("\nResults:")
            print(f"Total Flips: {flips}")
            print(f"Heads: {heads} ({(heads / flips) * 100:.2f}%)")
            print(f"Tails: {tails} ({(tails / flips) * 100:.2f}%)")

            again = input("Do you want to toss again? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the Virtual Coin Toss Program!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
