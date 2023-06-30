import coverage_test
import inspect

# Lijst van element-namen in function_demo.pyc
elementen = dir(coverage_test)

# Filter de functies uit de elementenlijst
functies = [eval('coverage_test.' + x) for x in elementen if type(eval('coverage_test.' + x)).__name__ == 'function']

# Loop door elke functie en print de naam, signature en documentatie
for f in functies:
    print(f.__name__)
    print(inspect.signature(f))
    print(inspect.getdoc(f))
    print('---')