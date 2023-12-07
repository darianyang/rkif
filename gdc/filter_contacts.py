"""
By default, the indentify_contacts.py script will calculate an
all-to-all feature set. Since I have a 2 domain protein in the 
case of gD-crystallin and a dimer for HIV-1 CA-CTD, I would like 
to only focus on the inter-domain/-monomer changes instead of the
current default which includes the intra-domain/-monomer features.
"""

import numpy as np
import pandas as pd
import re

# Load the CSV file into a pandas DataFrame
csv_file_path = "contacts_all_res.csv"
df = pd.read_csv(csv_file_path)
      
# Define a function to check if a column name corresponds to inter-domain features
def is_inter_domain_feature(column_name):
    # Extract residue numbers from the column name
    # Extract the first two parts and remove the last three characters
    residues = [int(part[:-3]) for part in column_name.split()[:2] if part[:-3].isdigit()]

    # Check if the residues belong to different domains
    if len(residues) == 2:
        domain1, domain2 = residues
        return (domain1 <= 83 and domain2 > 83) or (domain1 > 83 and domain2 <= 83)
    else:
        return False
    # it might be fine to only use: 
    # return residues[0] <= 83 and residues[1] > 83
    # since all the larger domain values of residues[0] should be
    # already captured by the first set


# Filter columns based on the specified criteria
filtered_columns = [col for col in df.columns if is_inter_domain_feature(col)]

# Create a new DataFrame with only the filtered columns
filtered_df = df[filtered_columns]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv("inter_contacts.csv", index=False)

#print(filtered_df.shape)