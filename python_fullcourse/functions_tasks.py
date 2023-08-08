def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    return max(a,b)

def animal_crackers(text):
    words = text.lower().split()
    if len(words) != 2:
        print('Input Two words in one string argument')
        return False
    return words[0][0] == words[1][0]

def makes_twenty(n1,n2):
    return n1 == 20 or n2==20 or sum([n1,n2])==20


##tasks Level One
def old_macdonald(name):
    first_part = name[:3].capitalize()
    second_part = name[3:].capitalize()
    return first_part + second_part

def master_yoda(sentence):
    return ' '.join(sentence.split()[::-1])


def almost_there(n):
    return abs(100-n) <=10 or abs(200-n) <=10
##плохо читается(непонятно что делает)
##    return 90<=n<=110 or 190<=n<=210

##tasks Level Two
def has_33(arr):
    for i in range(len(arr)-1):
        if arr[i]==3 and arr[i+1]==3:
            return True
    return False

def paper_doll(text):
    result = ''
    for char in text:
        result+=char*3
    return result

def blackjack(n1,n2,n3):
    if (nums_sum := sum([n1,n2,n3]))<=21:
        return nums_sum
    if 11 in [n1,n2,n3] and nums_sum <= 31:
        return nums_sum-10
    else:
        return "BUST"

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total+=num
                break
            add=False
        while not add:
            if num!=9:
                break
            add=True
    return total
                

        
##Hard tasks
def spy_game(nums):
    code = [0,0,7,'chivi']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1


def count_primes(num):
    if num<2:
        return 0
    
    primes_count = 1
    for x in range(3,num+1,2):
        count=0
        for i in range(3,x//2+1,2):
            if x%i==0:
                count+=1
                break
        else:
            primes_count+=1

    return primes_count


        
