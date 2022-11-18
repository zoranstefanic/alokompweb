import pandas as pd
import json

torsions = open('torsions.dat','r').readlines()
torsions = [_.strip() for _ in torsions]

def dat_to_json(dat):
    df = pd.read_csv(dat, delim_whitespace=True)
    df = df.iloc[:,1]
    df = df.round(1)
    d = {}
    d['torsions'] = list(df)
    return d
    
for t in torsions:
    d = os.path.dirname(t)
    print(t)
    try:
        mdt = MDtrajectory.objects.filter(directory__name=d).get(num_frames__gt=10000)
        print(mdt)
    except:
        pass

def create_torsion_from_dat(dat):
    print(dat)
    name = os.path.basename(dat)
    file = dat
    values = dat_to_json(dat)
    traj = get_traj_for_dat(dat)
    return name, file, values, traj

