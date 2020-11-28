def age_assignment(*args, **kwargs):
    return {arg: kwargs[arg[0]] for arg in args}
    # for arg in args:
    #     result[arg] = kwargs[arg[0]]
    # return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
