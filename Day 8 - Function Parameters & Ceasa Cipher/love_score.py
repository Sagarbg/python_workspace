def calculate_love_score(name1, name2):

    nm1 = name1.lower()
    nm2 = name2.lower()

    nm_arr1 = [nm1]
    nm_arr2 = [nm2]

    c_arr = name1 + name2
    print(c_arr.count("e"))
    print(c_arr)

    re1 = c_arr.count("t") + c_arr.count("r") + c_arr.count("u") + c_arr.count("e")
    re2 = c_arr.count("l") + c_arr.count("o") + c_arr.count("v") + c_arr.count("e")

    print(f"{re1}{re2}")


    # print(c_arr.count("t") + c_arr.count("r") + c_arr.count("u") + c_arr.count("e"))

    # print(c_arr.count("l") + c_arr.count("o") + c_arr.count("v") + c_arr.count("e"))
    

calculate_love_score("Kanye West", "Kim Kardashian")
