"""Test Base module of python-openflow."""
import unittest

from pyof.foundation import base, basic_types


class TestGenericStruct:
    """Testing GenericStruct class."""

    def setup_method(self):
        """Basic Test Setup."""
        class AttributeA(base.GenericStruct):
            """Example class."""

            a1 = basic_types.UBInt8(1)
            a2 = basic_types.UBInt16(2)

        class AttributeC(base.GenericStruct):
            """Example class."""

            c1 = basic_types.UBInt32(3)
            c2 = basic_types.UBInt64(4)

        class AttributeB(base.GenericStruct):
            """Example class."""

            c = AttributeC()

        class Header(base.GenericStruct):
            """Mock Header class."""

            version = basic_types.UBInt8(1)
            message_type = basic_types.UBInt8(2)
            length = basic_types.UBInt8(8)
            xid = basic_types.UBInt8(4)

        class MyMessage(base.GenericMessage):
            """Example class."""

            header = Header()
            a = AttributeA()
            b = AttributeB()
            i = basic_types.UBInt32(5)

            def __init__(self):
                """Init method of example class."""
                super().__init__(None)

        self.MyMessage = MyMessage

    def test_basic_attributes(self):
        """[Foundation/Base/GenericStruct] - Attributes Creation."""
        message1 = self.MyMessage()
        message2 = self.MyMessage()
        assert message1 is not message2
        assert message1.i is not message2.i
        assert message1.a is not message2.a
        assert message1.b is not message2.b
        assert message1.a.a1 is not message2.a.a1
        assert message1.a.a2 is not message2.a.a2
        assert message1.b.c is not message2.b.c
        assert message1.b.c.c1 is not message2.b.c.c1
        assert message1.b.c.c2 is not message2.b.c.c2


class TestGenericType:
    """Testing GenericType class."""

    def test_basic_operator(self):
        """[Foundation/Base/GenericType] - Basic Operators."""
        a = basic_types.UBInt32(1)
        b = basic_types.UBInt32(2)

        assert a + 1 == 2
        assert 1 + a == 2
        assert b + 1 == 3
        assert 1 + b == 3

        assert a - 1 == 0
        assert 1 - a == 0
        assert b - 1 == 1
        assert 1 - b == 1

        assert a & 1 == 1
        assert 1 & a == 1
        assert b & 1 == 0
        assert 1 & b == 0

        assert a | 1 == 1
        assert 1 | a == 1
        assert b | 1 == 3
        assert 1 | b == 3

        assert a ^ 1 == 0
        assert 1 ^ a == 0
        assert b ^ 1 == 3
        assert 1 ^ b == 3
