# Conda activate my-rdkit-env
# import rkdit library
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdDistGeom

# Define function Convert SMILES to a 3D SDF
def smiles_to_sdf(smiles, reactant_id, output_folder="output_sdfs"):
    # Create the output folder if it doesn't exist
    import os
    os.makedirs(output_folder, exist_ok=True)

    # Convert SMILES to RDKit molecule
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print(f"Failed to parse SMILES for Reactant ID: {reactant_id}")
        return
    
    # Add hydrogens and generate 3D coordinates
    mol = Chem.AddHs(mol)
    success = AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    if success != 0:
        print(f"3D embedding failed for Reactant ID: {reactant_id}")
        return
    
    # Optimize geometry
    AllChem.UFFOptimizeMolecule(mol)

    # Write to SDF file
    sdf_path = os.path.join(output_folder, f"{reactant_id}.sdf")
    writer = Chem.SDWriter(sdf_path)
    writer.write(mol)
    writer.close()
    print(f"SDF file written: {sdf_path}")

# Main script
def main(input_csv, output_folder="output_sdfs"):
    # Read the CSV file
    data = pd.read_csv(input_csv)

    # Check if required columns are present
    required_columns = {"BindingDB Reactant_set_id", "Ligand SMILES"}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Input CSV must contain columns: {required_columns}")

    # Process each row
    for _, row in data.iterrows():
        reactant_id = row["BindingDB Reactant_set_id"]
        smiles = row["Ligand SMILES"]
        smiles_to_sdf(smiles, reactant_id, output_folder)

if __name__ == "__main__":
    # Input CSV file
    input_csv = "input_data_cleaned.csv"  # Replace with your actual CSV file path
    output_folder = "output_sdfs"  # Output folder for SDF files

    # Run the main function
    main(input_csv, output_folder)

