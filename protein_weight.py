# كود لحساب الوزن الجزيئي التقريبي لسلسلة بروتينية
def calculate_protein_weight(protein_seq):
    # الأوزان الجزيئية التقريبية للأحماض الأمينية (Daltons)
    aa_weights = {'A': 71.07, 'C': 103.13, 'D': 115.08, 'E': 129.11, 'F': 147.17} # مثال مبسط
    weight = sum(aa_weights.get(aa, 110.0) for aa in protein_seq) # 110 هو المتوسط
    return weight

my_protein = "ACDEF"
print(f"Protein: {my_protein}")
print(f"Estimated Molecular Weight: {calculate_protein_weight(my_protein)} Daltons")
