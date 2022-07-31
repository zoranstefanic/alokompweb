from alignments.populate import *
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
Alignment.objects.last()
a = Alignment.objects.last()
a.chain_fixed
Alignment.objects.filter(chain_fixed=a.chain_fixed)
Alignment.objects.filter(chain_fixed=a.chain_fixed).count()
Alignment.objects.filter(chain_moving=a.chain_fixed).count()
import random
random.choice(Alignment.objects.all())
a = random.choice(Alignment.objects.all())
Alignment.objects.filter(chain_fixed=a.chain_fixed)
Alignment.objects.filter(chain_fixed=a.chain_fixed).count()
Alignment.objects.filter(chain_moving=a.chain_fixed).count()
a = random.choice(Alignment.objects.all())
Alignment.objects.filter(chain_moving=a.chain_fixed).count()
Alignment.objects.filter(chain_fixed=a.chain_fixed).count()
a = random.choice(Alignment.objects.all())
Alignment.objects.filter(chain_fixed=a.chain_fixed).count()
Alignment.objects.filter(chain_moving=a.chain_fixed).count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
%timeit ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
%timeit ResidueMatch.objects.count()
%timeit ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
%timeit ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
%timeit ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
Chain.objects.count()
import pandas as pd
import bokeh
c = Chain.objects.last()
c
c.residues.count()
c.pdb
c.pdb.title
for r in c.residues.all():
    print r
for r in c.residues.all():
    print(r)
r
c.pdb.title
c.alignments_fixed
c.alignments_fixed.all()
c.alignments_moving.all()
c.alignments_moving.count()
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore)
ls
ls
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore)
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore, a.seq_identity)
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore, a.seq_identity, a.aligned_num)
a
a.positions.all()
a.positions.count()
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore, a.seq_identity, a.aligned_num)
for a in c.alignments_moving.order_by('-Qscore'):
    print(a, a.Qscore, a.seq_identity, a.aligned_num)
import pandas as pd
df = pd.DataFrame()
df
Alignment.objects.count()
c
c.alignments_fixed
c.alignments_fixed.count()
a
a.chain_fixed_id
a.chain_moving_id
import numpy as np
np.eye(20)
df.columns
df.columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned']
df.columns
df.append?
l = []
for a in Alignment.objects.all()"
for a in Alignment.objects.all():
    print(a.chain_fixed,a.chain_moving,a.Qscore,a.rmsd,a.aligned_num,a.seq_identity)
