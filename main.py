nums = {
    0: '\u00AD',  # SOFT HYPHEN (SHY)
    1: '\u2063',  # INVISIBLE SEPARATOR
    2: '\u2061',  # FUNCTION APPLICATION
    3: '\u2062',  # INVISIBLE TIMES
    4: '\u2064',  # INVISIBLE PLUS
    5: '\ufeff',  # ZERO WIDTH NO-BREAK SPACE (BOM)
    6: '\u2060',  # WORD JOINER
    7: '\u200d',  # ZERO WIDTH JOINER (ZWJ)
    8: '\u200c',  # ZERO WIDTH NON-JOINER (ZWNJ)
    9: '\u200e',  # LEFT-TO-RIGHT MARK (LTRM)
    10: '\u200f'  # RIGHT-TO-LEFT MARK (RTLM)
}

# \u200b removed
macros = {
    'a': '\u200f\ufeff', 'e': '\u2062\u2060', 'i': '\u200d\u2060', 'o': '\u2061\u200d', 'u': '\u200c\u200d',
    '\n': '\u200d\u200c', '\t': '\u200c\u200c', '₂': '\u200e\u200c',
         }

def encrypt(private, public=''):
    message = ''
    private_size, public_size = len(private), len(public)

    for i in range(max(private_size, public_size)):
        secret = '' if i >= private_size else private[i]
        normal = '' if i >= public_size else public[i]

        message += normal + toUnDecimal(secret)

    return message


def decrypt(private):
    nums_values = {v: k for k, v in nums.items()}
    message = ''
    i, n = 0, len(private)

    while i < n:
        if private[i] in nums_values.keys():
            message += fromUnDecimal(private[i:i + 2])
            i += 2
        else:
            i += 1

    return message


def toUnDecimal(char):
    # our ascii codes starts from 32 which is SPACE droped to 0
    ascii_value = ord(char) - 32
    unDecimal_code = ''

    if char in macros:
        return macros[char]

    while ascii_value > 0:
        num = ascii_value % 11
        unDecimal_code += str(nums[num])
        ascii_value = ascii_value // 11

    return unDecimal_code + (nums[0] * (2 - len(unDecimal_code)))


def fromUnDecimal(code):
    nums_values = {v: k for k, v in nums.items()}
    macros_values = {v:k for k, v in macros.items()}

    if code in macros_values:
        return macros_values[code]

    val = 0
    for i, code in enumerate(code):
        val += nums_values[code] * (11 ** i)

    char = chr(val + 32)
    return char


if __name__ == '__main__':
    choice = input('Enter Encrypt/Decrypt(e/d): ')
    if choice == 'e':
        public = input('Enter public message: ')
        private = input('Enter private message: ')

        result = encrypt(private, public)
        print(f'The encrypted message is \n{result}')
    else:
        message = input('Enter: ')
        result = decrypt(message)

        print(f'The Decrypted Message is \n{result}')
