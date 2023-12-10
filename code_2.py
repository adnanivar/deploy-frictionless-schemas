import random

    for item in data:
        print(f"Random Number: {item}")
def generate_random_data():
    main()

    data = [random.randint(1, 100) for _ in range(10)]

if __name__ == "__main__":
    return data

def main():
    data = generate_random_data()