def tv_providers_to_dict(data: dict, country: str) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :param country: <str> Country to get providers for
    :return: <dict> Internal representation
    """

    providers = []

    if country not in data['results']:
        return {"providers": providers}
    else:
        data = data['results'][country]

    if "flatrate" not in data:
        return {"providers": providers}

    for index in range(len(data.get("flatrate"))):
        provider = {"name": data.get("flatrate")[index].get("provider_name")}
        providers.append(provider)

    dict = {"providers": providers}

    return dict