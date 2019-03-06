# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:15:27 2019

@author: xutao
"""
import json
import ast
import pickle
import winreg 

#import sys
#sys.path.append(r'C://Users//xutao//test')

from app import Parameter

# 测试数据
f = open('select.txt')
test_data = ast.literal_eval(f.read()[1:-1])

# 选择标志
select_list = ['s1', 'stage_user_defined_feature_columns_name2', 'stage_user_defined_feature_columns_name3', 'stage_user_defined_feature_columns_name4']


# 获取数据库数据
def DB_data():
    #parameter = Parameter.query.first()
    #data = {}
    #data[str(parameter.name)] = parameter.value

    # 新建stage参数字典
    stage_param_dict = {}
    # 数据库参数数据
    num = Parameter.query.count()
    
    i = 0 #循环计数
    while i < num:
        i +=1
        data = Parameter.query.get(i)
        stage_param_dict[str(data.name)] = data.value

    return stage_param_dict


# 处理数据形式函数
def test(data_dict):
    # 返回当前stage数据条目化并列表化
    stage_data_list = list(data_dict.items())

    #stage_data_len = len(stage_data_list)
    result = {}  # 设结果字典
    
    # 通过是否有stage_user_defined_feature_columns_name 区分处理方式
    if stage_data_list[2][0][:-1] != 'stage_user_defined_feature_columns_name':
        #result[stage_data_list[1][0]] = stage_data_list[1][1]
        
        # 向结果字典添加stage_backend、stage_name两项参数
        result['stage_backend'] = stage_data_list[2][1]
        stage_name = stage_data_list[4][1].split('-')[2]
        result['stage_name'] = stage_name
        
        # 新建参数字典
        stage_param_dict = {}
        # 对参数相开始循环处理  后期可以用循环判定的方式 不然位数不见得正确
        for data in stage_data_list[6:]:
            stage_param_dict[data[0].split('-')[4]] = data[1]
        
        # 然后将参数字典放入结果字典的
        result[stage_data_list[0][0]] = stage_data_list[0][1]
        result[stage_data_list[1][0]] = stage_param_dict
    
    # 如果不是首stage的话
    else:
        # 向结果字典添加stage_backend、stage_name两项参数
        result['stage_backend'] = stage_data_list[3][1]
        stage_name = stage_data_list[5][1].split('-')[2]
        result['stage_name'] = stage_name
    
        # 新建参数字典
        stage_param_dict = {}
    
        # 对参数数据行循环处理
        for data in stage_data_list[7:]:
            #print(data[0].split('-'))
            stage_param_dict[data[0].split('-')[4]] = data[1]
    
        # 然后将参数字典放入结果字典的
        result[stage_data_list[0][0]] = stage_data_list[0][1]
        result[stage_data_list[1][0]] = stage_param_dict
    
        # stage_user_defined_feature_columns_name 数据添加
        stage_user_defined_feature_columns_name = stage_data_list[2][0][:-1]
        stage_user_defined_feature_columns_name_list = list((stage_data_list[2][1]).split(' '))
        name_list = [] # 循环处理name
        for columns_name in stage_user_defined_feature_columns_name_list:
            if columns_name == '':
                continue
            else:
                name_list.append(columns_name)
        result[stage_user_defined_feature_columns_name] = name_list
        
    return result

    



data_dict = test_data # 获取测试数据字典
data_len = len(data_dict) # 获取数据字典长度

# 数据key值列表  value值列表
data_key = []
data_value = []
for data in data_dict:
    data_key.append(data)
    data_value.append(data_dict[data])

# 获取测试数据条目列表
data_item_list = list(data_dict.items())

# 所需设置
stage_data_dict = {} # stage总数据字典
result_list = [] # 

#stage_name_dict = {'key':'stage1_config_dict'}
stage_name_dict = {} # stage名字字典
stage_name_str = '' # stage_name比较储存
pipeline_stages_config_dict = [] # pipeline_stages_config_dict参数预留

# 获取数据函数json
def SE_data():
    stage = 1 # stage计数
    # 按数据长度循环所有数据
    for i in range(data_len): 

        # 获取当前i的key 和 value两个值
        key = data_key[i]
        value = data_value[i]
    
        # 对key进行判定，是否为stage开头标志
        if key in select_list:
            if key == 's1': # 如果是第一个
        
                # 当前i为stage数据首项的取值 往后挪四位 可以获取stage_name取值
                e = i + 4
                if len(data_item_list[e][0].split('-')) > 1:
                    data_item = data_item_list[e][0].split('-')[3] # 取到stage_name的值
                    stage_name_str = data_item # 储存stage_name字符串

                    stage_name = 'stage1_config_dict' # 第一个stage数据字典  手动定义 用于比较
                    stage_dict = 'stage1_config_dict' # 用于生成字典名
                    stage_dict = {} # 新建数据字典
            
                    # stage_param_dict的数据
                    stage_param_dict = 'stage_param_dict' + str(int(stage))
                    #pipeline_stages_config_dict.append(stage_param_dict)  #另一种直接的形式
                    stage_dict['stage_param_dict'] = stage_param_dict
            
                    # 第一个stage特殊处理 在此添加参数  stage名字字典  stage1_config_dict
                    stage_name_dict['key'] = stage_name 
            
                    # 具体参数字典提前占位
                    stage_dict[str(stage_param_dict)] = '' 

                # 否则 如果没有参数 则
                else:
                    e = i + 2
                    data_item = data_item_list[e][1].split('-')[2]
                    stage_name_str = data_item # 储存stage_name字符串

                    stage_name = 'stage1_config_dict' # 第一个stage数据字典  手动定义 用于比较
                    stage_dict = 'stage1_config_dict' # 用于生成字典名
                    stage_dict = {} # 新建数据字典        
        
                    # stage_param_dict的数据
                    stage_param_dict = 'stage_param_dict' + str(int(stage))
                    #pipeline_stages_config_dict.append(stage_param_dict)  #另一种直接的形式
                    stage_dict['stage_param_dict'] = stage_param_dict
 
                    # 第一个stage特殊处理 在此添加参数  stage名字字典  stage1_config_dict
                    stage_name_dict['key'] = stage_name 
            
                    # 具体参数字典提前占位
                    stage_dict[str(stage_param_dict)] = '' 
      
            # 否则不是第一个stage
            else:
                stage += 1 # stage自增
            
                # 如果有stage_user_defined_feature_columns_name
                # 此时具体名为当前的 s

                #形成当前的字典名
                stage_name = 'stage' + str(int(stage)) + '_config_dict'
                stage_dict = 'stage' + str(int(stage)) + '_config_dict'
                stage_dict = {} #进行新建
            
                # stage_param_dict的数据
                stage_param_dict = 'stage_param_dict' + str(int(stage))
                #pipeline_stages_config_dict.append(stage_param_dict)
                stage_dict['stage_param_dict'] = stage_param_dict
            
                # 具体参数字典提前占位
                stage_dict[str(stage_param_dict)] = ''   
    
        # 添加每条数据
        if key != 's1' and key in select_list: # 如果新换stage 生成前台数据数据与例行数据组合
            stage_dict[key] = value + ' stage' + str(int(stage) - 1) + '_' + str(stage_name_str)
        
            # 然后更新data_item

            e = i + 3
            if len(data_item_list[e][0].split('-')) > 1:
                data_item = data_item_list[e][0].split('-')[3]
            else:
                e = i + 3
                data_item = data_item_list[e][1].split('-')[2]
            
            stage_name_str = data_item # 储存stage_name列表
        else:
            stage_dict[key] = value # 否则正常添加数据

        # 数据添加result_list
        result_list.append(stage_dict)
    
        if stage_name_dict['key'] != stage_name or i == data_len - 1: # 如果不相等 证明换stage了
            i -= 1 # 获取上一个stage最后完整的结果字典序号
            stage_data = result_list[i]
        
            #在这里对一个字典进行处理
        
            stage_data_dict[stage_name_dict['key']] = test(stage_data)
            stage_name_dict['key'] = stage_name   

    result = {}
    result['pipeline_stages_config_dict'] = stage_data_dict
    return result


def result_json_data():
    # json形式输出结果
    result = DB_data()
    result['pipeline_stages_config_dict'] = SE_data()

    js = json.dumps(result, indent=4)
    return js

def get_desktop(): 
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')#利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0] #返回的是Unicode类型数据

def read_data():
    data = json.loads(result_json_data())
    Desktop_path=str(get_desktop()) + '\\data_dict.txt'#Unicode转化为str
    pickle.dump(data,open(Desktop_path,'wb'))

read_data()