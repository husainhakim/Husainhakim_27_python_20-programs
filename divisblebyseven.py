class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisablebyseven(self):
        for num in range(1, self.n ):  
            if num % 7 == 0:
                yield num


number =int(input("Enter number:-")) 
if number >= 7:
    divisibleseven = DivisibleBySeven(number)

    generator = divisibleseven.divisablebyseven()
    print(f"Numbers divisible by 7 between 0 and {number}:")
    for num in generator:
     print(num)
else:
    print("No numbers are between 0 and",number,"by 7")