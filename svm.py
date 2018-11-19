#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn import svm
from urllib import unquote
from sklearn.externals import joblib


xss_file_path = '/Users/jeary/Desktop/xss_sample2.txt';
xss_sample_path = '/Users/jeary/Desktop/xss_sample.txt';
safe_file_path ='/Users/jeary/Desktop/result_safe_log2.txt';
model_student = '/Users/jeary/Desktop/lr.model'

def vector(req_url):
    key = ["script", "iframe", "javascript", "<", ">", "\"", "\'", "%", "(", ")", "xss", "marquee", "alert", "svg",
           "body", "onload", "confirm", "cookie", "document", "getelementbyid", "createelement", "onabort", "onblur",
           "onchange", "onclick", "ondblClick", "ondragdrop", "onerror", "onfocus", "onkeyDown", "onkeypress",
           "onkeyup", "onmousedown", "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmove", "onreset",
           "onresize", "onselect", "onsubmit", "expression", "prompt", "eval", "embed", "object", "createEvent",
           "style", "{", "}", "function"]
    try:
        result = []
        req_url = unquote(str(req_url))
        for s in key:
            result.append(req_url.count(s))
        return result
    except:
        print "转码错误!"


if __name__ == '__main__':
    xssfile = open(xss_file_path, 'r')
    xss_sample = open(xss_sample_path,'wb+')
    X = []
    y = []
    for line in (xssfile):
        try:
            line = unquote(str(line))

            result = vector(line)
            found = 0
            #去重复代码
            # for k in range(0, len(X)):
            #     if result == X[k]:
            #         found = 1
            #         break
            # if found == 0:
            found = result.count(0)
            if found<45:
                X.append(result)
                xss_sample.write(line.strip()+"\n")
        except:
            xssfile.close()
    xssfile.close()
    xss_sample.close()
    print "样本数量:"+str(len(X))
    for t in range(0, len(X)):
        y.append(1)

    #result_safe_log.txt
    safe_file = open(safe_file_path, 'r')
    for safe_log in safe_file:
        X.append(vector(safe_file))
        y.append(0)
    safe_file.close()
    #print "X长度:"+str(len(X))
    #print "y长度:" + str(len(y))

    clf = svm.SVC(kernel='linear', C=1000)
    clf.fit(X, y)

    joblib.dump(clf, model_student)
    print '模型已训练完成,'+model_student





