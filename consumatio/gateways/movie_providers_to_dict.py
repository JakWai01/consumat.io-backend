def movie_providers_to_dict(data):

    providers = []
    for index in range(len(data.get("flatrate"))):
        provider = {
            "name": data.get("flatrate")[index].get("provider_name")
        }
        providers.append(provider)

    dict = {
        "providers": providers
    }

    return dict
