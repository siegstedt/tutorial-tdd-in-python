def convert_to_int(integer_string_with_commas: str) -> int:
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None

    integer_string_with_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_with_commas)
    except ValueError:
        return None
