import pandas as pd
from symmetry.models import *
import pickle
import re

sgre = re.compile(r'([\w \:]+) \(No\. (\d+)\)') # works

pnps_uc_sg = pickle.load(open('symmetry/pnps_uc_sg.pkl','rb'))
def convert_sg(pnp):
    sg = pnps_uc_sg[pnp]
    s = sg['sg']
    m = sgre.match(s)
    return m.groups()

class ContactsFromDf:
    "Inputs Pandas dataframe and creates Contact, SymmOps and UnitCells"

    def __init__(self,f):
        self.read_pickle(f)

    def read_pickle(self, f):
        self.contacts = pickle.load(open(f,'rb'))
        self.rows = self.contacts.iterrows()

    def row_data(self,row):
        self.row = row = row[1]
        self.a1 = row['First_res_atom']
        self.a2 = row['Second_res_atom']
        self.res1 = row['First_res_num']
        self.res2 = row['Second_res_num']
        self.pdbname = row['PDB_name']
        self.ch1 = row['First_res_chain']
        self.ch2 = row['Second_res_chain']
        self.symop = row['symops']
        self.trans = row['Translation']
        self.prob= row['Probability']
        self.d = row['Distance']

    def contact_to_cctbx_format(self,symop):
        if symop == None:
            return
        try:
            symop = symop.split(':')[1]
            return symop.lower().replace(' ','')
        except:
            print(symop)
    
    def add_symops_in_cctbx_format(self):
        self.contacts['symops'] = self.contacts.Symmetry_operation.map(self.contact_to_cctbx_format)

    def create_contacts(self):
        for row in self.rows:
            self.row_data(row)
            self.create_contact()

    def create_contact(self):
        r1 = Residue.objects.get(chain__chain_id=self.ch1, chain__pdb=self.pdbname, num=self.res1)
        r2 = Residue.objects.get(chain__chain_id=self.ch2, chain__pdb=self.pdbname, num=self.res2)
        try:
            a1 = r1.atoms.get(name=self.a1)
            a2 = r2.atoms.get(name=self.a2)
            symop = SymmOp.objects.get(pdb=self.pdbname,rot=self.symop,trans=self.trans)
            contact, created = Contact.objects.get_or_create(d=self.d, prob=self.prob, from_atom=a1, to_atom=a2, symop=symop)
            if created:
                print('Created %s' % contact)
        except:
            print(self.row)
            print(r1.chain.pdb,r1.name,r1.num)
            print(r2.chain.pdb,r2.name,r2.num)
            print("atoms:", self.a1,self.a2)

    def print_rows(self):
        for row in self.rows:
            self.row_data(row)
            print(self.row)

    def create_symmops(self):
        for row in self.rows:
            self.row_data(row)
            self.create_symmop()

    def create_symmop(self):
        symop, created = SymmOp.objects.get_or_create(rot=self.symop, trans=self.trans, pdb=Pdb.objects.get(code=self.pdbname))
        if created:
            print('Created %s' % symop)
        else:
            print('Existing %s' % symop)

def create_unit_cells():
    pnps = list(Pdb.objects.value_list('code',flat=True))
    for pnp in pnps:
        p = pnps_uc_sg[pnp]
        uc, created=  UnitCell.objects.get_or_create(params = p['uc'],sg = p['sg'][0],num = p['sg'][1], pdb = Pdb.objects.get(code=pnp))
        if created:
            print('Created %s' % uc)


def create_symmetries():
    "This is used to populate SymOp objects from contacts dataframe prepared with cctbx"
    C = pd.read_pickle('/home/zoran/alokompweb/supermicro/disk1/ALOKOMP/cctbx/contacts/Contacts_not_same_residue.pkl')
    symmetres = C[['pdbid','symmetry']].value_counts()
    list_of_symmetries = symmetres.index.to_list()
    for pdbid, sym in list_of_symmetries:
        pdb = Pdb.objects.get(code=pdbid)
        uc = pdb.unit_cell
        if sym != '-':
            s, created = SymOp.objects.get_or_create(sym=sym,unit_cell=uc)
            if created:
                print('Created symmetry:', s, uc)
            else:
                print('Already existing:', s, uc)
