def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist (numbers are not coprime)")
    return x % phi


def setUp():
    print("--- KEY GENERATION ---")
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter public exponent e: "))

    N = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    print(f"Public Key  -> e: {e}, N: {N}")
    print(f"Private Key -> d: {d} (Keep this secret!)\n")
    return d, N


def encrypt():
    print("--- ENCRYPTION ---")
    message = input("Enter message to encrypt: ")
    e = int(input("Enter public key e: "))
    N = int(input("Enter public key N: "))

    # Encrypt each character into a list of modular integers
    cipher_list = [pow(ord(char), e, N) for char in message]

    # Convert to a single space-separated string
    ciphertext = " ".join(map(str, cipher_list))
    print(f"Ciphertext (C): {ciphertext}\nSend this to Alice!\n")
    return ciphertext


def decrypt(d, N):
    print("--- DECRYPTION ---")
    cipher_input = input("Enter received ciphertext (space-separated numbers): ")

    # Parse space-separated numbers back into an integer list
    cipher_list = [int(c) for c in cipher_input.split()]

    # Decrypt each integer and reassemble into the original string
    decrypted_chars = [chr(pow(c, d, N)) for c in cipher_list]
    decrypted_message = "".join(decrypted_chars)

    print(f"Decrypted Message: {decrypted_message}\n")


# Execution Flow
d, N = setUp()
encrypt()
decrypt(d, N)
