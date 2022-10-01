#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit import DataStructs


ref_path = 'reference_kinases.csv'   # No header
target_path = 'target_file/molecules_bases_proposed_ready.txt'   # delimeter tab: use :  cat oldfile.txt | tr '[,]' '[\t]' > newfile.txt

ref_file = pd.read_csv(ref_path, header=None)


os.mkdir('Result_tanimoto')

for line in range(0,len(ref_file)):
    out = open(str('Result_tanimoto/'+str(ref_file[0][line])+'.dat'),'w+')
    ref = str(ref_file[1][line])
    target = open(target_path)
    j = target.readlines()
    for i in j:
        cid = str(i.split('\t')[0])
        smile = i.split('\t')[1]
        print(smile)
        try :
            ms = [Chem.MolFromSmiles(ref), Chem.MolFromSmiles(smile)]
            fps = [Chem.RDKFingerprint(x) for x in ms]
            sim = DataStructs.FingerprintSimilarity(fps[0],fps[1])
            smile = smile.replace('\n','')
            out_name = str(cid + ',' + str(smile)+','+str(sim))
            print(out_name, file=out)
        except:
            print(cid)

    #df = df.transpose()
    #df.to_csv(str('Result_tanimoto/'+str(ref_file[0][line])+'.dat'))





