import django
import os, sys
import re
import glob
from pdbase.models import Chain, Residue
from .models import *

THIS = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(THIS)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alokomp.settings")
django.setup()

SUPERPOSITION = re.compile(r'\|(H|S| )?(\-|\+|\.)? ([A-Z]):([A-Z]+)\s+(\d+) \| <(\*\*|\+\+|==|\-\-|::|\.\.)(\d.\d\d)(\6)> \|(H|S| )?(\-|\+|\.)? ([A-Z]):([A-Z]+)\s+(\d+)')

def find_gesamt_files():
    GESAMT_DIR = "/mnt/supermicro/disk1/ALOKOMP/alignments/GESAMT/gesamt/"
    gesamt_files = []
    for d, dirs, files in os.walk(GESAMT_DIR):
        print(d)
        fs = [os.path.join(GESAMT_DIR,d,f) for f in files if not f.endswith('.aln')]
        gesamt_files += fs
    return gesamt_files

def process_gesamt_file(f):
    superposition_re = SUPERPOSITION
    lines = open(f).readlines()
    for line in lines:
        m = superposition_re.match(line)
        if m:
            print(m.groups())
            print(line)

def get_scores_from_file(f):
    qscore_re = re.compile(r" Q-score\s+\: (\d\.\d+)")
    rmsd_re = re.compile(r" RMSD\s+\: (\d\.\d+)")
    aligned_re = re.compile(r" Aligned residues \: (\d+)")
    seq_re = re.compile(r" Sequence Id\:\s+\: (\d\.\d+)")
    lines = open(f).readlines()
    qscore, rmsd, aligned, seq = None, None, None, None
    for line in lines:
        if qscore_re.match(line):
            qscore = qscore_re.match(line).groups()[0]
        elif rmsd_re.match(line):
            rmsd = rmsd_re.match(line).groups()[0]
        elif aligned_re.match(line):
            aligned = aligned_re.match(line).groups()[0]
        elif seq_re.match(line):
            seq = seq_re.match(line).groups()[0]
    return qscore, rmsd, aligned, seq

def pdb_chain_from_gesamt_file(f):
    name = os.path.split(f)[1]
    print(name)
    return name[:4],name[4],name[6:10],name[-1]
 
def create_alignments():
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
            print (qscore, rmsd, aligned, seq)
        else:
            print('No alignment in %s' %f)
            continue 

def create_residue_matches_for_alignment(f):
    superposition_re = SUPERPOSITION
    lines = open(f).readlines()
    pdb1, chain1, pdb2, chain2 = pdb_chain_from_gesamt_file(f)
    ch1 = Chain.objects.get(pdb__code=pdb1,chain_id=chain1)
    ch2 = Chain.objects.get(pdb__code=pdb2,chain_id=chain2)
    try:
        alignment = Alignment.objects.get(chain_fixed=ch1,chain_moving=ch2)
    except:
        return
    position = 1
    for line in lines:
        m = superposition_re.match(line)
        if m:
            g = m.groups()
            text = line.strip()
            fixed = Residue.objects.get(chain=ch1,num=g[4]) 
            moving = Residue.objects.get(chain=ch2,num=g[12]) 
            distance = g[6]
            similarity_ = {'**':5,'++':4,'==':3,"--":2,"::":1,"..":0}
            similarity = similarity_[g[5]]
            ss_fixed = g[0]
            ss_moving = g[8]
            h_fixed = g[1]
            h_moving = g[9]
            #print(position,text,fixed,moving,distance,similarity,ss_fixed,ss_moving,h_fixed,h_moving)
            residue_match, created = ResidueMatch.objects.get_or_create(
                                position = position,
                                text = text,
                                alignment = alignment,
                                fixed = fixed,
                                moving = moving,
                                distance = float(distance),
                                similarity = similarity,
                                ss_fixed = ss_fixed,
                                ss_moving = ss_moving,
                                h_fixed = h_fixed,
                                h_moving = h_moving)
            if created:
                print('Created %s' %residue_match)
            else:
                print('Existing ---: %s' %residue_match)
            position += 1
