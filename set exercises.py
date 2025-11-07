post1 = {"Subin", "Vishnu", "Nihal", "Sachin", "Dhoni", "Farzeen"}
post2 = {"Vishnu", "Nihal", "Dhoni", "Tendulkar"}
post3 = {"Nihal", "Hari", "Vishnu", "Tendulkar", "Kohli"}
operation = input("'a' : Interactors who viewed all the posts \n"
                  "'b' : Interactors who only viewed one post \n"
                  "'c' : The most popular post \n"
                  "What do you want to get? : ")
if operation == "a":
    print(" and ". join(post1.intersection(post2.intersection(post3))) + " interacted with all posts")
elif operation == "b":
    for x in post1:
        if x not in post2.union(post3) :
            print(f"{x} only interacted with post1")
    for x in post2:
        if x not in post1.union(post3):
            print(f"{x} only interacted with post2")
    for x in post3:
        if x not in post2.union(post1):
            print(f"{x} only interacted with post3")
elif operation == "c":
    if len(post1) > len(post2):
        if len(post1) > len(post3):
            print(f"The most popular post is post1 with {len(post1)} interactors ")
        elif len(post1) == len(post3):
            print(f"The most popular post is post1 and post3 with {len(post1)} interactors ")
        else:
            print(f"The most popular post is post3 with {len(post3)} interactors ")
    else:
        if len(post2) > len(post3):
            print(f"The most popular post is post2 with {len(post2)} interactors ")
        elif len(post2) == len(post3):
            print(f"The most popular post is post2 and post3 with {len(post1)} interactors ")
        else:
            print(f"The most popular post is post3 with {len(post3)} interactors ")
else:
    print("Wrong input code!")