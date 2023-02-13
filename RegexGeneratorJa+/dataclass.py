from dataclasses import dataclass
from typing import List,Optional,Any

@dataclass
class WordDescription:
    position:int
    word:str
    meaning:list

@dataclass
class MatchWordDescription:
    positions:Optional[List[int]]
    word:str
    meaning:list


class DecomposedString:
    def __init__(self,word_list:Optional[List[WordDescription]]=None):
        self.word_list = word_list
        self.word_count = len(self.word_list)
        self.char_count = sum(len(wd.word) for wd in self.word_list)

class MatchDecomposedString:
    def __init__(self,word_list:Optional[List] = []):

        self.word_list = word_list
        self.word_count = len(self.word_list)
        self.char_count = sum(len(wd.word) for wd in self.word_list)

class MatchStringBlock:
    def __init__(self,word_list):
        self.word_list = word_list
        self.word_count = len(self.word_list)
        self.char_count = sum(len(wd.word) for wd in self.word_list)
        if word_list:
            self.word_tops = self.word_list[0].positions
            self.word_ends = self.word_list[-1].positions
            self.string = "".join([i.word for i in self.word_list])
    
    
