import json

# 変換表の読込みと逆方向の変換表を作成 / Load the conversion table and create a reverse mapping
def symbols_and_decimal_mapping(file_path="symbols.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        from_decimal_map = json.load(file)

    to_decimal_map = {v: int(k) for k, v in from_decimal_map.items()}
    
    return from_decimal_map, to_decimal_map

# 元の進数から10進数へ変換 / Convert from origin base to decimal
def convert_to_decimal(value, origin_base, value_map):
    decimal_value = 0

    # 文字列を逆にして{origin_base}の0乗のケタから変換していく
    for index, digit in enumerate(reversed(value)):
        if digit not in value_map:
            raise ValueError(f"'{digit}'に対応する数が見つかりません / Cannot find the number mapped to '{digit}'.")
        if value_map[digit] >= origin_base:
            raise ValueError(f"'{digit}'は{origin_base}進数の表記に使えません / '{digit}' cannot be used for the notation of a number in base '{origin_base}'.")
        
        decimal_value += value_map[digit] * (origin_base ** index)
    
    return decimal_value

# 10進数から任意進数に変換 / Convert from decimal to arbitrary base
def convert_from_decimal(decimal_value, target_base, symbols):
    if decimal_value == 0:
        return "0"
    
    inv_symbols = {int(k): v for k, v in symbols.items()}
    num_list = []

    # 任意進数で割った余りを追加していく
    while decimal_value > 0:
        remainder = decimal_value % target_base

        # 10以上の余りは対応表にある記号に置き換える
        if remainder >= 10:
            remainder = inv_symbols.get(remainder, str(remainder))

        num_list.append(str(remainder))
        decimal_value //= target_base
    
    num_list.reverse()

    return ''.join(num_list)

def main():
    from_decimal_map, to_decimal_map = symbols_and_decimal_mapping()

    while True:
        try:
            origin_base = int(input("何進数を変換しますか / Enter the base number to convert from: "))
            if str(origin_base - 1) not in from_decimal_map:
                raise ValueError(f"{origin_base}進数の変換は対応していません / Conversion from base {origin_base} is not supported")
            
            target_base = int(input("何進数へ変換しますか / Enter the base number to convert to: "))
            if str(target_base - 1) not in from_decimal_map:
                raise ValueError(f"{target_base}進数への変換は対応していません / Conversion to base {origin_base} is not supported")
            
            value = input("値を入力してください / Enter the value: ").strip()
            
            # 元の進数から10進数へ変換 / Convert from origin base to decimal
            decimal_value = convert_to_decimal(value, origin_base, to_decimal_map)

            # 10進数から任意進数へ変換 / Convert from decimal to arbitrary base
            result = convert_from_decimal(decimal_value, target_base, from_decimal_map)

            # 結果を表示 / Show the result
            print("変換結果 / Converted result: ", result)
            
        except ValueError as e:
            print(f"入力エラー / Input error: {e}")
            print("再入力してください / Please enter again.\n")

if __name__ == "__main__":
    main()