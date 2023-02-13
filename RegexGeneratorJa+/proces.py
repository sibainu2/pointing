import MeCab
from dataclass import WordDescription,DecomposedString,MatchDecomposedString

def decompose_string(text:str):
    word_list = []
    #めかぶ～
    m = MeCab.Tagger()
    node = m.parse(text)
    node = node.strip().split("\n")
    for i,w in enumerate(node):
        if w == "EOS":
            continue
        w_list = w.split("\t")
        if len(w_list) < 2:
            continue
        word_list.append(WordDescription(i,w_list[0], w_list[1]))
    return word_list

def shift_list_right_n(lst,n):
    #リストの要素を右に一つずらす関数。
    return lst[-n:] + lst[:-n]

def is_out_of_range(arr, y=0):
    #リストが範囲外か判定する
    try:
        arr[y]
    except IndexError:
        return True
    else:
        return False


def convert_to_2d_array(lst):
    #連続して一致した単語をグループ化する関数
    result = []
    sub_list = []
    #start = lst[0]
    for i, num in enumerate(lst):

        if i == len(lst) - 1:
            sub_list.append(num)
            result.append(sub_list)
        elif num.positions[0] + 1 != lst[i + 1].positions[0] and num.positions[1] + 1 != lst[i + 1].positions[1]:
            sub_list.append(num)
            result.append(sub_list)
            sub_list = []
        else:
            sub_list.append(num)
    return result

def remove_empty_lists(lst):
    #リストの中の空のリストを位置を保持したまま削除する
    return [sub_list for sub_list in lst if sub_list]

def pad_lists(lst, pad_value):
    #パディング関数
    padded_lists = []
    pad_length = max([i.word_count for i in lst])
    for sub_list in lst:
        if len(sub_list.word_list) < pad_length:
            sub_list.word_list.extend(pad_value * (pad_length - len(sub_list.word_list)))
        padded_lists.append(sub_list)
    return padded_lists