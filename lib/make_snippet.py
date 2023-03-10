"""def make_snippet(str):
    trunc_string = ' '.join(str.split()[:5])
    word_list = str.split()
    num_words = len(word_list)
    if num_words > 5:
        return trunc_string + "..."
    else:
        return str