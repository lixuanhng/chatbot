# -*- coding: utf-8 -*-

'''
@Author  :   Bruce

@Software:   PyCharm

@File    :   read_qa.py

@Time    :   2020-6-29 14:26

@Desc    :   本代码的目的是将问答数据进行导入

'''
import os
import pathlib
from run_similarity import BertSim
import tensorflow as tf


sim = BertSim()
sim.set_mode(tf.estimator.ModeKeys.PREDICT)

file_path = os.path.abspath(__file__)
# 路径为 /home/lixh/works/text/chatbot_project/Chatbot_Retrieval/Chatbot_Retrieval_model/Bert_sim
basepath = str(pathlib.Path(file_path).parent)
print(basepath)

class similarity():
    def __init__(self, path):
        self.path = path  # 对话数据路径

    def mainProcess(self):
        """
        找出与输入问题
        :return:
        """
        print('\n' + '请输入您的问题')
        q = input('输入问题：')

        queue = []
        # 在这一步的时候就要开始计算输入问题和存在问题的相似度了
        with open(self.path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                qa_pair = line.split(' ')
                qa_pair = (qa_pair[0].strip(' '), qa_pair[1].strip('\n').strip(' '))  # (问题，答案)元组
                # 此处计算文本相似度
                pre_sim = sim.predict(qa_pair[0], q)[0][1]
                if len(queue) < 3:
                    queue.append((qa_pair, pre_sim))
                else:
                    if pre_sim > queue[2][1]:
                        queue = queue[:-1]
                        queue.append((qa_pair, pre_sim))
                # 每次循环结束后，都重新对queue进行降序排列
                if queue:
                    queue = sorted(queue, key=lambda x: x[1], reverse=True)

        flag_done = False  # 用来标记是否匹配到了正确答案
        for i in range(len(queue)):
            print('您是否想问：' + queue[i][0][0])
            respose = input('您的回答：（请回答是/否）')
            if respose == '是':
                print(queue[i][0][1])
                flag_done = True
                break
        if not flag_done:
            print('很抱歉，小策不理解您的意思，请拨打客服电话。')


if __name__ == '__main__':
    data_dir = os.path.join(basepath, 'data/qa_corpus.txt')
    # q = '公司认证需要哪些材料'
    model = similarity(data_dir)
    model.mainProcess()