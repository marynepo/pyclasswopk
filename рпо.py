def read_file(filename):
    DASH = '—'
    with open(filename, encoding = 'utf-8') as f:
        list_of_authors  = []
        for line in f:
            parts = line.split(DASH)
            quote = parts[0].strip()
            author = parts[1].strip()

            quote_words = get_words(quote)
            if 'разум' in quote_words:
                list_of_authors.append(author)

    print( 'Слово \'разум\' встречается ', len(list_of_authors), ' раз')
    print( ', '.join(list_of_authors))
                

def get_words(text):
    trash_tokens = '@#$%^&*()_+=-?:%;№,—.[]{}<>\\\'"'
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens


def clear_text(text, trash_tokens):
    #очистка левой части

    text = text.strip(trash_tokens)
    return text
def main():
    filename = 'C:\\Users\\student\\Documents\\quotes.txt'
    text = read_file(filename)
if __name__ == '__main__':
    main()
