import pickle
import winreg
#import os
from ReinDeer.RD_pipeline import RDPipeline

def pipeline_config_dict(): 
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')#利用系统的链表
    Desktop_path = winreg.QueryValueEx(key, "Desktop")[0] + '\\data_dict.txt'#返回的是Unicode类型数据
    pipeline_config_dict = pickle.load(open(Desktop_path,'rb'))
    #if os.path.exists(Desktop_path):
        #os.remove(Desktop_path)
    return pipeline_config_dict

def pipeline_API_demo():
    print('pipeline ini')
    pipeline = RDPipeline(pipeline_config_dict())
    print('pipeline run')
    pipeline.run()

if __name__ == '__main__':
    print("pipeline API demo")
    print('train phase')
    pipeline_config_dict['pipeline_input_file_name'] = 'data_train'
    pipeline_config_dict['pipeline_phase_config'] = 'train'
    pipeline_API_demo()
    print('eval phase')
    pipeline_config_dict['pipeline_input_file_name'] = 'data_eval'
    pipeline_config_dict['pipeline_phase_config'] = 'eval'
    pipeline_API_demo()

