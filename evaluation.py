import os 
import numpy as np 
import pdb

wav_dirs = os.listdir("wav")
mos_dirs = os.listdir("wav/mos")
ballad_dirs = os.listdir("wav/mos/ballad")
child_dirs = os.listdir("wav/mos/child")

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

for c in child_dirs:
    model_name = c.split("_")[0]
    data_name = c[len(model_name)+1:]
    if model_name == "GT":
        GT_dict[data_name] = "wav/mos/child/"+c
    elif model_name == "NSinger":
        NSinger_dict[data_name] = "wav/mos/child/"+c
    elif model_name == "NSinger2Tune":
        NSinger2_dict[data_name] = "wav/mos/child/"+c

cnt = 1
dict_dict = {"GT": GT_dict, "NSinger": NSinger_dict, "NSinger2": NSinger2_dict}
for idx, key in enumerate(GT_dict.keys()):
    np.random.seed(idx)
    perm = np.random.permutation(["GT", "NSinger", "NSinger2"])
    dict1 = dict_dict[perm[0]]
    dict2 = dict_dict[perm[1]]
    dict3 = dict_dict[perm[2]]
    
    if idx == 0:
        with open("test.md", 'w') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict2[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict3[key]))
            cnt += 1
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
            
    else: 
        with open("test.md", 'a') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict2[key]))
            cnt += 1
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict3[key]))
            cnt += 1
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
