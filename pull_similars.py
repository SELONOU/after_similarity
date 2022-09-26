import pandas as pd
import os
import numpy as np
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit import DataStructs

df = pd.read_csv("test2.dat",sep=',',header=None,names=['cid','SMILES','similarity'])
df.drop(df[df.similarity < 0.1].index, inplace=True)
df.to_csv('similars.csv',sep=',', header=True, index=False, mode='w', decimal='.')


from rdkit.Chem import AllChem
df = pd.read_csv('similars.csv')
mols = [Chem.MolFromSmiles(smi) for smi in df.SMILES]
hmols = [Chem.AddHs(m) for m in mols]
for mol  in hmols:
    print(mol)
    AllChem.EmbedMolecule(mol,AllChem.ETKDG())
    print(AllChem.UFFOptimizeMolecule(mol,1000))
smiles = list(df.SMILES)
sid = list(df.cid)
libs = df[df.columns[0]]
writer = Chem.SDWriter('TEST.sdf')

for n in range(len(libs)):
    hmols[n].SetProp("_Library","%s"%libs[n])
    hmols[n].SetProp("_Name","%s"%sid[n])
    hmols[n].SetProp("_PubChemID","%s"%sid[n])
    hmols[n].SetProp("_SMILES","%s"%smiles[n])
    writer.write(hmols[n])
writer.close()
