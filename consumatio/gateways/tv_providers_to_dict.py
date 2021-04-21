def tv_providers_to_dict(data, country):

    providers = []

    if country not in data['results']:
        return {
            "providers": providers
        }
    else:
        data = data['results'][country]

    if "flatrate" not in data:
        return {
            "providers": providers
        }

    for index in range(len(data.get("flatrate"))):
        provider = {
            "name": data.get("flatrate")[index].get("provider_name")
        }
        providers.append(provider)
    
    dict = {
        "providers": providers
    }

    return dict