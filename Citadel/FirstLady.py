def main(n_process: int, n_interval: int):
    if n_process == 0 or n_interval == 0:
        return 0
    if n_process == 1:
        return 1
    if n_interval == 1:
        return n_process
    return n_process * ((n_process - 1) ^ (n_interval - 1))


if __name__ == "__main__":
    print(main(2, 3))
