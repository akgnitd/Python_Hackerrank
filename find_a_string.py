def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string.startswith(sub_string,i)])
