#########################
# 오늘 트리 뽀개기를 뽀갠다 #
########################

import collections
import re
import time

sent_list = []


def subtree(sentence):

    dq = collections.deque()
    score = 0
    i = 0
    i = split_tree(sentence)
    # 노드 덩어리가 큰 덩어리면
    if i == len(sentence):
        for s in sentence:
            dq.append(s)
        ## 전체문장 score 계산 ##
        # 맨 앞 ( 제거
        dq.popleft()
        # 전체 문장 점수 저장
        score = dq.popleft()
        # 공백 제거
        dq.popleft()
        # 마지막 ) 제거
        dq.pop()

        dq_sentence = ''.join(dq)
        sub1_pars_sentence = re.sub("[(]\d{1}[ ]", '', dq_sentence)
        sub2_pars_sentence = re.sub("[)]", '', sub1_pars_sentence)
        # sent_list.append(str(score) + ": " + sub2_pars_sentence)
        sent_list.append([str(score), sub2_pars_sentence])


        if '(' in dq_sentence:
            # ((3 authentic) (2 and)) 와 같으면
            subtree(dq_sentence)
        else:
            # (2 Creepy) 같은 leaf node는 서브트리 안 탐
            pass
        dq_sentence = ''
        dq.clear()

    else:
        subtree(sentence[:i])
        subtree(sentence[i + 1:])

    return sent_list

def split_tree(sentence):
    # ( 개수
    b_left = 0
    # ) 개수
    b_right = 0
    # index 번호
    i = 0

    for s in sentence:
        if s == '(':
            b_left += 1
            i += 1

        elif s == ')':
            b_right += 1
            i += 1

        elif s == ' ':
            if b_left == b_right:

                if b_left == 1:
                    return i
                break
            i += 1
        else:
            i += 1

    if i < 5:
        return 0

    return i


f = open("/home/judy/SentimentTreeBank/stanfordSentimentTreebank/trees/sorted_train.txt", 'r')
lines = f.readlines()

fw = open("/home/judy/SentimentTreeBank/stanfordSentimentTreebank/trees/parsed_sorted_train(only_Sentence).txt", 'w')
l = 0

for line in lines:
    parsed_tree = subtree(line)
    for s in parsed_tree:
        # data = s[0] + '\t' + s[1] + '\n'
        data = s[1] + '\n'
        fw.write(data)
    fw.write('\n')
    sent_list.clear()


f.close()
fw.close()

print("----end----")
