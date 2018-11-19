#coding: utf-8
import sys
from sklearn import svm
from urllib import unquote


def vector(key,req_url):
    try:
        result = []
        req_url = unquote(str(req_url).lower())
        for s in key:
            result.append(req_url.count(s))
        return result
    except:
        print "转码错误!"


if __name__ == '__main__':
    X = []
    y = []

    xss = ["script", "iframe", "javascript", "<", ">", "\"", "\'", "%", "(", ")"]
    sql = ["select","union","char","concat","count","from","where","group"]
    code = ["eval","phpinfo","print","base64_decode","md5","assert","system","passthru"]

    #xss_file = open("/Users/jeary/Desktop/100xss.txt","r")
    #for xss in xss_file:
    #    xss_vector = vector(xss, xss)

    #req_url = "/index.php?keyword=Search...<script src=http://xxooxxoo.js></script>";
    req_url = "/index.php?keyword=Search...scriptscript<<>>";
    c = vector(xss,req_url)
    print c