from Bio import PDB
from Bio.PDB.Polypeptide import standard_aa_names, three_to_one
from Bio import AlignIO
from pdbase.models import Residue, Chain

def get_seq_for_chain(c):
    seq = ''
    for r in c.residues.all():
        if r.name in standard_aa_names:
           seq += three_to_one(r.name)
    return seq

def get_fasta_for_chain(c):
    fasta = '>%s|%s\n' % (c,c.pdb.title)
    for r in c.residues.all():
        if r.name in standard_aa_names:
            fasta += three_to_one(r.name)
    return fasta + '\n'

def is_standard_residue(r):
    return r.name in standard_aa_names

# First the file chains.fasta is created
def create_chains_fasta():
    out = open('chains.fasta','w')
    for c in Chain.objects.all():
        out.write(get_fasta_for_chain(c))
    out.close()

# Then run script run_clustal.sh to create msa in a file chains_alignment.aln

class RI:
    "Standard residue iterator"
    def __init__(self,chain):
        self.chain = chain
        self.residues_list = [ r for r in chain.residues.order_by('num') if is_standard_residue(r)]
    def next(self):
        return self.residues_list.pop(0)

def connect_MSAlignment_to_residues():
    "Make a dictonary mapping of msa positions (columns) to Residues"
    d = {}
    chain_alignment = AlignIO.read('chains_alignment.aln','clustal')
    for row in chain_alignment:
        p, c = tuple(row.description[:6].split('-'))
        chain = Chain.objects.get(pdb__code=p, chain_id=c)
        seq_from_chain = get_seq_for_chain(chain)
        print(seq_from_chain)
        print(row.seq)
        print(len(row.seq))
        count = 1
        ri = RI(chain)
        d[str(chain)] = []
        for i in row.seq:
            if i != '-':
                res = ri.next()
                assert i == three_to_one(res.name), f" {res} {count}"
                d[str(chain)].append((res,count))
            count +=1
    return d
