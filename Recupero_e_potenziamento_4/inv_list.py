def recursive_inv(elements: list[int | str]) -> None:

    if not elements:
        pass
    
    else:

        print(elements[-1])

        recursive_inv(elements[:-1])


recursive_inv([1, 2, 3, 4, 5])



