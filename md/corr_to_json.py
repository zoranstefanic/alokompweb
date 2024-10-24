import json
import pickle
from md.models import *

def change_phi_psi(p):
    if p == 'φ': return 'phi'
    else: return 'psi'

def parse(source,target,value):
    return {'source':source[0],'sa':change_phi_psi(source[1]),'target':target[0],'ta':change_phi_psi(target[1]), 'value':round(value,3)}

def translate_corr_to_json(id):
    '''Translates the pickled correlations files to json for use in d3.js'''
    d = []
    corr = pickle.load(open('/mnt/supermicro/avocado/%d/correlations_c.pkl' %id,'rb'))
    for k,v in corr.items():
        for i,j in v.items():
            d.append({'source':k,'target':i,'value':j})
    d1 = list(map(lambda a: parse(**a),d))
    json.dump(d1,open('/mnt/supermicro/avocado/%d/correlations.json' %id,'w'),indent=4)
    return json.dumps(d1,indent=4)

def parse_janin(source,target,value):
    return {'source':source[0],'sa':source[1],'target':target[0],'ta':target[1], 'value':round(value,3)}

def translate_corr_to_json_janin(id):
    '''Version for janin angles'''
    d = []
    corr = pickle.load(open('/mnt/supermicro/avocado/%d/janin_corr.pkl' %id,'rb'))
    for k,v in corr.items():
        for i,j in v.items():
            d.append({'source':k,'target':i,'value':j})
    d1 = list(map(lambda a: parse_janin(**a),d))
    json.dump(d1,open('/mnt/supermicro/avocado/%d/janin_corr.json' %id,'w'),indent=4)
    return json.dumps(d1,indent=4)
