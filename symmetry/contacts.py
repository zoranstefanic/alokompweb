from random import choice
from symmetry.models import *
import pickle
from django.db.models import Q
#contacts = pickle.load(open('contacts.hexamers.pkl','rb'))

hexamers = """1q1g 3uaz 3ooh 4d8y 3ooe 5lu0 4d9h 3opv 5mx4 6xz2 3occ 6f5i 2i4t 4mar 6f4x 6f52 6f4w 6g7x 3tl6 3enz 5mx8 4d8x 3u40 5i3c 4tti 6aqu 5znc 1sq6 4dao 5iu6 4m3n 1xe3 3of3 3fow 6aqs 3onv 3mb8 5mx6 3uay 2isc 1vhj 4ts3 4dan 6f5a 4tta 3uav 3phc 4d98 4ttj 3uax 4d8v 4da8 3uaw 5zni 4da0 4da6 3ut6 4m7w 4da7 4ts9 1vhw 4ldn 4dab 2b94 4dae 2bsx 4lkr 4dar 3emv 1pr2 1ou4 1jdz 1jds 1pr0 1jdt 1jdv 1je0 1jp7 1oum 1pk9 1ecp 1pk7 1nw4 1pr6 1je1 1k9s 1otx 1pw7 1jdu 1jpv 1oty 1ovg 1pr5 1pr4 1pr1 1ov6 1pke 1a69""".split(' ')
trimers = """6b71 5ugf 4pnp 3f8w 5tbt 6b7i 3iex 3fnq 2ai3 4nsn 5ko5 5etj 3gb9 3ggs 6bj7 2oc9 6bhb 3phb 6bi9 6bfv 3k8o 3khs 3e0q 5ko6 1yr3 4m1e 6tk9 6b6k 1vmk 6b56 3faz 3iom 2ai1 3pnp 1qe5 3fuc 2qpl 2p4s 1vfn 6b37 1tcv 1v48 1tcu 6b2l 1ulb 5tbv 2a0w 3k8q 3fb1 1rct 4ear 5tbu 1yqq 1v3q 6bif 3lba 2on6 3scz 1ula 1td1 1v2h 1rfg 2ai2 3e9z 1rsz 3e9r 4eb8 2q7o 3iny 5ifk 6b4t 1yqu 6bi1 2a0y 2oc4 4ns1 6bj6 1rr6 6b3l 6awe 3d1v 4uc0 3la8 1rt9 6bb7 1v41 2a0x 4lna 1yry 3odg 5tbs 6axa 3bgs 1v45 6b4q 1c3x 1pbn 1g2o 1lv8 1lvu 1i80 1pf7 1m73 1pwy 1fxu 1a9t 1b8o 1b8n 1a9o 1a9s 1a9q 1a9r 1a9p 4ece 3djf 4gka""".split(' ')
others = """6dzd 1xaf 6t1b 1u05 1rw0 6t0y 1rv9 1z9t 1t8h 1xfj""".split(' ')


def contacts_counts():
    atoms_with_contacts = Atom.objects.exclude(Q(contacts_to=None)&Q(contacts_from=None))
    residues_with_contacts = Residue.objects.filter(atoms__in=atoms_with_contacts).distinct()
    print("Atoms with contacts: %d" % atoms_with_contacts.count())
    print("Residues with contacts: %d" % residues_with_contacts.count())
