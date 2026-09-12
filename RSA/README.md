# RSA Algorithm — From First Principles

A small educational implementation of the RSA public-key cryptosystem, written in Python to explore the connection between number theory and practical computing.

## Why I built this

This project was created as preparation for my personal statement and to deepen my understanding of how mathematical ideas become working algorithms. Rather than using a cryptography library, the implementation builds the core RSA operations directly:

- Extended Euclidean Algorithm
- Greatest common divisor (GCD)
- Modular multiplicative inverses
- RSA key generation
- Modular exponentiation
- Character-by-character encryption and decryption

## How RSA works

RSA starts with two prime numbers, `p` and `q`.

### 1. Generate the modulus

`N = p × q`

### 2. Calculate Euler's totient

`φ(N) = (p - 1)(q - 1)`

### 3. Choose the public exponent

Choose `e` such that:

`gcd(e, φ(N)) = 1`

### 4. Calculate the private exponent

The private exponent `d` is the modular inverse of `e` modulo `φ(N)`:

`d × e ≡ 1 (mod φ(N))`

The program calculates this using the **Extended Euclidean Algorithm** rather than relying on a library function.

### 5. Encrypt

Each character is converted to an integer using `ord()` and encrypted using modular exponentiation:

`c = m^e mod N`

Python's built-in `pow(m, e, N)` performs this efficiently.

### 6. Decrypt

The ciphertext is recovered using:

`m = c^d mod N`

The integers are then converted back into characters using `chr()`.

## Example

For a small educational example, values such as:

- `p = 61`
- `q = 53`
- `e = 17`

give:

- `N = 3233`
- `φ(N) = 3120`
- `d = 2753`

The public key is `(17, 3233)` and the private key is `(2753, 3233)`.

The program then allows a message to be encrypted using the public key and decrypted using the private key.

## Implementation

`rsa.py` contains the complete program. It is deliberately kept small so that the mathematical steps are visible rather than hidden behind a cryptography library.

### Main functions

| Function | Purpose |
|---|---|
| `extended_gcd(a, b)` | Calculates the GCD and Bézout coefficients recursively |
| `mod_inverse(e, phi)` | Finds the modular inverse needed for the private exponent |
| `setUp()` | Generates the RSA keys from user-supplied values |
| `encrypt()` | Converts a message into modular ciphertext values |
| `decrypt(d, N)` | Converts ciphertext back into the original message |

## What I learned

The most useful part of this project was seeing the relationship between several mathematical ideas in one algorithm. The Extended Euclidean Algorithm provides the modular inverse required for RSA, while modular exponentiation makes the encryption and decryption operations practical to compute.

This also reinforced the difference between implementing an algorithm for understanding and implementing cryptography for real-world security.

## Limitations

This is an **educational implementation, not secure cryptographic software**.

In particular:

- The user must provide the prime numbers; the program does not generate or validate them.
- The program does not check that `e` is valid before calculating its inverse.
- Messages are encrypted one character at a time rather than using secure padding and block encoding.
- Small manually chosen primes are unsuitable for real RSA.
- There is no secure random number generation, key storage, padding scheme, authentication, or protection against practical cryptographic attacks.
- The modulus must be large enough for the character values being encrypted.

Real applications should use a well-tested cryptographic library and established schemes such as RSA-OAEP rather than this implementation.

## Running

Requires Python 3.

```bash
python rsa.py
```

The program will prompt for `p`, `q`, and `e`, then ask for a message and public key before performing decryption.

---

**Purpose:** mathematical/computing exploration and personal learning.
