# DNA Sequence Analysis Script
# This script calculates the GC content of a DNA sequence.

def calculate_gc_content(sequence):
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

# Example DNA Sequence
dna_sample = "ATGCGATCGTAGCTAGCTAGCTAGCTAGTCGATCG"
result = calculate_gc_content(dna_sample)

print(f"DNA Sequence: {dna_sample}")
print(f"GC Content: {result:.2f}%")
