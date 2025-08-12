#20
# class A:
#     def __init__(self,val):
#         self.val=val

#     def show(self):
#         print("A:",self.val)
# class B(A):
#     def show(self):
#         print("B:",self.val)
# class C(A):
#     def show(self):
#         print("C:",self.val)
# class D(C,B):
#     pass
# d=D(50)
# d.show()          

#19.
class A:
    def __init__(self,a):
        print("class A:",a)

class B(A):
    def __init__(self, a):
        super().__init__()