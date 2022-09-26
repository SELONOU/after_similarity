import pandas as pd
import os
import numpy as np
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit import DataStructs
import os
from rdkit.Chem import AllChem
directory = '/cta/users/myildiz/workspace/selonou/mol_propos_test/tanimoto_similarities/tanimoto_job/job_tanimoto/results_tanimoto/maybe'
for ligand in os.listdir(directory):
    if ligand.endswith(""):
        df = pd.read_csv(ligand,sep=',',header=None,names=['cid','SMILES','similarity'])
        df.drop(df[df.similarity < 0.7].index, inplace=True)
        df.to_csv(ligand+'.csv',sep=',', header=True, index=False, mode='w', decimal='.')
        df = pd.read_csv(ligand+'.csv')
        mols = [Chem.MolFromSmiles(smi) for smi in df.SMILES]
        hmols = [Chem.AddHs(m) for m in mols]
        for mol  in hmols:
            print(mol)
            AllChem.EmbedMolecule(mol,AllChem.ETKDG())
            print(AllChem.UFFOptimizeMolecule(mol,1000))
        smiles = list(df.SMILES)
        sid = list(df.cid)
        libs = df[df.columns[0]]
        writer = Chem.SDWriter(ligand+'.sdf')
        for n in range(len(libs)):
            hmols[n].SetProp("_Library","%s"%libs[n])
            hmols[n].SetProp("_Name","%s"%sid[n])
            hmols[n].SetProp("_PubChemID","%s"%sid[n])
            hmols[n].SetProp("_SMILES","%s"%smiles[n])
            writer.write(hmols[n])
        writer.close()
        continue
    else:
        continue

