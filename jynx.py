import jynx
import os
import request

print('checking for update')
time.sleep()
os.system('git pull')

jynx.submit(menu)
