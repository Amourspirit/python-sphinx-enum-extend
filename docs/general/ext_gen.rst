Extension
=========

Description
-----------

Extends `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
in a way that allows for auto generation docs derived from :doc:`AutoEnum <enum_extend:class/AutoEnum>`
class.

Directive
---------

**\.\. auto_autoenum\:\:**

Options
^^^^^^^

``:hex:`` generates documents as hex. See :doc:`example hex <../ex/ex_hex>`

Usage
-----

.. code-block:: rst
   :caption: Usage

   .. auto_autoenum:: <MyClassEnum>
     :noindex:

.. code-block:: rst
   :caption: example

   .. auto_autoenum:: ex.FruitEnum
      :noindex:

.. seealso::

    | :doc:`Example <../ex/ex>`
    | :doc:`Example Hex <../ex/ex_hex>`
