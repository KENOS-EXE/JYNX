import jynx
import os
import request

print('checking for update')
time.sleep(5)
os.system('git pull')

jynx.submit(menu)
