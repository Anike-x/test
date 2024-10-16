from abc import ABC, abstractmethod


# 在 Python 中，所有的属性和方法默认都是公开的。但是，我们可以通过一些约定来模拟公共、保护和私有属性：
# 公共属性：公共属性可以在类的任何地方访问。在你的 Dog 类中，name 和 age 就是公共属性。
# 保护属性：保护属性在 Python 中是以一个下划线 _ 开头的。这是一种约定，意味着这个属性应该被视为非公开的，但是 Python 不会阻止你访问或修改它。
# 私有属性：私有属性在 Python 中是以两个下划线 __ 开头的。Python 会对这些属性进行名称改编，使得它们不能在类的外部直接访问。
# 在 Python 中，构造方法是 __init__ 方法，析构方法是 __del__ 方法。
# Python 不支持像 C++ 那样的虚方法和虚基类，但是我们可以通过使用抽象基类（Abstract Base Class, ABC）来达到类似的效果。

# ABC是abc模块中的一个类，全名是 Abstract Base Class
# Animal类继承了 ABC，这意味着Animal是一个抽象基类。@abstractmethod装饰器表示make_sound方法是一个抽象方法，这意味着任何继承 Animal 的类都必须实现 make_sound 方法。
# 如果尝试创建一个 Animal 类的实例，或者创建一个继承 Animal 但没有实现 make_sound 方法的类的实例，Python 都会抛出 TypeError
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name: str = "", age: int = 0):
        self.name = name  # 公共属性
        self._age = age  # 保护属性
        self.__secret = "This is a secret."  # 私有属性

    def sit(self):
        print(self.name.title())  # title()会将每个单词首字母变为大写

    def set_name(self, name):
        self.name = name

    def make_sound(self):
        print("Woof!")

    def __del__(self):
        print(f"Destructor called,{self.name} Dog deleted.")


class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")


# 使用类名直接调用静态方法
MyClass.my_static_method()  # 输出：This is a static method.

dog = Dog()
dog.make_sound()  # 输出：Woof!
del dog  # 输出：Destructor called, Dog deleted.
