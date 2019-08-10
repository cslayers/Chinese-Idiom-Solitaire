

# idiom collection is from https://github.com/pwxcoo/chinese-xinhua
# word 成语
# item 一条成语json记录
# char 汉字
# 需求

# 1. 给出一个词列表 词的首字的拼音字母是给定的，e.g. 'pin'
# 2. 给出一个词列表 词的末字的拼音字母是给定的，e.g. 'lia'

# 3. 对一个词列表排序，最快结束游戏的排在前面 ----------现实词频；玩家习惯；
# 4. 对一个词列表排序，后继词最少的排在前面


from pypinyin import pinyin, lazy_pinyin, Style
import json

word_set= set ()
first_index_store = {}
last_index_store = {}


def build_word_set():
    with open("./idiom.json", 'r') as load_f:
        dict_json = json.load(load_f)
    for item in dict_json:
        word = item['word']
        word_set.add(word)


def build_indexs():
    for word in word_set:
        first_key = lazy_pinyin(word)[0]
        last_key = lazy_pinyin(word)[-1]
        if not first_index_store. __contains__(first_key):
            first_index_store[first_key] = []
        if not last_index_store. __contains__(last_key):
            last_index_store[last_key] = []
        first_index_store[first_key].append(word)
        last_index_store[last_key].append(word)


build_word_set()
build_indexs()




def getWordListByFirstPinyin(first_pinyin):
    if first_index_store.__contains__(first_pinyin):
        return first_index_store[first_pinyin]
    else:
        return []


def getWordListByLastPinyin(last_pinyin):
    if last_index_store.__contains__(last_pinyin):
        return last_index_store[last_pinyin]
    else:
        return []


def sort_by_next_count(word_list):
    
    def second(elem):
        return elem[1]
    
    pairs=[]
    for word in word_list:
        e1 = word
        e2 = len(getWordListByFirstPinyin(lazy_pinyin(word)[-1]))
        pairs.append((e1,e2))
    pairs.sort(key=second)
    
    word_list=[]
    for p in pairs:
        word_list.append(p[0])
    
    return pairs,word_list
    
def get_sorted_next_word_list(first):
    next_words = getWordListByFirstPinyin(first)
    next_word_and_nums, next_words_sort = sort_by_next_count(next_words)
    return next_words_sort


def get_pinyins_without_next():
    first_set = set(first_index_store.keys())
    last_set = set(last_index_store.keys())
    no_first_set = last_set - first_set
    return list(no_first_set)


def main():
    pinyin = 'pin'
    next_candidates = get_sorted_next_word_list(pinyin)
    print('pin ->',next_candidates)
    print()

    # get a list of pinyins that never being the pinyin of first char of any idiom
    hell_list = get_pinyins_without_next()
    print(hell_list)
    assert 'lia' in hell_list
    
    # to find all the words that terminate the game immediately
    for hell in hell_list:
        print(getWordListByLastPinyin(hell)) 


if __name__ == '__main__':
    main()
    




# to find words that end the game imediately

# print('Black hole ',no_first_set)
# for n in no_first_set:
#     print(getListByLastPinyin(n))
#     print(getListByFirstPinyin(n))




# with open("./idiom.json", 'r') as load_f:
#     dict_json = json.load(load_f)

# item = dict_json[0]
# word = item['word']
# first_char = word[0]

# print('dict len:', len(dict_json))
# print('item:', item)
# print('word:', word)
# print('first char:', first_char)


# print(lazy_pinyin(first_char))
# print(lazy_pinyin(word))