l
for a in Alignment.objects.all():
    l.append([a.chain_fixed,a.chain_moving,a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
l
/len l
c
repr(c)
c.__str__()
str(c)
l = []
l = [[str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity] for a in Alignment.objects.all()]
l
for a in list(Alignment.objects.all())[:1000]:
    l.append([a.chain_fixed,a.chain_moving,a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
l
/len l
/len l
for a in list(Alignment.objects.all())[:10000]:
    l.append([a.chain_fixed,a.chain_moving,a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
l
/len l
l = []
for a in Alignment.objects.all():
    l.append([a.chain_fixed,a.chain_moving,a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
l
/len l
d = pd.DataFrame(l)
d
%history
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
d
import pickle
pickle.dump?
pickle.dump(d,open('alignments.pkl','wb'))
ls
ll
ll -rth
Alignment.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ls
d
d
d[:100]
d[d[0]=='1q1g-F']
d[d[1]=='1q1g-F']
d[0]
d
d.0
ResidueMatch.objects.count()
ResidueMatch.objects.count()
d
d['Cfixed']
d['Cfixed'][0]
fixed = d['Cfixed']
fixed.unique?
fixed.unique()
fixed.unique().length()
len(fixed.unique())
fixed[0]
c = fixed[0]
c.residues
c.residues.all()
c.residues[0]
c.residues.first()
r = c.residues.first()
r
r.atoms.all()
fixed = d['Cfixed']
d
d
fixed
fixed.sort_values?
fixed.sort_values()
fixed
fixed_str = fixed.map(str)
fixed_str
fixed_str[0]
type(fixed_str[0])
fixed_str.sort_values()
fixed_str.sort_values().unique()
chain_names = fixed_str.sort_values().unique()
/len chain_names
ResidueMatch.objects.count()
d
d.head()
d
d.Qscore
d.RMSD
594^2
594^^2
594**2
594**2/2
594*593/2
594*593/2 + 594
d
dd = pd.DataFrame(columns=chain_names)
dd
dd.shape
dd
dd.head
dd.index
dd = pd.DataFrame(columns=chain_names,index=chain_names)
dd
dd
dd['1a69-A'][0]
dd['1a69-A']['1a69-A']
dd['1a69-A']['1a69-A'] = 1
dd
d
d.Cfixed
d[d.Cfixed='1qig-F']
d[d.Cfixed=='1qig-F']
d.Cfixed = d.map(str,d.Cfixed)
d
dd
d.Cfixed.
d.Cfixed
d.Cfixed
d.Cfixed[0]
c = d.Cfixed[0]
c
c.pdb
c.pdb.code
c.chain_id
c
d
dd
d.Cfixed = map(str,d.Cfixed)
d
map?
d
d = pd.DataFrame()
d
for a in Alignment.objects.all():
    l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
d
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
dd = pd.DataFrame(columns=d.Cmoving,index=d.Cfixed)
d
chain_names = d.Cfixed.sort_values().unique()
d
d.Cfixed
d = pd.DataFrame()
d
l
l = []
for a in Alignment.objects.all():
    l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
dd = pd.DataFrame(columns=d.Cmoving,index=d.Cfixed)
chain_names = d.Cfixed.sort_values().unique()
chain_names
dd = pd.DataFrame(columns=d.Cmoving.sort_values().unique(),index=d.Cfixed.sort_values().unique())
dd
d
d[d.Cfixed="1q1g-F"]
d[d.Cfixed=="1q1g-F"]
%timeit d[d.Cfixed=="1q1g-F"]
ResidueMatch.objects.count()
%timeit d[d.Cmoving=="1q1g-F"]
d[d.Cmoving=="1q1g-F"]
d.loc?
d.loc[Cfixed="1q1g-F"]
d.loc(Cfixed="1q1g-F")
d.loc?
d.loc["1q1g-F"]
d
dd
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
dd
d
dd
dd
d
d
ResidueMatch.objects.count()
d.Cmoving.value_counts()
d.Cfixed.value_counts()
dd
d
d.loc?
d
d.loc[1:2]
d.loc[0:2]
d.loc[d[Cfixed]=="1q1g-F"]
d.loc[d['Cfixed']=="1q1g-F"]
d.loc[d.Cfixed=="1q1g-F"]
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving="3uaz-A']
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A']
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A"]
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A"].Qscore
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A"].Qscore[0]
dd
ResidueMatch.objects.count()
Residue.objects.count()
Residue.objects.last()
r = Residue.objects.first()
r
r.pdb
r.chain_id
r.chain
r.matches_fixed.count()
r.matches_moving.count()
import random
Residue.objects.all()
r = random.choice(Residue.objects.all())
r
r.matches_moving.count()
r.matches_fixed.all()
r.matches_moving.all()
r.matches_moving.values_list('alignments')
r.matches_moving.values_list('alignment')
r.matches_moving.values_list('alignment__chain')
r.matches_moving.values_list('alignment__fixed')
r.matches_moving.values_list('alignment__chain_fixed')
r.matches_moving.values_list('alignment__position')
r.matches_moving.values_list('alignment__positions')
/len r.matches_moving.values_list('alignment__positions')
r = random.choice(Residue.objects.all())
/len r.matches_moving.values_list('alignment__positions')
r = random.choice(Residue.objects.all())
/len r.matches_moving.values_list('alignment__positions')
/len r.matches_moving.values_list('alignment')
r.matches_moving.values_list('alignment')
d
dd
c
c.residues.all()
Residue.objects.all()
ResidueMatch.objects.count()
r = random.choice(Residue.objects.all())
Residue.objects.all()
Residue.objects.count()
r
r.chain
r.matches_moving.all()
r.matches_moving.count()
r.matches_fixed.count()
r = random.choice(Residue.objects.all())
r.matches_fixed.count()
r.matches_moving.count()
r.matches_moving.all()
r
for r in r.matches_moving.all():
    print r
for r in r.matches_moving.all():
    print(r)
r
r.alignment
for r in r.matches_moving.all():
    print(r.alignment)
for r in r.matches_moving.all():
    print r
for r in r.matches_moving.all():
    print(r)
r
r = random.choice(Residue.objects.all())
r
for r in r.matches_moving.all():
    print(r)
for r in r.matches_moving.all():
    print(r.alignment)
r = random.choice(Residue.objects.all())
for j in r.matches_moving.all():
    print(j.alignment)
r = random.choice(Residue.objects.all())
for j in r.matches_moving.all():
    print(j.alignment)
d
dd
d.loc[d.Cfixed=="1q1g-F"]
d.loc[d.Cmoving=="1q1g-F"]
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A"].Qscore[0]
#dataframe = pd.DataFrame()
d.Cfixed
dataframe = pd.DataFrame(d.Cfixed, d.Cmoving, d.Qscore)
d.Cfixed
dataframe = d[0:2]
dataframe
dataframe = d[::0:2]
dataframe = d[:0:2]
dataframe
dataframe = d[0:2:]
dataframe
dataframe = d[0:2:8]
dataframe
d
d
d.loc[d.Cfixed=="1q1g-F"].loc[d.Cmoving=="3uaz-A"].Qscore[0]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="3uaz-A"].Qscore[0]
dd
d
d.loc[d.Cfixed=="1q1g-D"]
pickle.dump(d,open('alignments.pkl','wb'))
ls -lrt
ls -lrth
cd alignments/
cd -
ls
d
dd
pdb
pdb
c
c.pdb
c.pdb.data
from pdbase.models import Pdb
Pdb.objects.all()
for pdb in Pdb.objects.all():
    print(pdb,pdb.data['number_of_copies'])
pdb
pdb.data
d
dd
chain_names
chain_names.len
chain_names.len()
/len chain_names
d
dd
ddd = dd.copy()
ddd
ddd['1a69-A']
ddd
ddd[0]
dd
dd['1a69-A']
dd[0]
d
d[0]
d[:1]
d
dd
d[:100]
d[d.Cfixed=='1q1g-F']
d[d.Cfixed=='1q1g-F'].sort_values('Cmoving')
d[d.Cfixed=='1q1g-F'].sort_values('Qscore')
Residue.objects.count()
ResidueMatch.objects.count()
dd
fixed_names = d.Cfixed.sort_values().unique()
moving_names = d.Cmoving.sort_values().unique()
for n in fixed_namesČ
for f in fixed_names:
    for m in moving_names:
        print(n,m)
for f in fixed_names:
    for m in moving_names:
        print(f,m)
d
dd
for f in fixed_names[:2]:
    for m in moving_names[:2]:
        print(f,m)
dd(0)
dd[0]
dd[0::]
dd[0:]
dd[:0:]
dd[q:0:]
dd[1:0:]
dd[1:1:]
dd[1:1:1]
dd
d
for f in fixed_names[:2]:
    for m in moving_names[:2]:
        print(f,m)
d[['Cfixed','Cmoving']]
dd[d[['Cfixed','Cmoving']]]
dd
d[['Cfixed','Cmoving']]
d['Cfixed']
fixed_chains = d['Cfixed']
d
dd
dd.shape
dd
d
dd['1a69-B']['1a69-C']
dd['1a69-B']
d.Cfixed
d
dd
d.Cfixed[d.Cfixed=='1a69-A']
d.Cmoving[d.Cfixed=='1a69-A']
dd
d
dd.at['1a69-B','1a69-A'] = 10
dd
dd.at['1a69-B','1a69-A'] = d.loc[d.Cfixed=='1a69-B'].loc[d.Cmoving=='1a69-A'].Qscore[0]
dd
d
dd[d[['Cfixed','Cmoving']]]
d[['Cfixed','Cmoving']]
for f in fixed_names[:2]:
    for m in moving_names[:2]:
        print(f,m)
d.loc[d.Cfixed=="1q1g-D"]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"]
type(d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"])
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore[0]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore
type(d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore)
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore[4]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"]['Qscore']
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"]['Qscore'][0]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"][4]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].iloc[0]
d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore.iloc[0]
for f in fixed_names:
    for m in moving_names:
        print(n,m)
for f in fixed_names:
    for m in moving_names:
        print(f,m)
#dd.at[f][m] = d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore.iloc[0]
for f in fixed_names:
    for m in moving_names:
        print(f,m)
        dd.at[f][m] = d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore.iloc[0]
f
m
for f in fixed_names:
    for m in moving_names:
        print(f,m)
        dd.at[f,m] = d.loc[d.Cfixed=="1q1g-D"].loc[d.Cmoving=="5lu0-D"].Qscore.iloc[0]
dd
for f in fixed_names:
    for m in moving_names:
        print(f,m)
        dd.at[f,m] = d.loc[d.Cfixed==f].loc[d.Cmoving==m].Qscore.iloc[0]
dd
d
dd = pd.DataFrame(columns=d.Cmoving.sort_values().unique(),index=d.Cfixed.sort_values().unique())
dd
dd['1a69-A']
dd
dd.1a69-A
dd.columns
dd.index
d
dd
ls
dd
d
pwd
import pickle
df_boris = pickle.load('/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/align.pkl')
df_boris = pickle.load(open('/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/align.pkl','rb'))
df_boris = pickle.load(open('/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/align.pkl'))
cp /mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/making_dataframe.py .
ls
mv making_dataframe.py alignments
ls
pwd
cd -
cd -
%run alignments/making_dataframe.py
ls
d
dd
dd['1a69-B']
dd['1a69-B'] = 1
dd
d
dd['1a69-B'] = d[d.Cmoving=='1a69-B'].Qscore
d
dd
d[d.Cmoving=='1a69-B'].Qscore
d[d.Cmoving=='1a69-B']
d[d.Cfixed=='1a69-B']
dd
d
Chain.objects.count()
Alignment.objects.count()
Alignment.objects.values_list('chain_fixed')
a = random.choice(Alignment.objects.all())
a.chain_fixed
Alignment.objects.values_list('chain_fixed',flat=True)
list(Alignment.objects.values_list('chain_fixed',flat=True))
list(Alignment.objects.value_list('chain_fixed',flat=True))
Alignment.objects.values_list?
list(Alignment.objects.value_list('chain_fixed__chain',flat=True))
list(Alignment.objects.values_list('chain_fixed__chain',flat=True))
list(Alignment.objects.values_list('chain_fixed__chain_id',flat=True))
list(Alignment.objects.values_list('chain_fixed',flat=True))
list(Alignment.objects.values_list('chain_fixed_',flat=True))
list(Alignment.objects.values_list('chain_fixed__chain__pdb',flat=True))
a
a.chain_fixed
from pdbase.models import Chain
Chain.objects.exclude(alignments=None)
Chain.objects.exclude(alignments_fixed=None)
Chain.objects.exclude(alignments_fixed=None).count()
Chain.objects.exclude(alignments_moving=None).count()
Chain.objects.exclude(alignments_moving=None).count()
for c in Chain.objects.exclude(alignments_moving=None):
    print c
for c in Chain.objects.exclude(alignments_moving=None):
    print(c)
chains = []
for c in Chain.objects.exclude(alignments_moving=None):
    print(c)
    chains.append(c)
c
chains
chains = []
for c in Chain.objects.exclude(alignments_moving=None):
    print(c)
    chains.append(str(c))
chains
chains = sorted(chains)
chains
/len chains
dd
dd = pd.DataFrame(columns=chains,index=chains)
dd
chains
chains[0]
chains[0].split('-')
Alignment.objects.filter(chain_fixed__id='B', chain_fixed__pdb_code="1a69")
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb_code="1a69")
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69")
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").order_by('chain_fixed__pdb__code')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").order_by('chain_fixed__pdb__code').count()
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values_list('Qscore')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values('Qscore')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values('Qscore','pdb')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values('Qscore','chain_fixed')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values('Qscore','chain_moving')
Alignment.objects.filter(chain_fixed__chain_id='B', chain_fixed__pdb__code="1a69").values('Qscore','chain_moving__pdb')
Alignment.objects.values('Qscore','chain_moving__pdb')
Alignment.objects.values('Qscore','chain_moving__pdb').count()
Alignment.objects.values('Qscore','chain_fixed__pdb','chain_moving__pdb').count()
Alignment.objects.values('Qscore','chain_fixed__pdb','chain_moving__pdb')
Alignment.objects.values('chain_fixed__pdb','chain_fixed__chain_id','chain_moving__pdb','chain_moving__chain_id')
Alignment.objects.values('chain_fixed__pdb','chain_fixed__chain_id','chain_moving__pdb','chain_moving__chain_id','Qscore')
q = Alignment.objects.values('chain_fixed__pdb','chain_fixed__chain_id','chain_moving__pdb','chain_moving__chain_id','Qscore')
dd
dict(q)
q
q
q
dd
chains
dd
dd[chains[0]]
dd[chains[0]].index
[i for i in dd[chains[0]].index]
[i for i in dd[chains[0]].index] == chains
Alignment.objects.values('Qscore')
dd
chains
/len chains
Alignment.objects.count()
Alignment.objects.values('chain_fixed__pdb','chain_fixed__chain_id','chain_moving__pdb','chain_moving__chain_id','Qscore')
Alignment.objects.filter(chain_fixed__pdb_code='1a69')
Alignment.objects.filter(chain_fixed__pdb__code='1a69')
Alignment.objects.filter(chain_fixed__pdb__code='1a69').count()
Alignment.objects.filter(chain_fixed__pdb__code='1a69').count()
ResidueMatch.objects.count()
dd
d
dd
Alignment.chain_fixed
Alignment.chain_fixed.all()
a
a.chain_fixed_id
a.chain_fixed
chain_names
chain_names[0]
dd
d
dd
chain_names
dd = pd.DataFrame(columns=chain_names,index=chain_names)
dd
dd
dd[0]
chain_names
for n in chain_names:
    print(dd[n])
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    q = Alignment.objects.filter(chain_fixed__pdb__code=pdb)
    print(q)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    q = Alignment.objects.filter(chain_fixed__pdb__code=pdb).count()
    print(q)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).count()
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).count()
    print(f,m,f+m)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).count()
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).count()
    print(f,m,f+m)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).count()
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).count()
    print(f,m,f+m)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).count()
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).count()
    print(f,m,f+m)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).count()
    print(f)
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).count()
    print(list(f))
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
d
dd
f
m
f
f.values()
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).values_list('Qscore',flat=True)
    print(list(f))
