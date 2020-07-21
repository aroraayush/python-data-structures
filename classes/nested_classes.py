class Outer:

    def outer_fn(self):
        print("Function of Outer class")

    class Inner:

        def inner_fn(self):
            print("Function of Inner class")

outer = Outer()
outer.outer_fn()

inner = Outer.Inner()
inner.inner_fn()