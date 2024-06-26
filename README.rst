
########
Overview
########


|Stable| |Openflow| |Tag| |Release| |License| |Build| |Coverage| |Quality|

*python-openflow* is a low level library to parse and create OpenFlow messages.
If you want to read an OpenFlow packet from an open socket or send a message to
an OpenFlow switch, this is your best friend. The main features are: high
performance, short learning curve and free software license.

This library is part of `Kytos-NG project <http://kytos-ng.github.io>`_, but feel free to
use this simple and intuitive library in other projects.

.. attention::
   *python-openflow* does not perform I/O operations. To communicate with a
   switch, you must write your own controller using this library or use our
   `Kytos-NG SDN Platform <http://kytos-ng.github.io/>`_.

A quick start follows for you to check whether this project fits your needs.
For a more detailed documentation, please check the `python-openflow API
Reference Manual <http://docs.kytos.io/developer/pyof/>`_.

Quick Start
***********

Installing
==========

In order to use this software please install python3.11 into your
environment beforehand.

We are doing a huge effort to make Kytos and its components available on all
common distros. So, we recommend you to download it from your distro repository.

But if you are trying to test, develop or just want a more recent version of our
software no problem: Download now, the latest release (it still a beta
software), from our repository:

First you need to clone `python-openflow` repository:

.. code-block:: shell

   $ git clone https://github.com/kytos-ng/python-openflow.git

After cloning, the installation process is done by standard `setuptools` install
procedure:

.. code-block:: shell

   $ cd python-openflow
   $ sudo python3 -m pip install .

Alternatively, if you are a developer and want to install in develop mode:

.. code-block:: shell

   $ cd python-openflow
   $ python3 -m pip install --editable .

To install the kytos environment, please follow our
`development environment setup <https://github.com/kytos-ng/documentation/blob/master/tutorials/napps/development_environment_setup.rst>`_.

Basic Usage Example
===================

See how it is easy to create a feature request message with this library.  You
can use ipython3 to get the advantages of autocompletion:

.. code-block:: python

    >>> from pyof.v0x01.controller2switch.features_request import FeaturesRequest
    >>> request = FeaturesRequest()
    >>> print(request.header.message_type)
    Type.OFPT_FEATURES_REQUEST

If you need to send this message via socket, call the ``pack()`` method to get
its binary representation to be sent through the network:

.. code:: python

    >>> binary_msg = request.pack()
    >>> print(binary_msg)
    b"\x01\x05\x00\x08\x14\xad'\x8d"
    >>> # Use a controller (e.g. Kytos SDN controller) to send "binary_msg"

To parse a message, use the ``unpack()`` function:

.. code:: python

   >>> from pyof.utils import unpack
   >>> binary_msg = b"\x01\x05\x00\x08\x14\xad'\x8d"
   >>> msg = unpack(binary_msg)
   >>> print(msg.header.version)
   UBInt8(1) # OpenFlow 1.0
   >>> print(msg.header.message_type)
   Type.OFPT_FEATURES_REQUEST

Please, note that this library do not send or receive messages via socket. You
have to create your own server to receive messages from switches. This library
only helps you to handle OpenFlow messages in a more pythonic way.

Authors
*******

For a complete list of authors, please open ``AUTHORS.rst`` file.


License
*******

This software is under *MIT-License*. For more information please read
``LICENSE`` file.


.. |Stable| image:: https://img.shields.io/badge/stability-stable-orange.svg
.. |Openflow| image:: https://img.shields.io/badge/Openflow-1.3-brightgreen.svg
   :target: https://www.opennetworking.org/images/stories/downloads/sdn-resources/onf-specifications/openflow/openflow-switch-v1.3.5.pdf
.. |Tag| image:: https://img.shields.io/github/tag/kytos-ng/python-openflow.svg
   :target: https://github.com/kytos-ng/python-openflow/tags
.. |Release| image:: https://img.shields.io/github/release/kytos-ng/python-openflow.svg
   :target: https://github.com/kytos-ng/python-openflow/releases
.. |License| image:: https://img.shields.io/github/license/kytos-ng/python-openflow.svg
   :target: https://github.com/kytos-ng/python-openflow/blob/master/LICENSE
.. |Build| image:: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/badges/build.png?b=master
   :alt: Build status
   :target: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/?branch=master
.. |Coverage| image:: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/badges/coverage.png?b=master
   :alt: Code coverage
   :target: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/?branch=master
.. |Quality| image:: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/badges/quality-score.png?b=master
   :alt: Code-quality score
   :target: https://scrutinizer-ci.com/g/kytos-ng/python-openflow/?branch=master