f
m
m.values()
f & m
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).values_list('Qscore',flat=True)
    print(list(f|m))
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).values_list('Qscore',flat=True)
    f_or_m = f|m
    f_or_m.order_by('chain_fixed__pdb__code').order_by('chain_moving__pdb__code')
    print(list(f_or_m))
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid).values_list('Qscore',flat=True)
    m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid).values_list('Qscore',flat=True)
    f_or_m = f|m
    f_or_m.order_by('chain_fixed__pdb__code').order_by('chain_moving__pdb__code')
    print(list(f_or_m))
ls -lrt
d
dd
f_or_m
f_or_m.values()
import json
json.load?
json.decoder
from django.core import serializers
f_or_m_list = list(f_or_m)
f_or_m_list
/len f_or_m_list
f_or_m.values()
f_or_m_list = list(f_or_m.values())
/len f_or_m_list
f_or_m_list
f_or_m_json = serializers.serialize(f_or_m_list)
f_or_m_json = serializers.serialize(f_or_m)
serializers.serialize?
f_or_m_json = serializers.serialize('json',f_or_m_list)
f_or_m_list
json.load?
f_or_m_json = serializers.serialize('json',f_or_m)
f_or_m
f_or_m.values()
list(f_or_m)
list(f_or_m.values())
594*593
594*593/2
594*593/2 + 594
json.dumps(list(f_or_m.values()))
f_or_m_json = json.dumps(list(f_or_m.values()))
f_or_m_json = json.dumps(list(f_or_m.values()), indent=4)
f_or_m_json
print(f_or_m_json)
dd_json = pd.DataFrame(f_or_m_json)
dd_json = pd.DataFrame()
dd_json
dd_json = pd.read_json(f_or_m_json)
dd_json
dd
d
chain_names
/len chain_names
chain_names[0]
dd
f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid)
f
pdb, chid = tuple(n.split('-'))
pdb
pdb
n
n = '1a69-A'
pdb, chid = tuple(n.split('-'))
f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid)
f
dd[0]
dd['1a69-A']
dd['1a69-A'] = 1
dd['1a69-A']
dd
f = Alignment.objects.filter(chain_fixed__pdb__code=pdb).filter(chain_fixed__chain_id=chid)
f
m = Alignment.objects.filter(chain_moving__pdb__code=pdb).filter(chain_moving__chain_id=chid)
m
f.order_by('chain_moving__pdb__code','chain_moving__chain_id')
f
f = f.order_by('chain_moving__pdb__code','chain_moving__chain_id')
dd
Alignment.objects.count()
595*594/2
Alignment.objects.filter(chain_fixed__pdb__code='1a69'|chain_moving__pdb__code='1a69')
Q
from django.db.models import Q
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')|Q(chain_moving__pdb__code='1a69'))
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')|Q(chain_moving__pdb__code='1a69'))
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')|Q(chain_moving__pdb__code='1a69')).filter(Q(chain_moving__chain_id='A')|Q(chain_fixed__chain_id='A'))
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')|Q(chain_moving__pdb__code='1a69')).filter(Q(chain_moving__chain_id='A')|Q(chain_fixed__chain_id='A')).count()
594*2
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')|Q(chain_moving__pdb__code='1a69')).count()
Alignment.objects.filter(Q(chain_fixed__pdb__code='1a69')).count()
Alignment.objects.filter(chain_fixed__pdb__code='1a69').count()
Alignment.objects.filter(chain_fixed__pdb__code='1a69',chain_fixed__chain_id='A')
Alignment.objects.filter(chain_fixed__pdb__code='1a69',chain_fixed__chain_id='A').count()
query = Q(chain_fixed__pdb__code='1a69')&Q(chain_fixed__chain_id='A')
Alignment.objects.filter(query).count()
query = Q(chain_fixed__pdb__code='1a69')&Q(chain_fixed__chain_id='A')|Q(chain_moving__pdb__code='1a69')&Q(chain_moving__chain_id='A')
Alignment.objects.filter(query).count()
n
pdb, chid = tuple(n.split('-'))
n
n = chain_names[1]
n
n = chain_names[100]
n
pdb, chid = tuple(n.split('-'))
query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)|Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
Alignment.objects.filter(query).count()
fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
Alignment.objects.filter(moving_query).count()
Alignment.objects.filter(fixed_query).count()
pdb, chid = tuple(chain_names[200].split('-'))
Alignment.objects.filter(fixed_query).count()
pdb
pdb, chid = tuple(chain_names[234].split('-'))
Alignment.objects.filter(fixed_query).count()
Alignment.objects.filter(moving_query).count()
pdb, chid = tuple(chain_names[400].split('-'))
pdb
fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
Alignment.objects.filter(moving_query).count()
Alignment.objects.filter(fixed_query).count()
Alignment.objects.filter(fixed_query|moving_query)
Alignment.objects.filter(fixed_query|moving_query).count()
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
    moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
    f_or_m = Alignment.objects.filter(fixed_query|moving_query)
    print(list(f_or_m))
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
    moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
    f_or_m = Alignment.objects.filter(fixed_query|moving_query)
    print f_or_m.count()
