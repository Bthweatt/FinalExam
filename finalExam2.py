COIN_VALUES = {
    "penny": 0.01, "pennies": 0.01,
    "nickel": 0.05, "nickels": 0.05,
    "dime": 0.10, "dimes": 0.10,
    "quarter": 0.25, "quarters": 0.25
}

def parse_coin_sentence(sentence):
    """
    Converts a pseudo-English sentence describing coins into a dollar amount.
    Example: "1 penny and 2 nickels" -> 0.11
    """
    sentence = sentence.lower().strip()
    phrases = sentence.split(" and ")
    total = 0.0

    for phrase in phrases:
        parts = phrase.strip().split()
        if len(parts) < 2:
            continue  # skip malformed input
        quantity = int(parts[0])
        denomination = " ".join(parts[1:])
        coin_value = COIN_VALUES.get(denomination, 0)
        total += quantity * coin_value

    return round(total, 2)

if __name__ == "__main__":
    test_cases = [
        "1 penny and 2 nickels",
        "4 dimes and 7 quarters",
        "1 quarter and 3 pennies",
        "21 pennies and 17 dimes and 52 quarters",
        "95 dimes and 73 quarters and 22 nickels and 36 pennies",
        "1 nickel and 17 quarters",
        "21 nickels and 15 pennies",
        "1 dime and 1 nickel and 1 penny and 1 quarter"
    ]

    for case in test_cases:
        print(f"{case} -> {parse_coin_sentence(case)}")