import winsound
# Frequency and duration in milliseconds
winsound.Beep(1000, 500)  # 1000 Hz for 500 ms


import os
# Works on most UNIX systems and Windows
os.system('echo -e "\a"')  # On Unix-based systems
# os.system('echo \a')  # On Windows, the echo command will beep


print('\a')