for n in chain_names:
    pdb, chid = tuple(n.split('-'))
    print(pdb,chid)
    fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
    moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
    f_or_m = Alignment.objects.filter(fixed_query|moving_query)
    print(f_or_m.count())
f_or_m
f_or_m
f_or_m.order_by('pdb__code')
f_or_m.order_by('chain_moving__pdb__code')
for a in f_or_m.order_by('chain_moving__pdb__code'):
    print a
for a in f_or_m.order_by('chain_moving__pdb__code'):
    print(a)
dd
for a in f_or_m.order_by('chain_moving__pdb__code'):
    print(a.Qscore)
dd
d
d.Cfixed
d[d.Cfixed=='1q1g-F']
n = '1q1g-F'
pdb, chid = tuple(chain_names[400].split('-'))
pdb, chid = tuple(n.split('-'))
fixed_query = Q(chain_fixed__pdb__code=pdb)&Q(chain_fixed__chain_id=chid)
Alignment.objects.filter(fixed_query|moving_query).count()
moving_query = Q(chain_moving__pdb__code=pdb)&Q(chain_moving__chain_id=chid)
Alignment.objects.filter(fixed_query|moving_query).count()
Alignment.objects.filter(fixed_query).count()
d[d.Cfixed=='1q1g-F'].sort_values('Cmoving')
d[d.Cfixed=='1q1g-F'].sort_values('Cmoving')['Qscore']
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')['Qscore']
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')
dd
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')['Qscore']
chain_names
/len chain_names
dd
d
Alignment.objects.count()
d
ResidueMatch.objects.count()
ResidueMatch.objects.count()
Alignment.objects.count()
Alignment.objects.all()
Alignment.objects.count()
Alignment.objects.values('Cmoving')
Alignment.objects.values('chain_moving')
Alignment.objects.values('chain_moving').count()
Alignment.objects.values('chain_moving').unique()
Alignment.objects.values('chain_moving',flat=True)
Alignment.objects.values_list('chain_moving',flat=True)
Alignment.objects.values('chain_moving')
Alignment.objects.values('chain_fixed')
a = random.choice(Alignment.objects.all())
a
a.chain_fixed
str(a.chain_fixed)
a
a.chain_moving
str(a.chain_moving)
a
Alignment.objects.values('chain_fixed')
Alignment.objects.values('chain_fixed__chain_id')
Alignment.objects.values('chain_fixed__chain')
Alignment.objects.values('chain_fixed__chain_id')
Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id',)
list(Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id'))
set(Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id'))
list(Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id'))
/len list(Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id'))
set(list(Alignment.objects.values('chain_fixed__pdb__code','chain_fixed__chain_id')))
595*594/2
(595*594)/2
chain_names
/len chain_names
Chain.objects.count()
Chain.objects.exclude(alignments_moving=None).count()
Chain.objects.exclude(alignments_fixed=None).count()
Chain.objects.filter(alignments_fixed=None).count()
Chain.objects.filter(alignments_moving=None).count()
Chain.objects.filter(alignments_moving=None)
Chain.objects.filter(alignments_moving=None).filter(alignments_fixed=None)
Chain.objects.exclude(alignments_moving=None).filter(alignments_fixed=None)
Chain.objects.filter(alignments_moving=None).exclude(alignments_fixed=None)
Chain.objects.filter(alignments_moving=None).exclude(alignments_fixed=None)
Chain.objects.filter(alignments_moving=None).exclude(alignments_fixed=None).values()
Alignment.objects.get(fixed_chain__id=1)
Alignment.objects.get(chain_fixed__id=1)
Alignment.objects.get(chain_moving__id=1)
Alignment.objects.get(chain_moving__id=2)
Alignment.objects.get(chain_moving__id=1)
Alignment.objects.filter(chain_fixed__pdb__code="1a69")
Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain__moving__pdb__code="6xz2")
Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain_moving__pdb__code="6xz2")
Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain_moving__pdb__code="6xz2").count()
for a in Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain_moving__pdb__code="6xz2"):
    print a
