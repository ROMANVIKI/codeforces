def wayTooLongWords(word):
    if len(word) <= 10:
        return word
    else:
        return f"{word[0]}{len(word) - 2}{word[-1]}"


if __name__ == "__main__":
    no_test_cases = int(input())
    for _ in range(no_test_cases):
        word = str(input())
        print(wayTooLongWords(word))
