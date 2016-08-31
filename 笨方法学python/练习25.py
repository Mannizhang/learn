def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split('')
    return words


def sort_words(words):
    """sorts the words."""
    return sorted(words)


def print_first_word(words):
    """prints the first word after popping it off."""
    print(word)


def print_last_words(words):
    """prints the last word after popping it off."""
    print(word)


def sort_sentence(sentence):
    """take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)
#loading...书上写得清楚明白，修改这个ex25这个模块，让它运行无错误，再在cmd或终端输入python，
呼叫出python shell，再import ex25
调用ex25模块的函数，即可。
是英文看不懂，还是没有认真看。
看下面图片，我是如何做的，左边是代码，在代码所在的目录，输入python，再import ex25


链接：http://www.zhihu.com/question/42216402/answer/94034081
来源：知乎
著作权归作者所有，转载请联系作者获得授权。