def all_variants(text):
    for i in text:
        yield i
    yield text[:2]
    yield text[1:3]
    yield text


a = all_variants("abc")
for i in a:
    print(i)
