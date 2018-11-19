#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sklearn.externals import joblib
from svm import vector
import re

log = "http://www.thebugs.ws/search.shtml?q=<script>alert(\"m\")</script>"
def xss_detail(user_input):
    clf = joblib.load('lr.model')
    input_vector = [vector(user_input)]
    print "特征向量:"+str(input_vector)
    t_store = clf.predict(input_vector)
    if t_store == 1:
        return True
    return False

if __name__ == '__main__':
    print "日志:"+log
    is_xss =  xss_detail(log)
    if is_xss:
        print "识别结果:XSS攻击"
    else:
        print "识别结果:正常"    






    # clf = joblib.load('lr.model')
    # xss_file = open("/Users/jeary/Documents/selfwork/20170922/5w_xss.txt","r")
    # for xss in xss_file:
    #     str_xss = re.split('\d+:',xss)[1]
    #     T = [vector(str_xss)]
    #     #print T
    #     Tn = clf.predict(T)
    #     if Tn == 1:
    #         print "XSS攻击:" + str_xss
    #         print T
    #         print Tn
    #     else:
    #         print "正常请求:" + str_xss

