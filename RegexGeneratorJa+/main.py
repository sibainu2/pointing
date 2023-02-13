import MeCab
import itertools
from dataclass import WordDescription,DecomposedString,MatchWordDescription,MatchDecomposedString,MatchStringBlock
from proces import decompose_string,shift_list_right_n,is_out_of_range,convert_to_2d_array,remove_empty_lists,pad_lists
from typing import List

m = MeCab.Tagger()
text_list = ["テキスト1","テキストに2です a です","テキストに3です です"]



word_list = []
decomposed_string = []
for text in text_list:
    decomposed_string.append(DecomposedString(
        decompose_string(text=text)
        ))

for DecomposedStrings in list(itertools.combinations(decomposed_string, 2)):

    #デバック用print
    print("-" * 20)
    print("比較するテキスト")
    for aDecomposedString in DecomposedStrings:
        print(">"+"".join([i.word for i in aDecomposedString.word_list]))
    print("一致した単語")
    
    matchstring_2d_array_list:List[MatchDecomposedString] = []
    for n in range(max([i.word_count for i in DecomposedStrings])):
        #文字数が多い方をaになるようにする
        def key_out(x:DecomposedString):
            return x.word_count
        list(DecomposedStrings).sort(key=key_out)

        WordDescription_a = shift_list_right_n(DecomposedStrings[0].word_list,n)
        WordDescription_b = DecomposedStrings[1].word_list

        #デバック用printd
        print(f"位置ずらし：回数({n})")


        print([i.word for i in WordDescription_a])
        print([i.word for i in WordDescription_b])
        #インスタスの生成&初期化
        matchstring = MatchDecomposedString(word_list=[])
        #textの比較(ずらし済み)
        for a in range(max([i.word_count for i in DecomposedStrings])):

            #範囲外だったらループをパスする
            if is_out_of_range(WordDescription_a,y=a) or is_out_of_range(WordDescription_b,y=a):
                continue

            #print(WordDescription_b)

            #一致したときの処理
            if [WordDescription_a[a].word]==[WordDescription_b[a].word]:
                print(f"ima{WordDescription_a[a].word,(WordDescription_a[a].position,WordDescription_b[a].position)}")
            if [WordDescription_a[a].word,WordDescription_a[a].meaning]==[WordDescription_b[a].word,WordDescription_b[a].meaning]:

                #デバック用print
                print(f">{WordDescription_a[a].word}(位置{WordDescription_a[a].position,WordDescription_b[a].position})")

                matchstring.word_list.append(
                    MatchWordDescription(
                        positions=[WordDescription_a[a].position,WordDescription_b[a].position],
                        word=WordDescription_a[a].word,
                        meaning=WordDescription_a[a].meaning
                    )
                )
        matchstring_2d_array_list.append(
            convert_to_2d_array(matchstring.word_list)
            )

    tmp_matchstring_3d_array:List = []
    for matchstring_2d_array in matchstring_2d_array_list:
        #被っている文字などを消す
        tmp_positions = MatchStringBlock(word_list = [])
        #ブロックの一番最後の文字の位置を保存する
        tmp_end_word_position:tuple = ((-1,-1),0)
        for matchstring in matchstring_2d_array:
            if (matchstring[0].positions[0] > tmp_end_word_position[0][0] and matchstring[0].positions[0] > tmp_end_word_position[0][1] or
                matchstring[0].positions[0] >= tmp_end_word_position[0][0] and matchstring[0].positions[0] > tmp_end_word_position[0][1] or
                matchstring[0].positions[0] > tmp_end_word_position[0][0] and matchstring[0].positions[0] >= tmp_end_word_position[0][1]
                and len(matchstring) >= tmp_end_word_position[1]):
                
                tmp_end_word_position = (tuple(matchstring[-1].positions),len(matchstring))
                tmp_positions.word_list.append(matchstring)
        if tmp_positions.word_list:
            tmp_matchstring_3d_array.append(tmp_positions)

    for i in tmp_matchstring_3d_array:
        for z in i.word_list:
            print([(x.word,x.positions) for x in z])
    
            

            
                    