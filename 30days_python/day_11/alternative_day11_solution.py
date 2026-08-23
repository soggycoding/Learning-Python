def reverse_list(*items):
    for item in items[::-1]:
        print(item)

reverse_list('bing', 'bong', 'doot', 'bloop')