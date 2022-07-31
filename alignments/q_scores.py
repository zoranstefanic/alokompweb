from alignments.models import Alignment
from pdbase.models import *
from sklearn.cluster import SpectralBiclustering
import pandas as pd
import numpy as np
import pickle
from matplotlib import pyplot as plt

def plot_clustered_qscores(df,n_clusters=3):
    model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
    model.fit(df)
    fit_data= df.values[np.argsort(model.row_labels_)]
    fit_data = fit_data[:, np.argsort(model.column_labels_)]
    plt.matshow(fit_data,cmap=plt.cm.plasma)
    plt.show()
    plt.savefig('qscores.png',dpi=400)

def alignments_to_dataframe():
    # Not very fast as it iterates through the list
    l = []
    for a in Alignment.objects.all():
        l.append([str(a.chain_fixed),str(a.chain_moving),a.Qscore,a.rmsd,a.aligned_num,a.seq_identity])
        print (a.id)
    chain_names = [_['pdb_id']+'-'+_['chain_id'] for _ in list(Chain.objects.exclude(alignments_fixed=None,alignments_moving=None).values())]
    # append alignments between same chains
    for n in chain_names:
        l.append([n,n,1.000,0.000,237,1.000])
    d = pd.DataFrame(l, columns=['Cfixed','Cmoving','Qscore','RMSD','Num_aligned','Seqid'])
    d = d.sort_values(['Cfixed','Cmoving'])
    ddd = d.pivot(index="Cfixed",columns=["Cmoving"], values=['Qscore'])
    ddd = ddd['Qscore']
    ddd = ddd + ddd.T - np.identity(595)
    return ddd
