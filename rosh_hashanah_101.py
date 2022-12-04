import sys

def rosh_hashanah(y):
    """Calculate the Gregorian date of Rosh Hashanah.
    
    Args:
        y (int): the Gregorian year to calculate the date of Rosh Hashanah for.
    
    Side effects:
        Prints the date to stdout.
    """
    f = 12 * (y % 19 + 1) % 19
    c = y // 100
    n = (c
         - (y // 400) 
         - 2
         + ((765433 * f) / 492480)
         + ((y % 4) / 4)
         - (((313 * y) + 89081) / 98496))
    j = n // 1
    p = n % 1
    z = y % 100
    k = (j + z - 2*c + z//4 + c//4 + 4) % 7
    if k in {0, 3, 5}:
        a = 1
    elif k == 1 and p >= 23296/25920 and f > 11:
        a = 1
    elif k == 2 and p >= 1367/2160 and f > 6:
        a = 2
    else:
        a = 0
    b = j + a
    d = int((b - 1) % 30 + 1)
    m = int(9 + (b // 30))
    print(f"{m}/{d}")


if __name__ == "__main__":
    rosh_hashanah(int(sys.argv[1]))
