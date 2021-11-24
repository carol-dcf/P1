def encode(bytes):
    """
    Function to encode a sequence of bytes using run-length algorithm
    :param bytes: (str) with the sequence to encode
    :return: (str) encoded sequence
    """
    bytes_to_encode = list(bytes) # String of bytes to list
    encoded_bytes = '' # Output string
    num_zeros = 0 # Counter of 0's
    for byte in bytes_to_encode:
        if (byte == '0'):
            num_zeros += 1
        else:
            # If no more consevutive 0's, add one to the list followed by the number of 0's counted
            if (num_zeros > 0):
                encoded_bytes += '0'
                encoded_bytes += str(num_zeros)
            encoded_bytes += byte
            num_zeros = 0

    return encoded_bytes