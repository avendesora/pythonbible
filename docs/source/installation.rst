Installation
============

Requirements
------------

**pythonbible** requires Python and is tested with the following versions:

* 3.10
* 3.11
* 3.12
* 3.13
* 3.14

**pythonbible** has no other dependencies.

How to Install
--------------

To use **pythonbible**, first install it using pip:

.. code-block:: console

    $ python3 -m pip install pythonbible

By default, this will only include the American Standard Version (ASV) of the Bible. To install additional versions, specify them during installation. For example, to install the King James Version (KJV):

.. code-block:: console

    $ python3 -m pip install "pythonbible[KJV]"

You can also install multiple versions at once. For example, to install the Geneva Bible (GB), the Wycliffe Bible (WYC), and the Tyndale Bible (TYN):

.. code-block:: console

    $ python3 -m pip install "pythonbible[GB,WYC,TYN]"

To install all available versions of the Bible, use:

.. code-block:: console

    $ python3 -m pip install "pythonbible[all]"
