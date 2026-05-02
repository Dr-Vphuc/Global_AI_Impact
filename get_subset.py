import pandas as pd

# Load the dataset
df = pd.read_csv('processed_data/encoded_ai_company_adoption.csv')

# Sample 10,000 random records
subset_10k = df.sample(n=10000, random_state=42)
subset_10k.to_csv('./processed_data/subset_10k.csv', index=False)

# Sample 20,000 random records
subset_20k = df.sample(n=20000, random_state=43)
subset_20k.to_csv('./processed_data/subset_20k.csv', index=False)

# Sample 50,000 random records
subset_50k = df.sample(n=50000, random_state=44)
subset_50k.to_csv('./processed_data/subset_50k.csv', index=False)