from unittest import *    
import doctest
import io
from contextlib import redirect_stdout


def function_to_unittest(list):
    ordered = []
    for item in list:
        if item < 0:
            item *= -1
            item += 1
            
        if item % 2 == 1:
            if not is_prime(item):
                continue
        ordered = insert(item, ordered)
    return ordered


def insert(item, list):
    for index in range(0, len(list)):
        if list[index] > item:
            list.insert(index, item)
            break
    else:
        list.append(item)

    return list


def is_prime(n):
    """
    Testing Inspection docs function - Wow many docs
    """
    if n < 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True



    

class ExerciseTest(TestCase):
    def setUp(self):
        self.inputList = []
        for i in range(50):
            self.inputList.append(i)
            self.inputList.append(i*-1)
        self.inputList.reverse()
        #TODO schrijf hier globale dingen die nodig zijn voordat de tests gedraait gaan worden.
        pass # Pass om syntax errors te voorkomen in de notebook

    #TODO definieer hieronder je tests
    # LET OP: de functies die je als tests schrijft moeten in de naam met 'test' beginnen!
    def test_1(self): # voorbeeld
        input = self.inputList
        output = function_to_unittest(input)
        # print(output)
        self.assertEqual([0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 22, 22, 23, 23, 24, 24, 26, 26, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 34, 34, 36, 36, 37, 37, 38, 38, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 46, 46, 47, 47, 48, 48, 50], output, "test for Functio_to_unittest() has failed")
        pass # Pass om syntax errors te voorkomen in de notebook
            
        
test = ExerciseTest()
suite = TestLoader().loadTestsFromModule(test)
TextTestRunner().run(suite)