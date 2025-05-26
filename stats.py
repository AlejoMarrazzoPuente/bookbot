def get_book_text(filepath: str):
    content = None

    with open(filepath) as f:
        content = f.read()

    return content 

def get_num_words(text: str):
    words_quantity = text.strip().split()
    return len(words_quantity)

def count_chars(filepath: str):
    content = get_book_text(filepath)
    words = content.strip().split()
    char_dic: dict = {}

    for word in words:
        for ch in word:
            if ch.isalpha():
                t_ch = ch.lower()
                if t_ch not in list(char_dic.keys()):
                    char_dic[t_ch] = 0
                char_dic[t_ch] += 1
    
    return char_dic

def present_chars(chars: dict):
    val = sorted(list(chars.keys()), key= lambda x: chars[x], reverse=True)
    for v in val:
        print(f"{v}: {chars[v]}")
    


