#!/usr/bin/env python
import requests
import os, sys
import django
from Bio.PDB import *

THIS = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(THIS)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alokomp.settings")

django.setup()

from pdbase.models import *

mp = MMCIFParser()
PNP_DIR = '/home/zoran/PNPs/'
pnps = open('/home/zoran/PNPs/PDBe_search.csv').readlines()
pnps = [p.strip() for p in pnps]

def structure_from_cif(cif):
    try:
        pdb = Pdb.objects.get(code=cif)
        print('Already in %s' %pdb)
        return 
    except:
        s = mp.get_structure(cif, '/home/zoran/PNPs/%s.cif' %cif)
        pdb, created = Pdb.objects.get_or_create(code=cif, title=s.header['name'])
        print('Created structure %s' %pdb)

def chains_from_cif(cif):
    pdb = Pdb.objects.get(code=cif)
    s = mp.get_structure(cif, '/home/zoran/PNPs/%s.cif' %cif)
    for c in s.get_chains():
        chain, created = Chain.objects.get_or_create(chain_id=c.id, pdb=pdb)
        if created:
            print('Created chain %s' %chain)

def residues_from_cif(cif):
    pdb = Pdb.objects.get(code=cif)
    s = mp.get_structure(cif, '/home/zoran/PNPs/%s.cif' %cif)
    for c in s.get_chains():
        chain = Chain.objects.get(chain_id=c.id, pdb=pdb)
        for r in c.get_residues():
            residue, created = Residue.objects.get_or_create(name=r.resname, num=r.id[1], chain=chain) 
            if created:
                print('Created residue %s ' %residue)

def atoms_from_cif(cif):
    pdb = Pdb.objects.get(code=cif)
    s = mp.get_structure(cif, '/home/zoran/PNPs/%s.cif' %cif)
    print(pdb)
    for c in s.get_chains():
        chain = Chain.objects.get(chain_id=c.id, pdb=pdb)
        for r in c.get_residues():
            residue = Residue.objects.get(name=r.resname, num=r.id[1], chain=chain) 
            for a in r.get_atoms():
                atom, created = Atom.objects.get_or_create(name=a.name,
                                                           num =a.serial_number,
                                                           x = a.coord[0],
                                                           y = a.coord[1],
                                                           z = a.coord[2],
                                                           bfactor = a.bfactor,
                                                           residue = residue)
                if created:
                    print('Created atom %s' %atom)

def fill_structures():
    for p in pnps:
        #structure_from_cif(p)
        #chains_from_cif(p)
        #residues_from_cif(p)
        #atoms_from_cif(p)
        pass

def get_json_data(code):
    pdb = Pdb.objects.get(code=code)
    data = requests.get(f'https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{code}').json()[code.lower()]
    pdb.data = data[0]
    pdb.save()
    print('Added json data to: %s' %pdb)
    
def fill_json():
    for pdb in pnps:
        get_json_data(pdb)


if __name__ == '__main__':
    #    fill_structures()
    fill_json()
