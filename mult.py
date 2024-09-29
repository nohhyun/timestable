import random


def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def random_question():
    i = random.randint(1, 9)
    j = random.randint(1, 9)
    return i, j, i * j


def get_response(i, j):
    resp = input(f"{i} X {j} = ")
    if resp.isdigit():
        return int(resp)
    else:
        print(f"{resp} is not an integer!")
        return get_response(i, j)


def main():
    print("Welcome Arina! Let's start your multiplication challenge!")
    correct_count = 0
    total = 100
    for n in range(total):
        print(f"Your {ordinal(n+1)} question:")
        i, j, ans = random_question()
        resp = get_response(i, j)
        if ans == resp:
            print("Correct! Great job Arina!")
            correct_count += 1
        else:
            print(f"Oh no! The answer is actually {ans}")
            print("That's okay keep going!")
        print(f"You have {correct_count}/{n+1} right! {total - n - 1} more questions to go.")
        print()


if __name__ == '__main__':
    main()
