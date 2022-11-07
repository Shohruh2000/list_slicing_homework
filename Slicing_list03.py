def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    ls = []
    ls1 = ls+list1
    return list1 + ls1[::-1]