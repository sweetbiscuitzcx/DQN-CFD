def discounted_returns(returns, gamma=0.5):
    G = 0
    for i in range(len(returns)):
        G += returns[i] * gamma ** i
    return G


import json
import os

import platform
sys_platform = platform.system()


def getRootPath(projectRootName):
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    if sys_platform == 'Windows':
        # Win10 environment prefix
        rootPath = curPath[:curPath.find(projectRootName+"\\")+len(projectRootName+"\\")]
    elif sys_platform == 'Linux':
        # Linux environment prefix
        rootPath = curPath[:curPath.find(projectRootName+"/")+len(projectRootName+"/")]
    else:
        rootPath = " "
        print('path error')
    print("add path :" + rootPath)
    return rootPath

def getMassFraction(T, RH):
    """
        Molecular mass fraction of air and water corresponding to temperature and humidity
    :param T: Temperature at a point in the room
    :param RH: Humidity at a certain point in the room
    :return MFdata: Molecular mass fraction of air and water
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + "/MFdata.json", 'r') as f:
        data = json.load(f)
        T = str(T)
        RH = str(RH)

        # hum_ratio is moisture content
        hum_ratio = data[T][RH]
        h2o_ratio = float(hum_ratio) / 1000
        h2o_ratio = round(h2o_ratio, 7)
        air_ratio = float(1) - h2o_ratio

        # Format data
        MFdata = '{' + str(h2o_ratio) + ',' + str(air_ratio) + '}'

        return MFdata

import sys
import time


# Console output recorded to file
class Logger(object):
    def __init__(self, file_name="Default.log", stream=sys.stdout):
        self.terminal = stream
        self.log = open(file_name, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def log():
    # Log file location setting
    log_path = 'out/logs/'
    # The log file name is set according to the program running time
    log_file_name = log_path + 'log-' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.log'
    # Record normal print information
    sys.stdout = Logger(log_file_name)
    # Record traceback exception information
    sys.stderr = Logger(log_file_name)


from .gymProfile import *


def checkExistFile():
    # Delete history files
    if os.path.exists(episode_reward_history_csv):
        os.remove(episode_reward_history_csv)
    if os.path.exists(each_episode_rewards_history_csv):
        os.remove(each_episode_rewards_history_csv)
    if os.path.exists(FanPower_history_csv):
        os.remove(FanPower_history_csv)
    if os.path.exists(each_FanPower_history_csv):
        os.remove(each_FanPower_history_csv)
    if os.path.exists(Loss_history_csv):
        os.remove(Loss_history_csv)

