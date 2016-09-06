#创建句子
#1.匹配match：主谓宾设置中不同种类元组的方法
#2.窥视peek：潜在元组的方法，以便做决定时候用到
#3.跳过skip：我们不关心内容的方法，如形容词、冠词等修饰词



#peek
def peek(word_list):
    if word_list:
        word=word_list[0]
        return word[0]
    else:
        return None
#match
def match (word_list,expecting):
   if word_list:
       word=word_list.pop(0)
       if word[0]==expecting:
           return word
       else:
           return None
   else:
       return None
#skip
def skip(word_list,word_type):
    while peek(word_list)==word_type:
        match(word_list,word_type)