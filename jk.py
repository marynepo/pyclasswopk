def read_file(filename):
    DASH = '—'
    with open(filename, encoding = 'utf-8') as f:
        for line in f:
            parts = line.split(DASH)
            quote = parts[0]
            author = parts[1]

            quote_words = get_words(quote)

            if len(quote_words) < 10:
                print(quote)
                

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
    #while text[0] > 0 and text[0] in trash_tokens:
    #    text = text[1:]
    text = text.strip(trash_tokens)
    return text
def main():
    filename = 'C:\\Users\\student\\Documents\\quotes.txt'
    text = read_file(filename)
if __name__ == '__main__':
    main()
