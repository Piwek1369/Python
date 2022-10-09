def main():
    x = 2
    def inner_method():
        nonlocal x
    x = 1
    def lambda_as_function(x):
        return x + 1
    lambda_x = lambda x : x + 1
    print(lambda_as_function(1) == lambda_x(1))

if __name__ == "__main__":
    main()
