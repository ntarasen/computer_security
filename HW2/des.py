from typing import Tuple

# Initial permutation (IP) table
INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final permutation (IP-1) table
FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Permutation Choice 1 (PC-1) table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permutation Choice 2 (PC-2) table
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Number of left shifts for each round
SHIFT_SCHEDULE = [
    1, 1, 2, 2,
    2, 2, 2, 2,
    1, 2, 2, 2,
    2, 2, 2, 1
]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

PERMUTATION_TABLE = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]

S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

def xor(a, b):
    """Perform XOR operation between two strings a and b."""
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def bin2dec(binary):
    """Convert a binary string to a decimal number."""
    return int(binary, 2)

def dec2bin(number):
    """Convert a decimal number to a binary string."""
    return bin(number)[2:]

def bin2text(binary_str):
    """Convert binary string to ASCII text."""
    text = ''
    for i in range(0, len(binary_str), 8):  # Process 8 bits (1 byte) at a time
        byte = binary_str[i:i+8]
        text += chr(int(byte, 2))  # Convert binary to decimal then to char
    return text

#def permute(key, table):
#    """Permute the key using the specified table."""
#    return ''.join(key[i - 1] for i in table)

def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation += k[arr[i] - 1]  # Subtract 1 because array indices in the permutation table usually start from 1
    return permutation

def left_shift(key, shifts):
    """Left shift the key by the specified number of shifts."""
    return key[shifts:] + key[:shifts]

def generate_round_keys(initial_key):
    """Generate the 16 round keys."""
    # Convert the initial key from hex to binary and permute using PC-1
    key_binary = bin(int(initial_key, 16))[2:].zfill(64)
    key_pc1 = permute(key_binary, PC1, 56)
    
    # Split the key into left and right halves
    C0 = key_pc1[:28]
    D0 = key_pc1[28:]
    
    round_keys = []
    
    # Generate each of the 16 round keys
    for i in range(16):
        # Perform left shifts
        C0 = left_shift(C0, SHIFT_SCHEDULE[i])
        D0 = left_shift(D0, SHIFT_SCHEDULE[i])
        
        # Combine the halves and permute using PC-2 to get the round key
        combined_key = C0 + D0
        round_key = permute(combined_key, PC2, 48)
        round_keys.append(round_key)
    
    return round_keys
    
def expansion_function(block):
    """Expand the block from 32 to 48 bits using the expansion table."""
    return permute(block, EXPANSION_TABLE)

def substitution_function(expanded_block):
    """Substitute using the S-boxes."""
    substituted_block = ""
    for i in range(8):  # Process 6 bits at a time for each S-box
        block_section = expanded_block[i*6:(i+1)*6]
        row = int(block_section[0] + block_section[5], 2)
        column = int(block_section[1:5], 2)
        substituted_block += bin(S_BOXES[i][row][column])[2:].zfill(4)
    return substituted_block
    
def permutation_function(substituted_block):
    """Permute the substituted block using the permutation table."""
    return permute(substituted_block, PERMUTATION_TABLE)
    
def decrypt(ciphertext, round_keys):
    # Reverse the order of round keys for decryption
    round_keys.reverse()

    # Initial Permutation
    ciphertext_bits = permute(ciphertext, INITIAL_PERMUTATION, 64)
    left, right = ciphertext_bits[:32], ciphertext_bits[32:]

    for i in range(16):
        # Expansion D-box: Expanding the 32 bits data into 48 bits
        right_expanded = permute(right, EXPANSION_TABLE, 48)
        
        # XOR RoundKey[i] and right_expanded
        xor_x = xor(round_keys[i], right_expanded)
        
        # S-Box
        sbox_str = ""
        for j in range(0, 48, 6):
            row = bin2dec(int(xor_x[j]) << 1 | int(xor_x[j + 5]))
            col = bin2dec(int(xor_x[j + 1]) << 3 | int(xor_x[j + 2]) << 2 | int(xor_x[j + 3]) << 1 | int(xor_x[j + 4]))
            val = S_BOX[j // 6][row][col]
            sbox_str += dec2bin(val)
        
        # Straight D-box
        sbox_str = permute(sbox_str, PERMUTATION_TABLE, 32)
        
        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result
        
        # Swapping left and right
        if i != 15: # No swapping in the last round
            left, right = right, left
    
    # Combine the halves and apply the final permutation
    combine = left + right
    plaintext = permute(combine, FINAL_PERMUTATION, 64)
    
    # Convert the binary plaintext to characters (ASCII)
    plaintext = bin2text(plaintext)
    
    return plaintext

# Example usage
initial_key_hex = "133457799BBCDFF1"  # Replace this with the actual key
round_keys = generate_round_keys(initial_key_hex)

# Output the round keys
for i, key in enumerate(round_keys, start=1):
    print(f"Round {i} key: {key}")
    

ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"
key = "0100110001001111010101100100010101000011010100110100111001000100"


    # Decrypt the ciphertext
#plaintext = decrypt(ciphertext, round_keys)

#print("Decrypted Text:", plaintext)
