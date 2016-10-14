def get_full_name_or_username(user):
    result = []
    if user.first_name or user.last_name:
        if user.last_name:
            result.append(user.last_name)
        if user.first_name:
            result.append(user.first_name)
    else:
        result.append(user.username)

    return " ".join(result)