for a in Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain_moving__pdb__code="6xz2"):
    print(a)
Chain.objects.filter(alignments_moving=None).exclude(alignments_fixed=None)
for a in Alignment.objects.filter(chain_fixed__pdb__code="1a69").filter(chain_moving__pdb__code="1a69"):
    print(a)
Chain.objects.all()
Chain.objects.count()
Chain.objects.exclude(alignments=None)
Chain.objects.exclude(alignments_fixed=None)
Chain.objects.exclude(alignments_fixed=None).count()
Chain.objects.filter(alignments_fixed=None).count()
for c in Chain.objects.filter(alignments_fixed=None).count():
    print(c)
for c in Chain.objects.filter(alignments_fixed=None):
    print(c)
for c in Chain.objects.filter(alignments_moving=None):
    print(c)
dd
d
Alignment.objects.filter(chain_fixed__pdb__code="6xz2").filter(chain_moving__pdb__code="6xz2").count()
Alignment.objects.filter(chain_fixed__pdb__code="6xz2").filter(chain_moving__pdb__code="1a69").count()
Alignment.objects.filter(chain_fixed__pdb__code="6xz2").filter(chain_moving__pdb__code="1a69")
Alignment.objects.filter(chain_fixed__pdb__code="6xz2")
Alignment.objects.exclude(chain_fixed=None)
Alignment.objects.exclude(chain_fixed=None).count()
Alignment.objects.filter(chain_fixed=None).count()
Alignment.objects.filter(chain_moing=None).count()
Chain.objects.filter(Q(alignments_fixed=None)|Q(alignment_moving=None)).count()
Chain.objects.filter(alignments_fixed=None,alignments_moving=None).count()
Chain.objects.filter(alignments_fixed=None,alignments_moving=None)
Chain.objects.exclude(alignments_fixed=None,alignments_moving=None)
Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).count()
Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values_list()
Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).count()
Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values()
list(Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values())
[_['pdb_id']+'-'+_['chain_id'] for _ in list(Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values())]
chain_names = [_['pdb_id']+'-'+_['chain_id'] for _ in list(Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values())]
/len chain_names
dd = pd.DataFrame(columns=chain_names,index=chain_names)
dd
dd
d
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')['Qscore']
d[d.Cfixed=='1a69-A'].sort_values('Cmoving')
Chain.objects.filter(alignments_fixed=None)
Chain.objects.filter(alignments_fixed=None).count()
fixed_none = Chain.objects.filter(alignments_fixed=None)
moving_none = Chain.objects.filter(alignments_moving=None)
fixed_none
moving_none
fixed_none
fixed_none.count()
moving_none
moving_none & fixed_none
(moving_none & fixed_none).count()
(moving_none | fixed_none).count()
Alignment.objects.filter(Qscore=1)
Alignment.objects.filter(Qscore=1.0)
Alignment.objects.filter(Qscore=1.0).count()
fixed_none = Chain.objects.filter(alignments_fixed=None)
fixed_none | moving_none
fixed_none = Chain.objects.filter(alignments_fixed=None)
fixed_none
fixed_none.count()
moving_none = Chain.objects.filter(alignments_moving=None)
moving_none
moving_none.count()
fixed_none & moving_none
no_alignment_chains = fixed_none & moving_none
no_alignment_chains.count()
chain_names
/len chain_names
c in chain_names
c
c
no_alignment_chains
alignments_chains = Chain.objects.all() - no_alignment_chains
alignments_chains = [c for c in Chain.objects.all() if not c in no_alignment_chains]
/len alignment_chains
/len alignments_chains
alignments_chains
for c in alignments_chains:
    print(c.alignments_fixed.count())
