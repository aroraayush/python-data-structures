class Outer:
    """Outer Class"""

    def __init__(self):
        ## Instantiating the 'Inner' class
        self.inner = self.Inner()
        ## Instantiating the '_Inner' class
        self._inner = self._Inner()

    def show_classes(self):
        print("\nThis is Outer class")
        print("inner : ", inner)
        print("_inner : ", _inner)

    class Inner:
        """First Inner Class"""

        def inner_display(self, msg):
            print("inner_display - This is Inner class")
            print("inner_display : (msg) :", msg)

    class _Inner:
        """Second Inner Class"""

        def inner_display(self, msg):
            print("_inner : This is _Inner class")
            print("_inner : ", msg)

## instantiating the classes

## 'Outer' class
outer = Outer()
## 'Inner' class
inner = outer.Inner() ## inner = outer.inner or inner = Outer().Inner()
## '_Inner' class
_inner = outer._Inner() ## _inner = outer._outer or _inner = Outer()._Inner()

## calling the methods
outer.show_classes()

print()

## 'Inner' class
inner.inner_display("Just Print It!")

print()

## '_Inner' class
_inner.inner_display("Just Show It!")