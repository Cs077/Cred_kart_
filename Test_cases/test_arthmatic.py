class Test_2 :

    def test_add_01(self):
        a=12
        b=21
        print(f"addition of a+b:{a+b}")

    def test_mul_02(self):
        a=22
        b=2
        print(f"multiple of a*b:{a*b}")


    def test_div_03(self):
        a=420
        b=10
        print(f"division of a/b:{a/b}")
        assert a/b ==42