for c in alignments_chains:
    if c.alignments_fixed.count() + c.alignments_moving.count() == 594:
        print(c)
for c in alignments_chains:
    if c.alignments_fixed.count() + c.alignments_moving.count() == 593:
        print(c)
Alignment.objects.filter(chain_fixed__pdb__code="1a9o")
Alignment.objects.filter(chain_fixed__pdb__code="1a9o").count()
Alignment.objects.filter(chain_fixed__pdb__code="1a9o").count() + Alignment.objects.filter(chain_moving__pdb__code="1a9o").count()
Alignment.objects.filter(chain_fixed__pdb__code="1vhj").count() + Alignment.objects.filter(chain_moving__pdb__code="1vhj").count()
3564/594
Alignment.objects.filter(Q(chain_fixed__pdb__code="1a90")|Q(chain_moving__pdb__code="1a90"))
Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o"))
Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o")).count()
Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o")).filter(Q(chain_fixed__pdb__code="1vhj")|Q(chain_moving__pdb__code="1vhj"))
for a in Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o")).filter(Q(chain_fixed__pdb__code="1vhj")|Q(chain_moving__pdb__code="1vhj")):
    print a
for a in Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o")).filter(Q(chain_fixed__pdb__code="1vhj")|Q(chain_moving__pdb__code="1vhj")):
    print(a)
# Napraviti jos 1 alignment koji fali def create_alignments():
    gesamt_files = find_gesamt_files()
    for f in gesamt_files:
            print(f)
                pdb1, chain1, pdb2, chain2 = pdb_chain_from_gesamt_file(f)
        qscore, rmsd, aligned, seq = get_scores_from_file(f)
        if qscore:
                ch1 = Chain.objects.get(pdb__code=pdb1,chain_id=chain1)
                    ch2 = Chain.objects.get(pdb__code=pdb2,chain_id=chain2)
            alignment, created = Alignment.objects.get_or_create(
                                Qscore  = float(qscore),
                                                    rmsd  = float(rmsd),
                                                                        aligned_num = int(aligned),
                                                                                            seq_identity = float(seq),
                                                                                                                chain_fixed = ch1,
                                                                                                                                    chain_moving = ch2)
            if created:
                    print('Created new alignment: %s' %alignment)
                    else:
                            print('Existing alignment: %s' %alignment)
            print (pdb1, chain1, pdb2, chain2)
# Napraviti alignment za gesamt/1a9o/1a9oA_1vhjD
whos
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
# gesamt/1a9o/1a9oA_1vhjD
gesamt_files
gf = '/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/'
gf = '/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/1a9o/1a9oA_1vhjD'
cat gf
%cat gf
fg
gf
ls /mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/1a9o/1a9oA_1vhjD
ls -l /mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/1a9o/1a9oA_1vhjD
create_alignments?
create_alignments??
f
pdb1, chain1, pdb2, chain2 = pdb_chain_from_gesamt_file(gf)
pdb1
create_alignments??
qscore, rmsd, aligned, seq = get_scores_from_file(f)
qscore, rmsd, aligned, seq = get_scores_from_file(gf)
qscore
rmsd
create_alignments??
q
create_alignments??
ch1 = Chain.objects.get(pdb__code=pdb1,chain_id=chain1)
ch1
ch2 = Chain.objects.get(pdb__code=pdb2,chain_id=chain2)
ch2
alignment, created = Alignment.objects.get_or_create(
                                Qscore  = float(qscore),
                                                                rmsd  = float(rmsd),
                                                                                                aligned_num = int(aligned), 
                                                                                                                                seq_identity = float(seq),
                                                                                                                                                                chain_fixed = ch1,
                                                                                                                                                                                                chain_moving = ch2)
alignment
Alignment.objects.filter(Q(chain_fixed__pdb__code="1a9o")|Q(chain_moving__pdb__code="1a9o")).filter(Q(chain_fixed__pdb__code="1vhj")|Q(chain_moving__pdb__code="1vhj"))
Alignment.objects.count()
595*594/2
a
dd
aa
d
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
l = []
for a in Alignment.objects.all():
    l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
/len l
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
dd
d.sort_values('Cfixed')
d = d.sort_values('Cfixed')
d
dd
d
d = d.sort_values('Cfixed','Cmoving')
d = d.sort_values(['Cfixed','Cmoving'])
d
dd
d
dd
ls
d
dd
dd.resample?
dd
d
d.pivot(index="Cfixed")
d.pivot(index="Cfixed",columns=["Cmoving","Qscore"])
d
d.pivot(index="Cfixed",columns=["Cmoving"])
ddd = d.pivot(index="Cfixed",columns=["Cmoving"])
ddd
ddd.columns
ddd['Qscore']
d
ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
ddd
ddd['Qscore']
d
chain_names
/len chain_names
d.append?
d
for n in chain_names:
    d.append([n,n,1.000,0.000,237,1.000]
   )
