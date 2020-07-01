# -*- coding: utf-8 -*-

'''
@Author  :   Bruce
 
@Software:   PyCharm
 
@File    :   test.py
 
@Time    :   2020-6-28
 
@Desc    :  本代码的目的是请用户在输入端输入问题，模型将与输入问题最相近的问题输出，由用户来选择是否该问题正确；
            若正确，则返回答案；若不正确，则提示用户新的问题；如果连续5个问题用户还不能确认提示的问题，则转接人工服务
'''

from run_similarity import BertSim
import tensorflow as tf


sim = BertSim()

if True:
    sim.set_mode(tf.estimator.ModeKeys.PREDICT)
    sentence2_set = ['认证时需要上传什么东西？', '如何进行认证？', '在哪里可以找到认证的页面？', '哪里可以认证？', '认证中要经历哪些过程？']
    print('\n' + '请输入您的问题')
    question = input('输入问题：')
    Q_sim = []
    for sen in sentence2_set:
        predict = sim.predict(question, sen)
        Q_sim.append((sen, predict[0][1]))
    Q_sim = sorted(Q_sim, key=lambda x: x[1], reverse=True)
    # print('----------------------------------------------------------------------')
    print('输入句子为【' + question + '】')
    n = 3  # 总共记录用户的3次判断
    for i in range(len(Q_sim)):
        # print('与【' + pair[0] + '】相似度的为：' + str(pair[1]))
        if i < 3:
            print('您是否想问：' + Q_sim[i][0])
            respose = input('您的回答：（请回答是/否）')
            if respose == '是':
                print('答案是......')
                break
        else:
            print('很抱歉，小策不理解您的意思，请拨打客服电话。')
            break