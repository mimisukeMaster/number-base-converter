import json
import itertools

def generate_symbols():
    digits = [str(i) for i in range(10)]
    uppercase = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    hiragana = [chr(i) for i in range(ord('ぁ'), ord('ん') + 1)]
    katakana = [chr(i) for i in range(ord('ァ'), ord('ヶ') + 1)]
    hankakukana = [chr(i) for i in range(ord('ｱ'), ord('ﾝ') + 1)]
    kanji = [chr(i) for i in range(ord('一'), ord('鿿') + 1)] 
    
    return itertools.chain(digits, uppercase, lowercase, hiragana, katakana, hankakukana, kanji)

def create_mapping():
    mapping = {}
    for i, symbol in enumerate(generate_symbols()):
        mapping[str(i)] = symbol
    return mapping

def main():
    mapping = create_mapping()
    with open("symbols.json", "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)
    print("JSON file has been created.")

if __name__ == "__main__":
    main()