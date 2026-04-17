import pandas as pd

# Years
years = [2025, 2024, 2023]

# 40 Colleges
colleges = [
    "RVCE","BMSCE","MSRIT","DSCE","PESU","BIT","BNMIT","NMIT","CMRIT","SJBIT",
    "AIT","RVU","REVA","CMRU","NHCE","JSS","SDM","KLE","PDA","BIET",
    "GAT","EWIT","RNSIT","VVCE","SIT","TCE","AMC","JIT","SJB","SEA",
    "MVJ","KSIT","BGSIT","SMVIT","NIE","MITM","GEC","PESCE","ATME","DBIT"
]

# Branches
branches = ["CSE","ECE"]

data = []

# Generate data
for i, college in enumerate(colleges):
    for j, branch in enumerate(branches):
        base = 1000 + (i * 500) + (j * 2000)

        for k, year in enumerate(years):
            cutoff = base + (k * 300)

            data.append([year, college, branch, cutoff])

# Create DataFrame
df = pd.DataFrame(data, columns=["Year","College","Course","Cutoff"])

# Save CSV
df.to_csv("data.csv", index=False)

print("✅ data.csv generated successfully!")