d
dd
d
l
for n in chain_names:
    l.append([n,n,1.000,0.000,237,1.000]
   )
l
l[-1]
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
d.sort_values(['Cfixed','Cmoving'])
ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
ddd
ddd['Qscore']
d
d = d.sort_values(['Cfixed','Cmoving'])
d
d = d.sort_values(['Cfixed','Cmoving'])
d = d.sort_values(['Cfixed','Cmoving'])
d
ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
ddd
q_score_matrix_final = d['Qscore']
q_score_matrix_final
ddd
q_score_matrix_final = ddd['Qscore']
q_score_matrix_final
pickle.dump(d,open('q_score_matrix_final.pkl','wb'))
ll
ll -h
ls
q_score_matrix_final
q_score_matrix_final
q_score_matrix_final.T
q_score_matrix_final.D
q_score_matrix_final.T
q = q_score_matrix_final
q + q.T
q
q.T
q[q==0]
q[q==None]
q
q[q==None]
q[q==Nan]
q[q==NaN]
q[q==None]
q
q
q[q.isna()]
q.isna()
~q.isna()
q[~q.isna()]
q[q.isna()]
q.isna()
q[q.isna().any(axis=1)]
q
ResidueMatch.objects.count()
ls
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ddd
d
dd
d
ddd
ddd.T
df.values
ddd.values
import numpy as np
np.flip?
A = np.arange(8).reshape((2,2,2))
A
A = np.arange(8).reshape(())
A = np.arange(8).reshape(2)
A = np.arange(8).reshape(2,4)
A
np.flip(ddd)
ddd
ddd.values
np.flip(ddd.values)
d
dd
dd = ddd
dd
dd_lower = dd.T
dd_lower
dd_lower.values = np.flip(dd.values)
dd_lower
ddd
d
ddd.fillna(0.0)
ddd
ddd = ddd.fillna(0.0)
ddd
ddd.values + ddd.T.values
np.identity
np.identity
np.identity(2)
np.identity(3)
ddd.shape
ddd.values + ddd.T.values - np.identity(595)
A = ddd.values + ddd.T.values - np.identity(595)
from bokeh.plotting import figure, showw
from bokeh.plotting import figure, show
%matplotlib
import matplotlib.pyplot as plt
A
plt.imshow(A)
plt.show()
plt.show()
plt.show()
plt.imshow()
plt.imshow(A)
plt.show()
A
pickle.dump(A,open('q.pkl','wb'))
ls
ls -lrt
ddd
d
import seaborn as sns
sns.pairplot(d)
p = sns.pairplot(d)
fig = p.figure()
p.savefig('plot.png')
ls
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
whos
r
r.chain
r.chain.alignments_fixed.all()
d
dd
ddd
q
whos?
who
who?
who DataFrame
whos DataFrame
whos DataFrameq
q
q_score_matrix_final
whos DataFrame
ddd
ls
whos DataFrame
dataframe
ddd
q + q.T
q
q_score_matrix_final
q
q[q.isna().any(axis=1)]
q
q[0,0]
q[0,0:]
q[0:,0:]
q
dd
ddd
ddd
ddd + ddd.T
ddd.values
ddd.values + ddd.T.values
1 - ddd.values + ddd.T.values
1 - (ddd.values + ddd.T.values)
1 - (ddd.values + ddd.T.values) + np.identity()
1 - (ddd.values + ddd.T.values) + np.identity(595)
ResidueMatch.objects.count()
a
A
df = pd.DataFrame(A,columns=chain_names,index=chain_names)
df
df
from sklearn.cluster import k_means
k_means?
Kmeans = kmeans(df)
from sklearn.cluster import k_means
Kmeans = k_means(df)
Kmeans = k_means(df,n_clusters=3)
Kmeans
k_means?
Kmeans = k_means(df,n_clusters=3,return_n_iter=True)
Kmeans
Kmeans.count()
Kmeans = k_means(df,n_clusters=4,return_n_iter=True)
Kmeans
Kmeans.count()
ls
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
from sklearn.neighbors import NearestNeighbors
nbrs = NearestNeighbors(n_neighbors=2, algorithm="ball_tree").fit(df)
nbrs
distances, indices = nbrs.kneighbors(df)
distances
distances.shape
indices
nbrs = NearestNeighbors(n_neighbors=10, algorithm="ball_tree").fit(df)
distances, indices = nbrs.kneighbors(df)
distances
distances.shape
indices
nbrs.kneighbors_graph(df)
nbrs.kneighbors_graph(df).toarray()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
from sklearn.cluster import k_means
Kmeans = k_means(df,n_clusters=2,return_n_iter=True)
Kmeans
Kmeans = k_means(df,n_clusters=3,return_n_iter=True)
Kmeans
from sklearn.cluster import kmeans
import sklearn
sklearn.__version__
k_means?
df
d
d_d = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
d_d
d_d.fillna(0)
d_d.T
d_d.fillna(0)
d_d = d_d.fillna(0)
d_d.T
d_d = d.pivot(index="Cmoving",columns=["Cfixed"], values=['Qscore'])
d_d
d_d = d.pivot(index="Cmoving",columns=["Cfixed"], values=['Qscore','RMSD'])
d_d
d_d.columns
Alignment.objects.count()
d
dd
k_means
Kmeans
Kmeans?
k_means?
Kmeans
dd
dd.columns
ddd
ddd['Qscore']
ddd['Qscore'].columns
list(ddd['Qscore'].columns)
Kmeans
from sklearn.cluster import SpectralBiclustering
#https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#sphx-glr-auto-examples-bicluster-plot-spectral-biclustering-py
model = SpectralBiclustering(n_clusters=3, method="log", random_state=0)
model.fit?
model.fit(df)
model.column_labels_
np.argsort?
model
model.get_indices?
model.get_indices()
model.get_indices(1)
model.get_indices(2)
model.get_indices(0)
model.column_labels_
model.column_labels_
model = SpectralBiclustering(n_clusters=3, method="log", random_state=0)
model.biclusters_
model.get_indices()
model.get_indices(1)
model.fit(df)
model.biclusters_
model
model.method
fit_data=df[np.argsort(model.row_labels_)]
fit_data=df.values[np.argsort(model.row_labels_)]
fit_data
fit_data = fit_data[:,np.argsort(model.column_labels_)]
fit_data
from matplotlib import pyplot as plt
plt.matshow?
plt.matshow(fit_data,cmap=plt.cm.Blues)
plt.show()
plt.show()
plt.gcf()
plt.show()
plt.savefig('tmp.png')
ls
fit_data
plt.show()
plt.gcf()
plt.show()
model = SpectralBiclustering(n_clusters=4, method="log", random_state=0)
model = SpectralBiclustering(n_clusters=4, method="log", random_state=0)
model.n_clusters
model.biclusters_
model.fit(df)
model.biclusters_
model.columns_
model.get_indices(1)
model.get_indices(0)
model.get_indices(1)
model.get_indices(2)
model.get_indices(3)
fit_data=df.values[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
plt.matshow(fit_data,cmap=plt.cm.Blues)
plt.show()
plt.gcf()
plt.savefig('tmp.png')
plt.savefig('tmp.png',dpi=300)
plt.gcf()
plt.show()
%matplotlib inline
plt.show()
df
df['6f4x']
df['6f4xA']
df['6f4x-A']
df['6f4x-A','6f4x-A']
df[['6f4x-A','6f4x-A']]
df[:,'6f4x-A']
df[['6f4x-A']]
df[['6f4x-A']['6f4x-A']]
df['6f4x-A']['6f4x-A']
df[df=1]
df[df==1]
df==1
df[df<0.5]
df['6f4x-A']['6f4x-B']
df['6f4x-A']['6f4x-B']
df['6f4x-A']['6f4x-B']
df['6f4x-A']['6f4x-C']
df['6f4x-A']['6f4x-D']
df['6f4x-A']['6f4x-E']
df['6f4x-A']['6f4x-F']
df['6f4x-C']['6f4x-E']
df['6f4x-A']['6f52-A']
df['6f4x-C']['6f52-A']
df['6f4x-A','6f4x-B']
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
dd
d
%matplotlib
%matplotlib qt
%matplotlib tk
%matplotlib qt
%matplotlib qt5
%matplotlib
import matplotlib
matplotlib.use('Qt5Agg')
%matplotlib
%matplotlib
import matplotlib
matplotlib.use('Qt5Agg')
plt.gcf()
plt.show()
%matplotlib
d
%history -f make_q_score_matrix.py
A
dd
ddd
%matplotlib
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ls
d
l = []
for a in Alignment.objects.all():
    
    #l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
Alignment.objects.values('chain_fixed')
Alignment.objects.values('chain_fixed','chain_moving')
Alignment.objects.values('chain_fixed','chain_moving','Qscore')
Alignment.objects.values('chain_fixed','chain_moving','Qscore',flat=True)
Alignment.objects.values_list('chain_fixed','chain_moving','Qscore',flat=True)
Alignment.objects.values_list('chain_fixed',flat=True)
Alignment.objects.values_list('chain_fixed__id',flat=True)
Alignment.objects.values_list('chain_fixed__chain',flat=True)
Alignment.objects.values_list('chain_fixed__pdb',flat=True)
Alignment.objects.values('chain_fixed','chain_moving','Qscore')
[d['chain_fixed'] for d in Alignment.objects.values('chain_fixed','chain_moving','Qscore')]
[(d['chain_fixed'],d['chain_moving']) for d in Alignment.objects.values('chain_fixed','chain_moving','Qscore')]
[(d['chain_fixed'],d['chain_moving'],d['Qscore']) for d in Alignment.objects.values('chain_fixed','chain_moving','Qscore')]
q_scores = [(d['chain_fixed'],d['chain_moving'],d['Qscore']) for d in Alignment.objects.values('chain_fixed','chain_moving','Qscore')]
/len q_score_matrix_final.pkl
/len q_scores
d
ch1
a
repr(a)
str(a)
q_scores
def get_chains_and_q_score(t):
    ch1 = Chain.objects.get(id=t[0])
    ch2 = Chain.objects.get(id=t[1])
    return (str(ch1),str(ch2),t[2])
map(get_chains_and_q_score, q_scores)
[_ for _ in map(get_chains_and_q_score, q_scores)]
q_scores
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
ResidueMatch.objects.count()
l
ResidueMatch.objects.count()
ResidueMatch.objects.count()
q_scores
d
dd
d
q_scores
d
d
ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
ddd
l = []
for a in Alignment.objects.all():
    l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
    print (a.id)
l
l
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
d.sort_values(['Cfixed','Cmoving'])
d
d = d.sort_values(['Cfixed','Cmoving'])
d
l
l
chain_names
d
chain_names = d.Cfixed.sort_values().unique()
chain_names
/len chain_names
chain_names = d.Cmoving.sort_values().unique()
/len chain_names
chain_names = [_['pdb_id']+'-'+_['chain_id'] for _ in list(Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values())]
chain_names
/len chain_names
for n in chain_names:
    l.append([n,n,1.000,0.000,237,1.000]
   )
l
l[-1]
d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
d
d = d.sort_values(['Cfixed','Cmoving'])
d
ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
ddd
ddd = ddd['Qscore']
ddd
ddd = ddd.fillna(0)
ddd
ddd = ddd + ddd.T - np.identity(595)
ddd
ddd
ddd
ls
rm q.pkl q_score_matrix_final.pkl
ls
cd alignments/
ls
%history
%history -l
%history ~1/
%history ~1/
%history ~2/
%history ~3/
%history ~0/
%history -n
%history -n q_scores.py
%history -n -f q_scores.py
ls
%history -f q_scores.py
%history -f long_history.py
