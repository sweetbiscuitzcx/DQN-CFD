"""

    Define and call the Starcom command to set the host and port number of the server
    for easy connection and keep it running in the background.

    See user guide for specific command query: https://volupe.se/simcenter-star-ccm-documentation-a-guide-to-success/

"""


import socket


host_name = socket.gethostname()
from solutions.utils import sys_platform
if sys_platform == 'Windows':
    # Win10 environment prefix
    ospath = 'starccm+ '
elif sys_platform == 'Linux':
    # Linux environment prefix
    ospath = '/opt/Siemens/14.02.010-R8/STAR-CCM+14.02.010-R8/star/bin/starccm+ '
else:
    ospath = " "
    print('other')

# The command prefix of the star-ccm+ server
ospath_server = ospath + " -server "
# Command prefix for the star-ccm+ client
ospath_batch = ospath + " -batch "
# Sim file of simulation environment
simulink_file_Name = ' humidity.sim '
# The host name of the code you want to run

host_name_YOUR = ' -host ' + host_name + ' '

import random

#  Port number of client and server in star-ccm+
port_num = ' -port 48' + str(random.randint(100, 1000)) + ' '

# port_num = ' -port 47827 '

# Do not close the server after the client executes the macro file
Noexit = ' -noexit '
# Do not echo console output information
noecho = ' >NUL 2>NUL '
# Path for storing java macro files
javafilepath = './javafile/'
# Reset the Java macro file of the simulation environment
resetfilename = javafilepath + 'reset.java'
resetfile = javafilepath + 'reset.java,'
# Modify and run the Java macro file of one-step simulation environment

editandrunfile = javafilepath + 'editandrun_15.java'
# editandrunfile = javafilepath + 'editandrun_9.java'
# editandrunfile = javafilepath + 'editandrun.java'

'''
    Continuously call Java macro files
'''
editandrun_str = javafilepath + "checkinfo.java," + editandrunfile + ","
# Csv file generated by Python calling Java macro file
RHfile = javafilepath + "RHfile.csv"

"""

    Open the star-ccm+ server statement:  starccm+ -server filename.sim -port 48000 

"""
start_starccm_server = ospath_server + simulink_file_Name + port_num

"""

    Open the star-ccm+ client and call the macro file statement:  starccm+ -batch filename.java  -host your_host -port your_port 
    
"""
# Host and port numbers and other functions
NoexitAndHostPort = Noexit + host_name_YOUR + port_num
# # Reset Simulation Environment Statements
# reset_gymGame_command = ospath_batch + resetfilename + NoexitAndHostPort
# # Execute the one-step statement of the simulation environment
# runOneStep_gymGame_command = ospath_batch + editandrunfile + NoexitAndHostPort

# runforStep_gymGame_command = ospath_batch + editandrun_str * 20 + NoexitAndHostPort

# 21 stands for executing macro commands of editandrun_str for 21 times.
# The first step is the step of environment initialization,
# and the next 20 steps are the steps of a subsequent simulation round
runforStep_gymGame_command = ospath_batch + resetfile + editandrun_str * 21 + NoexitAndHostPort + noecho

runforStepTest_gymGame_command = ospath_batch + editandrun_str * 51 + NoexitAndHostPort

runforStepTest_100step = ospath_batch + editandrun_str * 101 + NoexitAndHostPort
"""
    
    Used to save the path of the reward and FanPower files
    
"""
savefilepath = 'out/'
# Record the change table of 'Reward total' with the number of rounds
episode_reward_history_csv = savefilepath + "episode_reward_history.csv"
# Record the change table of reward with the number of steps in each round
each_episode_rewards_history_csv = savefilepath + "each_episode_rewards_history.csv"
# Record the change table of 'FanPower total' with the number of rounds
FanPower_history_csv = savefilepath + "FanPower_history.csv"
# Record the change table of fanpower with the number of steps in each round
each_FanPower_history_csv = savefilepath + "each_FanPower_history.csv"

Loss_history_csv = savefilepath + "Loss_history.csv"
