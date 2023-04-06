# Intermediate Python
# https://hellogithub.com/repository/d7f416f2d9a24768baa99319b46d4710
# https://docs.pythontab.com/interpy/ 中文版


# *args 和 **kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
# *args 是用来发送一个非键值对的可变数量的参数列表给一个函数
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

# first normal arg: yasoob
# another arg through *argv: python
# another arg through *argv: eggs
# another arg through *argv: test

# **kwargs 的用法
# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me(name="yasoob")

# name == yasoob
