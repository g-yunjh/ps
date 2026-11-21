def custom_len(word):
    return len(word.replace("c=", '/').replace("c-", '|').replace("dz=", '#').replace("d-", '@').replace("lj", '%').replace("nj", '_').replace("s=", '$').replace("z=", '^'))

word = input()
print(custom_len(word))

