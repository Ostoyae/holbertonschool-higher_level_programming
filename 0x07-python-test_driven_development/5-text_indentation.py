"""
Task 4 module

basic example:
>>> text_indentation(" Hello. World: of Python?")
Hello.
<BLANKLINE>
World:
<BLANKLINE>
of Python?
"""


def text_indentation(text):
    """print a string and 2 newlines

    split each line after a period, question mark and colon
    """
    sp_str = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt_cpy = text
    # start with separating the periods
    sp_str = split_to_list(txt_cpy, ".")
    # question mark split
    sp_str = split_to_list(sp_str, "?")
    # finally colons
    sp_str = split_to_list(sp_str, ":")

    for i, ele in enumerate(sp_str):
        print(ele, end="")
        if i < len(sp_str) - 1:
            print(end="\n" * 2)


def split_to_list(text, delim=" "):
    sp_str = []
    if isinstance(text, str):
        txt_cpy = text
        while txt_cpy:
            if delim not in txt_cpy:
                sp_str.append(txt_cpy.strip())
                break
            temp = txt_cpy.split(delim, 1)[0] + delim
            txt_cpy = txt_cpy[len(temp):len(txt_cpy)]
            sp_str.append(temp.strip())
    else:
        for txt in text:
            if delim not in txt:
                sp_str.append(txt)
            else:
                while txt:
                    if delim not in txt:
                        sp_str.append(txt.strip())
                        break
                    temp = txt.split(delim, 1)[0] + delim
                    txt = txt[len(temp):len(txt)]
                    sp_str.append(temp.strip())
    return sp_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
