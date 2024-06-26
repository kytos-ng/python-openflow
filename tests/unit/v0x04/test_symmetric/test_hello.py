"""Hello message tests."""
from pyof.v0x04.symmetric.hello import (
    Hello, HelloElemHeader, HelloElemType, ListOfHelloElements)
from tests.unit.test_struct import StructTest


class TestHello(StructTest):
    """Hello message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_hello')
        self.set_raw_dump_object(Hello, xid=62,
                                    elements=_new_list_of_elements())
        self.set_minimum_size(8)


def _new_list_of_elements():
    """Crate new ListOfHelloElements."""
    hello_elem = HelloElemHeader(HelloElemType.OFPHET_VERSIONBITMAP,
                                 length=8, content=b'\x00\x00\x00\x10')
    elements = ListOfHelloElements()
    elements.append(hello_elem)
    return elements
