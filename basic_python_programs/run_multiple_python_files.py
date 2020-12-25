import glob
import subprocess
runnable_list = []
list_file_names = glob.glob("/dir_name/*.py") # directory name which contains multiple python files


def populate_list():
    for i in list_file_names:
        runnable_list.append(i.replace(' ', '\ '))  # to replace ' ' with '\ ' to make it runnable on terminal
    list_file_names.clear()
    print('Programs To run ', runnable_list)
    return runnable_list


def run_programs():
    run_list = populate_list()
    for i_runnable in run_list:
        print('Execution Started')
        cmd = 'python3 '+i_runnable
        print(cmd)
        subprocess.run(cmd, shell=True)
        print('Execution Completed')


run_programs()
