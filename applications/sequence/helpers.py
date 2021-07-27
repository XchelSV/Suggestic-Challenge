def flattener(sequence):
    sequence_length = len(sequence)
    if sequence_length <= 1:
        if sequence_length == 1 and isinstance(sequence[0], list):
            return flattener(sequence[0])
        return sequence
    else:
        k = sequence_length // 2
        return flattener(sequence[:k]) + flattener(sequence[k:])