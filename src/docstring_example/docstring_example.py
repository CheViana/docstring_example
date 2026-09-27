from abc import ABC, abstractmethod


class MyBaseClass(ABC):
    """
    Base class docstring.
    """
    __slots__ = ()

    @abstractmethod
    def method1(self) -> None:
        """
        method1 docstring - MyBaseClass
        """
        ...


class MyMixin(MyBaseClass):
    __slots__ = ()

    @abstractmethod
    def method2(self) -> None:
        """
        method2 docstring - MyMixin
        """
        ...


class MyOtherMixin(MyBaseClass):
    __slots__ = ()

    @abstractmethod
    def method3(self) -> None:
        """
        method3 docstring - MyOtherMixin
        """
        ...


class MyClass(MyMixin, MyOtherMixin):
    def method1(self) -> None:
        print("hello from MyClass.method1")

    def method2(self) -> None:
        print("hello from MyClass.method2")
    
    def method3(self) -> None:
        print("hello from MyClass.method3")
