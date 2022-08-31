import os
import subprocess
import sys
from subprocess import Popen, PIPE

def execute(command,e):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        process.wait(120*5)
    except:
        process.kill()
        print(e)
        return

    # Poll process for new output until finished
    return

if __name__ == '__main__':
    os.remove("scores.txt")
    os.remove("current_weight.txt")
    max_weight = 10
    for a in range(1, max_weight):
        for b in range(1, max_weight):
            for c in range(1, max_weight):
                for d in range(1, max_weight):
                    f = open("current_weight.txt", "a")
                    vector = str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + '\n'
                    f.write(vector)
                    f.close()

                    execute(
                        "python GameManager.py qLearnTest " +
                        str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + '\n')
