import pickle
import winreg
import json
#import os


def pipeline_config_dict(): 
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')#利用系统的链表
    Desktop_path = winreg.QueryValueEx(key, "Desktop")[0] + '\\data_dict.txt'#返回的是Unicode类型数据
    pipeline_config_dict = pickle.load(open(Desktop_path,'rb'))
    #if os.path.exists(Desktop_path):
        #os.remove(Desktop_path)
    return pipeline_config_dict


js = json.dumps(pipeline_config_dict(), indent=4)
print(pipeline_config_dict())



