def total_pages_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    dict = {"total_pages": data["total_pages"]}
    dict["__typename"] = "TotalPages"
    return dict
