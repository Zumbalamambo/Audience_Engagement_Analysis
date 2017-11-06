import csv
import os
import comman_utils as comman_utils
main_content = dict()
rowList = []
au_list = []
facs_calc = dict()
au_list_length =17
path = comman_utils.PATH_ANALYSIS_DIR
for _, dirnames, filenames in os.walk(path):
    for files in filenames:
        f=open(os.path.join(path,files),'r')
        rows = csv.reader(f, delimiter=',', quotechar='|')
        rowList = list(rows)
        rowList.pop(0)
        for row in rowList:
            key = files[:-4]+'_'+row[0]
            au_list = []
            au_list = row[10:27]
            main_content[key] = au_list

list_length = len(main_content)
au_avg = [0]*au_list_length

for key, value in main_content.items():
    for i in range(0, au_list_length):
        au_avg[i]+=float(value[i])
for i in range(0, au_list_length):
    au_avg[i] = au_avg[i] / list_length

# calculated AU
facs_calc[comman_utils.FACS_HAP] = au_avg[4]+au_avg[8] #6,12
facs_calc[comman_utils.FACS_SAD] = au_avg[0]+au_avg[2] + au_avg[10]  #1, 4, 15
facs_calc[comman_utils.FACS_SUR] = au_avg[0]+au_avg[1] +au_avg[3] +au_avg[15] #1,2,5,26
facs_calc[comman_utils.FACS_FER] = au_avg[0]+au_avg[1] + au_avg[2]+au_avg[3]+au_avg[5]+au_avg[12]+au_avg[15]
facs_calc[comman_utils.FACS_ANG] = au_avg[2]+au_avg[3]+au_avg[5]+au_avg[13] #6,12
facs_calc[comman_utils.FACS_DIS] = au_avg[6]+ au_avg[10]  #1, 4, 15
facs_calc[comman_utils.FACS_CON] = au_avg[8] + au_avg[9]  #1, 4, 15
print(max(facs_calc.keys(), key=(lambda key: facs_calc[key])))
print("hello")