def tv_providers_to_dict(data):

    providers = []
    for provider in range(len(data.get("flatrate"))):
        providers.append(data.get("flatrate")[provider].get("provider_name"))
    
    print(providers)

    dict = {
        "providers": providers
    }

    return dict