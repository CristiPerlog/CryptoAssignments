from collections import Counter
import matplotlib.pyplot as plt

# Original ciphertext
ciphertext = """Ftkins Xpk Wvzu; llna eeryc Tdgq nyx Btsl? Wldvfomx Flvs! Wpzr tizoc, Xcs
hycyiuq! Xywct mauiz Nizbv X ez meqz xf ycda; Goma Flp tdgxu-zxzqedwcv
Pvmi jqazzstvf ti.
Buqv ob X, pnfmvs hvgdaegl xpq affas, Qnki umrztthx bu iidxy hd hpnf qizozbs!
Csg vrm aj rza ilrzi emviwdgw ehroqh wcg hxepjm Qwtoetxu kiifl; kvdj wuhpb
mpfbt hyecmdq.
Xysgtjbyi afeer je! avu jwd xymhtps yivaae, Qdcuhlv btc wcth, iaqsg flv ktppgo
jqxpvr gteyt, Fg Yi kvtn eel etdirrn dzrygwyi, Ss iwsh alm aykkpgh phyaq,
pvti-weakil arv. Rgdrn hrl Nlîjvbp eak Nikeufpiln, Rezze, rbs ppy alm axysg
leeymwdw ysgt, Eel wtmme pn Bi. Qlwbdsp hwtq slezxijgan. Jvnlb! flfi hweya
gzgwy hwn vvcete me hwt jvlpl.
Eeexpne fhml: Temwcv lrhvl flvgt lsekw wr Ovgwpzn, oi ets nspgigo e lueusb,
lmgo nwurvr eppzz, ucmozbv prq wvwexioixrt omueict, heexl eomme hd Zvvzlvm,
wkobbiepro imkv utee, jeafmeu sdaa oma rets."""

# Clean the ciphertext: keep only alphabetic characters 'a' to 'z', convert to lowercase
clean_ciphertext = ''.join(filter(lambda x: 'a' <= x <= 'z', ciphertext.lower()))

# Count the frequency of each letter
frequency = {}

for letter in clean_ciphertext:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

# Calculate total letters for percentages
total_letters = sum(frequency.values())

# Calculate percentage for each letter
frequency_percentage = {letter: (count / total_letters) * 100 for letter, count in frequency.items()}

# Sort percentages by value instead of letter
sorted_percentage_by_value = sorted(frequency_percentage.items(), key=lambda x: x[1], reverse=True)

print("Frequency of each letter in the ciphertext:")
for letter, count in sorted_percentage_by_value:
    print(f"{letter}: {count} %")

# Count bigrams in the cleaned ciphertext
bigrams = [clean_ciphertext[i:i+2] for i in range(len(clean_ciphertext) - 1)]
bigram_counts = Counter(bigrams)

# Count trigrams in the cleaned ciphertext
trigrams = [clean_ciphertext[i:i+3] for i in range(len(clean_ciphertext) - 2)]
trigram_counts = Counter(trigrams)

# Get the 10 most frequent bigrams and 8 most frequent trigrams
most_frequent_bigrams = bigram_counts.most_common(10)
most_frequent_trigrams = trigram_counts.most_common(8)

# Find the most frequent bigram in the cleaned ciphertext
most_frequent_bigram = bigram_counts.most_common(10)[1][0] 

# Locate the positions of this bigram in the original ciphertext
positions = []
i = 0
while i < len(clean_ciphertext) - 1:
    # Check if the bigram matches (case insensitive)
    if clean_ciphertext[i:i+2].lower() == most_frequent_bigram:
        positions.append(i)
        # Skip the next character to avoid counting overlapping bigrams
        i += 2
    else:
        i += 1

# Calculate the gaps between consecutive positions of the bigram in the original ciphertext
gaps = [positions[i+1] - positions[i] for i in range(len(positions) - 1)]

print(gaps)

# Extract every 11th letter from the cleaned ciphertext
every_11th_letter = clean_ciphertext[0::11]  # Start at position 0 (1st letter) and take every 11th letter

# Count the frequency of each letter in the extracted letters
frequency_updated = Counter(every_11th_letter)

# Calculate total letters for percentages
total_letters_updated = sum(frequency_updated.values())

# Calculate percentage for each letter
frequency_percentage_updated = {letter: (count / total_letters_updated) * 100 for letter, count in frequency_updated.items()}

# Display results: Sorted by letter
sorted_frequency_updated = sorted(frequency_updated.items())
sorted_percentage_updated = sorted(frequency_percentage_updated.items())

# Sort percentages by value instead of letter
sorted_percentage_by_value_updated = sorted(frequency_percentage_updated.items(), key=lambda x: x[1], reverse=True)

print("Frequency of each letter in every 11th letter of the ciphertext:")
for letter, count in sorted_percentage_by_value_updated:
    print(f"{letter}: {count:.2f}%")

# English letter frequencies (from the second screenshot)
english_frequencies = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.2, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 
    'i': 7.0, 'j': 0.1, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 
    'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.0, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.1, 
    'y': 2.0, 'z': 0.1
}

statistical_distances = {}

# Function to shift the letters
def shift_text(text, k):
    shifted_text = []
    for char in text:
        if 'a' <= char <= 'z':  # Only shift alphabetic characters
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            shifted_text.append(new_char)
        else:
            shifted_text.append(char)  # If non-alphabetic, keep the character as is
    return ''.join(shifted_text)

# Calculate the statistical distance for each shift k (from 0 to 25)
for k in range(26):
    # Shift the 11th letters of the ciphertext
    shifted_text = shift_text(every_11th_letter, k)
    
    # Count the frequency of each letter in the shifted text
    frequency_shifted = Counter(shifted_text)

    # Calculate total letters for percentages in the shifted text
    total_letters_shifted = sum(frequency_shifted.values())

    # Calculate percentage for each letter in the shifted text
    frequency_percentage_shifted = {letter: (count / total_letters_shifted) * 100 for letter, count in frequency_shifted.items()}

    # Initialize the statistical distance for this k
    statistical_distance = 0.0

    # Calculate the statistical distance for each letter (as per the formula)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        # Pr[X = u] is the probability from the English frequencies
        Pr_X = english_frequencies.get(letter, 0)
        # Pr[Y_k = u] is the probability from the shifted text frequencies
        Pr_Y_k = frequency_percentage_shifted.get(letter, 0)

        # Only calculate the statistical distance if both probabilities are non-zero
        if Pr_X > 0 and Pr_Y_k > 0:
            # Calculate the absolute difference for each letter
            statistical_distance += abs(Pr_X - Pr_Y_k)

    # Apply the formula: Divide by 2
    statistical_distance /= 2

    # Store the result for this shift k
    statistical_distances[k] = statistical_distance

# Display the statistical distances for each shift value k
print("Statistical Distance for each shift k (0 to 25):")
for k, distance in statistical_distances.items():
    print(f"Shift {k}: {distance:.4f}")