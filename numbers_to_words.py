def num_to_words(number):
    ones = {0: 'zero', 1:'one', 2: 'two', 3: 'three', 4:'four', 5: 'five', 6 :'six', 7: 'seven', 8 :'eight', 9:'nine', 
            10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    tens = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty',9:'ninety'}
    multiples = ['hundred', 'thousand', 'million', 'billion', 'trillion']

    
    if number < 20:
        return ones[number]
    elif number in [20, 30, 40, 50, 60, 70, 80, 90]:
        return tens[int(number/10)]
    elif number < 100:
        a = int(number / 10)
        b = number % 10
        return tens[a] + " " + ones[b]
    elif number < 1000:
        a = int(number//100)
        b = int(number/10)
        c = number%10
        return 



print(num_to_words(99))