def main():
    # Inputs
    orgin_base = int(input("何進数を変換しますか / Enter the base number to convert : "))
    target_base = int(input("何進数へ変換しますか / Enter the base number to convert to : "))

    value = int(input("自然数を入力してください / Enter the natural number : "))

    # Convert input value to decimal value
    num_of_digits = 0
    decimal_value = 0
    while value >= 1:
        decimal_value += value % 10 * orgin_base ** num_of_digits
        value //= 10
        num_of_digits += 1

    # Convert to target_base value
    num_list = []
    while decimal_value >= 1:
        num_list.append(decimal_value % target_base)
        decimal_value //= target_base
    num_list.reverse()
    result = int("".join([str(num) for num in num_list]))

    print(result)

if __name__ == "__main__":
    main()