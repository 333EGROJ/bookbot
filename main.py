def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_char_lower(book_contents):
    lower = book_contents.lower()
    char_count = {}
    for char in lower:
        if char.isalpha():  # Only consider alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Convert to list of dictionaries and sort
    char_list = [{'char': k, 'num': v} for k, v in char_count.items()]
    char_list.sort(key=lambda x: x['num'], reverse=True)
    
    return char_list

def main():
    with open('books/frankenstein.txt') as f:
        book_contents = f.read()

    total_word_count = count_words(book_contents)
    char_count = count_char_lower(book_contents)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_word_count} words found in the document")
    for item in char_count:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")

if __name__ == "__main__":
    main()