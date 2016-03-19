# -*- coding:utf-8 -*- 
'''
Created on 2016年3月17日

@author: xuhshen
'''
import os, sys  
# import re

LOG_PATH="logs"
ERR_LST="keyword.txt"
isinstring = lambda x,y: 1 if (x in y) else 0

class log():
    def __init__(self,logpath=LOG_PATH,featurefile=ERR_LST):
        self.logpath = self.get_abspath(logpath)
        self.featurefile = self.get_abspath(ERR_LST)
    
    def get_abspath(self,name):
        abspath = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir,os.path.pardir,name))
        return abspath

    def get_files(self,):
        files = os.listdir(self.logpath)
        return files
    
    def get_errlst(self,):
        f = open(self.featurefile,'rb')
        return [i.strip() for i in f]
    
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
        features.sort() 
        for i in  features:
            print i
                    
                    

# pattern = re.compile(r'hello')
# match = pattern.match('hello world!')



if __name__ == '__main__':
    lg = log()
    lg.get_features()
#     
    
    
    
    
    