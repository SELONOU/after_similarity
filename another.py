from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV
f = open( 'out.csv', 'w' )
suppl = Chem.SDMolSupplier( 'ligands.sdf' )
# convert sdf to smiles
SDFToCSV.Convert( suppl, f )
f.close()
