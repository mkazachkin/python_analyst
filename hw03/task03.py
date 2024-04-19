ITEMS = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
MAX_WEIGHT = 1.0

backpack = {}
current_weight: int = 0
for key, value in ITEMS.items():
    if current_weight + value <= MAX_WEIGHT:
        backpack[key] = value
        current_weight += value

print(backpack)