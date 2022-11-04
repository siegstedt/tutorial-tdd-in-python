def convert_to_int(integer_with_commas: str) -> int:
    comma_separated_parts = integer_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    
    try:
        return int(integer_with_commas.replace(",", ""))
    except ValueError:
        return None
