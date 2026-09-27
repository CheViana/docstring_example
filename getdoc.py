import inspect
from docstring_example.docstring_example import MyClass

print(inspect.getdoc(MyClass))
print(inspect.getdoc(MyClass.method1))
print(inspect.getdoc(MyClass.method2))
print(inspect.getdoc(MyClass.method3))