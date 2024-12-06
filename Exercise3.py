from collections import defaultdict
import math

Pr_M = {"a": 1/3, "b": 4/15, "c": 1/5, "d": 1/5}
Pr_K = {"k1": 1/5, "k2": 3/10, "k3": 1/5, "k4": 3/10}

encryption_table = {
    "k1": {"a": 3, "b": 1, "c": 4, "d": 2},
    "k2": {"a": 2, "b": 4, "c": 1, "d": 3},
    "k3": {"a": 4, "b": 2, "c": 3, "d": 1},
    "k4": {"a": 1, "b": 3, "c": 2, "d": 4},
}

# P(C = c)
Pr_C = defaultdict(float)

# Iterate through each ciphertext
for ciphertext in range(1, 5):
    for plaintext, plaintext_prob in Pr_M.items():
        for key, mapping in encryption_table.items():
            if mapping[plaintext] == ciphertext:  # Check if the ciphertext matches
                Pr_C[ciphertext] += plaintext_prob * Pr_K[key]

# P(C = c | P = m)
Pr_C_given_M = defaultdict(lambda: defaultdict(float))

for key, mapping in encryption_table.items():
    for plaintext, ciphertext in mapping.items():
        Pr_C_given_M[ciphertext][plaintext] += Pr_K[key]

# P(P = m | C = c)
Pr_M_given_C = defaultdict(dict)

for ciphertext in range(1, 5):
    for plaintext in Pr_M:
        Pr_M_given_C[ciphertext][plaintext] = (
            Pr_M[plaintext] * Pr_C_given_M[ciphertext][plaintext] / Pr_C[ciphertext]
        )

# Display results for Exercise 3.a
print("Conditional Probabilities Pr(M | C):")
for ciphertext in sorted(Pr_M_given_C.keys()):
    print(f"Ciphertext {ciphertext}:")
    for plaintext, prob in Pr_M_given_C[ciphertext].items():
        print(f"  P({plaintext} | {ciphertext}) = {prob:.4f}")

# Entropy H(M|C)
H_MC = 0

# Iterate over all ciphertexts and plaintexts to compute the entropy
for ciphertext in sorted(Pr_M_given_C.keys()):
    for plaintext, prob in Pr_M_given_C[ciphertext].items():
        H_MC -= Pr_C[ciphertext] * prob * math.log2(prob)
        
# Display the result for Exercise 3.b
print(f"Conditional Entropy H(M|C) = {H_MC:.4f}")
