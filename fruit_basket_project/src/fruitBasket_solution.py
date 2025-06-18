import sys
import pandas as pd

# Ensure file is passed at runtime
if len(sys.argv) < 2:
    print("Usage: python fruit_basket_report.py <basket.csv>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Ensure 'days' and 'size' are numeric
df['days'] = pd.to_numeric(df['days'], errors='coerce')
df['size'] = pd.to_numeric(df['size'], errors='coerce')

# Drop rows with missing critical data
df.dropna(subset=['name', 'size', 'days'], inplace=True)

# 1. Total number of fruit
total_fruit = df['size'].sum()

# 2. Total types of fruit
type_counts = df.groupby('name')['size'].sum().sort_values(ascending=False)
total_types = type_counts.size

# 3. Characteristics per type
char_map = df.groupby('name').apply(
    lambda x: set((x['color'] + ", " + x['shape']).unique())
)

# 4. Fruits over 3 days old
old_fruits = df[df['days'] > 3].groupby('name')['size'].sum()

# Output
print(f"Total number of fruit: {int(total_fruit)}")
print(f"Types of fruit: {total_types}")
print("The number of each type of fruit in descending order")
for fruit, count in type_counts.items():
    print(f"{fruit}: {int(count)}")

print("The characteristics (size, color, shape, etc.) of each fruit by type")
for fruit, characteristics in char_map.items():
    for char in characteristics:
        print(f"{fruit}: {char}")

if old_fruits.empty:
    print("No fruit has been in the basket for over 3 days")
else:
    def pluralize(fruit, count):
        if fruit.endswith(('s', 'x')):
            return f"{int(count)} {fruit}es"
        elif fruit.endswith('y') and fruit[-2] not in 'aeiou':
            return f"{int(count)} {fruit[:-1]}ies"
        else:
            return f"{int(count)} {fruit}s"

    phrases = [pluralize(fruit, count) for fruit, count in old_fruits.items()]
    print("Have any fruit been in the basket for over 3 days")
    print(f"{' and '.join(phrases)} are over 3 days old")
    print(f"{int(count)} {fruit}(s) are over 3 days old")
