class utils:
    def reverse(self, num):
        reversed = 0
        while num != 0:
            digit = num % 10
            reversed = digit + reversed * 10 
            num = num // 10
        return reversed

    def formatter(self, num):
        binary, octal = '', ''
        num_copy = num
        while num != 0:
            rem = num % 2
            num = num // 2
            binary = str(rem) + binary

        while num_copy != 0:
            rem = num_copy % 8
            num_copy = num_copy // 8
            octal = str(rem) + octal

        return binary, octal
