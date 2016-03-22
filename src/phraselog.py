# -*- coding:utf-8 -*- 
'''
Created on 2016年3月17日

@author: xuhshen
'''
import os, sys  
import csv
import numpy as np
# import re

LOG_PATH="logs"
ERR_LST="keyword.txt"
# RESULT="result.csv"
RESULT="result_ver1.csv"
isinstring = lambda x,y: 1 if (x in y) else 0

class log():
    def __init__(self,logpath=LOG_PATH,featurefile=ERR_LST,result=RESULT):
        self.logpath = self.get_abspath(logpath)
        self.featurefile = self.get_abspath(ERR_LST)
        self.rst = self.get_abspath(result)
    
    def get_abspath(self,name):
        abspath = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir,os.path.pardir,name))
        return abspath

    def get_files(self,):
        files = os.listdir(self.logpath)
        return files
    
    def get_errlst(self,):
        f = open(self.featurefile,'rb')
        return [i.strip() for i in f]
    
    def store_result(self,lst):
        f = open(self.rst,'wb')
        headers = self.get_errlst()
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        for item in lst:
            f_csv.writerow(item)
        return 
    
    def get_test_feature(self,logfile):
        f_strings = self.get_errlst()
        feature = [0]*len(f_strings)
        f = open(self.get_abspath(logfile))
        for line in f:
            for i in xrange(len(f_strings)):
                if isinstring(f_strings[i],line):
                    feature[i] = 1
                    continue
        return np.array(feature,dtype="int")
    
    def get_features(self,):
        features = []
        f_strings = self.get_errlst()
        for name in self.get_files():
            f_path = os.path.join(self.logpath,name)
            f = open(f_path)
            feature = [0]*len(f_strings)
            for line in f:
                for i in xrange(len(f_strings)):
                    if isinstring(f_strings[i],line):
                        feature[i] = 1
                        continue
            feature.append(name)
            features.append(feature)
            f.close()
        return features
    
    def filter_features(self,lst):
        rst = []
        rst_with_tag = []
        for i in lst:
            if i[:-1] not in rst:
                rst.append(i[:-1])
                rst_with_tag.append(i)
        return rst_with_tag 
    
    def forecast(self,test_feature):
        with open(self.rst) as f:
            f_csv = csv.reader(f)
            f_csv.next()
            rst = []
            for i in f_csv:
                test_feature
                fi = np.array(i[:-2],dtype="int")
                err = test_feature-fi
                rst.append([np.dot(err,err),i[-1]])
            rst.sort()
            print rst
                
# pattern = re.compile(r'hello')
# match = pattern.match('hello world!')

if __name__ == '__main__':
    lg = log()
#     feature = lg.get_features()
#     filted_feat = lg.filter_features(feature)
#     lg.store_result(filted_feat)
    test_feature = lg.get_test_feature("logs/1451293112914_89f3ea958b92bc6394f2dd27944bb08121b93e2c_feature_fast1_1451293112914_compile_10_console.html")
    lg.forecast(test_feature)
#     
    
    
    
    
    