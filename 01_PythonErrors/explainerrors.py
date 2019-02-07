"""
Header: UW 2017 - Intro To Python
Topic: Python Error Types
Author: PydPiper

Objective: Demonstrate your knowledge of python error types by throwing as many errors as possible.
"""

class ExplainErrors:

    @classmethod
    def throw_syntax(cls):
        """
        SyntaxError Example:
        > print 'something'

        Throws a SyntaxError due to incorrect python syntax
        The intended syntax here was supposed to be print('something')
        Learning the syntax of any language comes with practice, but always check out
        the python PEP8 style guide first then the python docs

        :return:None
        """

        print(cls.throw_syntax.__doc__)

        eval("print 'something'")

    @classmethod
    def throw_type(cls):
        """
        TypeError Example:
        > 5 + 'a'

        Throws a TypeError since addition of a integer and string mismatch in type and strings dont support integer
        addition, however '5' + 'a' would have worked. Give it a shot!

        :return: None
        """

        print(cls.throw_type.__doc__)

        eval("5 + 'a'")

    @classmethod
    def throw_index(cls):
        """
        IndexError Example:
        mylist = [1, 2, 3]
        mylist[3]

        Throws a IndexError since mylist cannot be indexed beyond 2. Python starts it's 1st index at 0,
        therefore mylist has the following indices:
        mylist[0] is 1
        mylist[1] is 2
        mylist[2] is 3

        :return: None
        """

        print(cls.throw_index.__doc__)

        mylist = [1, 2, 3]
        eval("mylist[3]")

    @classmethod
    def throw_key(cls):
        """
        KeyError Example:
        mydict = {'a': 1, 'b': 2}
        mydict['c']

        Throws a KeyError since there is no keyword 'c' in mydict.

        :return: None
        """

        print(cls.throw_key.__doc__)

        mydict = {'a': 1, 'b': 2}
        eval("mydict['c']")

    @classmethod
    def throw_attribute(cls):
        """
        AttributeError Example:
        mylist = ['1', '2', '3']
        mylist.split()

        Throws a AttributeError since the list object does not have a attribute called split. However strings do.
        The following whould have worked: '1 2 3'.split() and in fact it would have yielded back mylist

        :return: None
        """

        print(cls.throw_attribute.__doc__)

        mylist = ['1', '2', '3']
        eval("mylist.split()")

    @classmethod
    def throw_name(cls):
        """
        NameError Example:
        x = y

        Throws a NameError because 'y' has not been defined in the current runtime.

        :return: None
        """

        print(cls.throw_name.__doc__)

        x = y

    @classmethod
    def throw_OS(cls):
        """
        OSError Example:
        with open("file.txt", "r") as f:
            pass

        Throws a OSError since "file.txt" does not exist, therefore python cannot read it.

        :return: None
        """

        print(cls.throw_OS.__doc__)

        with open("file.txt", "r") as f:
            pass

    @classmethod
    def throw_recursion(cls):
        """
        RecursionError Example:
        def endless(value):
            return endless(value + 1)

        Throws a RecursionError since there is no end condition for the code to stop calling itself.
        A fix would be:

        def endless(value):
            if value > 10:
                return "you reached the end"
            else:
                return endless(value + 1)

        :return: None
        """

        print(cls.throw_recursion.__doc__)

        def endless(value):
            return endless(value + 1)

        endless(1)

    @classmethod
    def throw_stopiter(cls):
        """
        StopIteration Example:
        my_iter = zip([1, 10], [2, 20], [3, 30])
        next(my_iter)
        > (1, 2, 3)
        next(my_iter)
        > (10, 20, 30)
        next(my_iter)
        > yields the error since we hit the end of the iterations

        :return: None
        """

        print(cls.throw_stopiter.__doc__)
        my_iter = zip([1, 10], [2, 20], [3, 30])
        next(my_iter)
        next(my_iter)
        next(my_iter)
