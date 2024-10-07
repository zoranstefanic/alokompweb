import random
import glob
import os, time
import MDAnalysis as mda
from .models import MDdirectory, MDtrajectory
from datetime import datetime

def trajectories_in_dir(d):
    return glob.glob(os.path.join(d,'*.nc')) + glob.glob(os.path.join(d,'*.xtc'))

def find_trajectories(topdir):
    # Returns a dictionary with keys directories and values
    # all the trajectories in it (nc for Amber and xtc for Gromacs)
    trajectories = {}
    for d, dirs, files in os.walk(topdir):
        traj_files = trajectories_in_dir(d)
        if traj_files:
            trajectories[d] = traj_files
            print(d)
    return trajectories

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
             return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0

def trajectory_info(t):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(t)
    print(sizeof_fmt(size))
    print('Atime:',time.ctime(atime))
    print('Mtime:',time.ctime(mtime))
    print('Ctime:',time.ctime(ctime))
    u = mda.Universe(t)
    t = u.trajectory
    print(t.totaltime)

def MDtrajectory_from_file(t):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(t)
    u = mda.Universe(t)
    traj, created = MDtrajectory.objects.get_or_create(file=t, 
        type = 'amber',
        filesize = size,
        atime = datetime.fromtimestamp(atime),
        ctime = datetime.fromtimestamp(ctime),
        mtime = datetime.fromtimestamp(mtime),
        totaltime = u.trajectory.totaltime,
        num_atoms = u.trajectory.n_atoms,
        num_frames = u.trajectory.n_frames,
        directory = MDdirectory.objects.get(name=os.path.dirname(t))
        )
    if created:
        print('Created trajectory %s' % traj)
    else:
        print('Updated trajectory %s' % traj)
        
def MDdirectory_from_directory(d):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(d)
    try:
        mdd = MDdirectory.objects.get(name=d)
        mdd.atime = datetime.fromtimestamp(atime)
        mdd.ctime = datetime.fromtimestamp(ctime)
        mdd.mtime = datetime.fromtimestamp(mtime)
        mdd.save()
        print('Updating directory %s' % mdd)
    except: 
        mdd = MDdirectory.objects.create(name=d,
            atime = datetime.fromtimestamp(atime),
            ctime = datetime.fromtimestamp(ctime),
            mtime = datetime.fromtimestamp(mtime),
        ) 
        print('Created directory %s' % mdd)
