import os
import pandas as pd
import re
import numpy as np
import pickle
# coding: utf-8
file = []
links = []
for root, dirs, files in os.walk('/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/', topdown=False):
    for name in files:
        if not name.endswith('.aln') and not name.endswith('.swp'):
            print(name)
            f = open(os.path.join(root, name), 'r')
            m = re.search(r'^\s\bQ-score\b\s+\:\s(?P<Qscore_value>\d+\.?\d+)\s+\n', f.read(), re.MULTILINE)
            if m:
                links.append({'fixed': name[0:5], 'moving': name[6:11], 'value': m.groups()[0]})
struc_name = []

for i in range(len(links)):
    if {'id': links[i].get('fixed')} not in struc_name:
        struc_name.append({'id': links[i].get('fixed')})
    if {'id': links[i].get('moving')} not in struc_name:
        struc_name.append({'id': links[i].get('moving')})
        
data = {'nodes': struc_name, 'links': links}

nodes = data['nodes']
names = [node['id'] for node in sorted(data['nodes'], key=lambda x: sorted(x))]
N = len(nodes)
df = pd.DataFrame(np.zeros((N, N)), index=names, columns=names)
for link in data['links']:
    df.at[link['fixed'], link['moving']] = link['value']
    df.at[link['moving'], link['fixed']] = link['value']
    
print(df)
pickle.dump(df,open('align.pkl','wb'))
