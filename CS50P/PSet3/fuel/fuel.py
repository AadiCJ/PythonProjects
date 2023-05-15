def main():
    while True:  # loop keeps executing till broken
        fraction = input("What is your fuel fraction? ")  # prompt
        if "/" in fraction:
            x, y = fraction.split("/")  # get the two components of the fraction
        else:
            continue
        try:
            x = int(x)
            y = int(y)  # typecast to int
        except ValueError:
            continue  # move to next iteration, prompt again

        if x > y:  # fuel cant be greater than 100%
            continue  # move to next iteration prompt again

        try:
            div = x / y
            if div >= 0.99:
                print("F")
            elif div <= 0.01:
                print("E")
            else:
                print(int(round(div * 100)), "%", sep="")
            break  # if everything works exit loop
        except ZeroDivisionError:  # division by zero not accepted
            continue  # move to next iteration prompt again


main()
