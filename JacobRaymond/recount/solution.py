from collections import Counter

top_2 = Counter(line.strip() for line in iter(input, "***")).most_common(2)
if (top_2[0][1] != top_2[1][1]):
    print(top_2[0][0])
else:
    print("Runoff!")

