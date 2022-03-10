import os 
import numpy as np 
import pdb

wav_dirs = os.listdir("wav")
mos_dirs = os.listdir("wav/mos")
ballad_dirs = os.listdir("wav/mos/ballad")

GT_dict = dict()
NSinger_dict = dict()
NSinger2_dict = dict()
for d in ballad_dirs:
    model_name = d.split("_")[0]
    data_name = d[len(model_name)+1:]
    if model_name == "GT":
        GT_dict[data_name] = "wav/mos/ballad/"+d
    elif model_name == "NSinger":
        NSinger_dict[data_name] = "wav/mos/ballad/"+d
    elif model_name == "NSinger2Aug":
        NSinger2_dict[data_name] = "wav/mos/ballad/"+d

cnt = 1
for idx, key in enumerate(GT_dict.keys()):
    if idx == 0:
        with open("test.md", 'w') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, GT_dict[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, NSinger_dict[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, NSinger2_dict[key]))
            cnt += 1
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
            
    else: 
        with open("test.md", 'a') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, GT_dict[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, NSinger_dict[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, NSinger2_dict[key]))
            cnt += 1
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
