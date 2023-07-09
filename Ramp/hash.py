import hashlib


def mian():
    salt = '9a98639e5354'
    flag = 'a588a36cb83c8a5836974a756cc01771'
    for line in open("word-list-7-letters.txt"):
        #print(hashlib.md5(line[:7].encode()).hexdigest())
        if hashlib.md5((line[:7]+salt).encode()).hexdigest() == flag:
            print(line[:7])
            break


if __name__ == "__main__":
    mian()
