

def count_words(file, word):
    """Count how many times a word pops up"""
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()
        
    except FileNotFoundError:
        print('hi')
    else:
        word_count = content.lower().count(word)
        # count the number of times a word is shown.
        msg = (f"'{word}' appears in {file} about {word_count} times.")
        print(msg)


files = ['our_cats.txt','the_domestic_cat.txt']

for file in files:
    print(f"\nAnalyzing text: {file}")
    count_words(file, 'cat')