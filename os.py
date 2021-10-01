import os
path='H:\Downloads\archive (2)\train'
os.getcwd()
os.chdir('H:/Downloads/archive (2)/train/New folder/')

list_=os.listdir()

filenames=[]
annotations=[]

for file in list_:
    filenames.append(file)
    if(file.split('.')[0]=='cat'):
        annotations.append(0)
    else:
        annotations.append(1)
    
    
 

import pandas as pd
df=pd.DataFrame(list(zip(filenames,annotations)),columns=['FileName','Target'])
os.chdir('H:/Downloads/')
df.to_csv('catsAnddogs2.csv',index=False)
