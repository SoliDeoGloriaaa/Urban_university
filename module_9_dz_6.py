def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text) - i + 1):
            yield text[j:j+i]


result = all_variants("abc")
for i in result:
    print(i)
