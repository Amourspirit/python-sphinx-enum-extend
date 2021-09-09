#!coding: utf-8
from typing import Any, Optional
from sphinx import __version__
from docutils.statemachine import StringList
from sphinx.ext.autodoc import ClassDocumenter, bool_option
from enum_extend import AutoEnum

# region AutoEnumDocumenter

class AutoEnumDocumenter(ClassDocumenter):
    # https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html
    objtype = '_autoenum'
    directivetype = 'class'
    priority = 10 + ClassDocumenter.priority
    option_spec = dict(ClassDocumenter.option_spec)
    option_spec['hex'] = bool_option

    @classmethod
    def can_document_member(cls,
                            member: Any, membername: str,
                            isattr: bool, parent: Any) -> bool:
        return isinstance(member, AutoEnum)

    def add_directive_header(self, sig: str) -> None:
        super().add_directive_header(sig)
        self.add_line('   :final:', self.get_sourcename())

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        super().add_content(more_content)

        source_name = self.get_sourcename()
        enum_object: AutoEnum = self.object
        use_hex = self.options.hex
        self.add_line('', source_name)

        indent_str = '    '
        for enum_value in enum_object:
            the_value_name = enum_value.name
            the_value_value = enum_value.value
            the_docstring: str = enum_value.__doc__
            valid_docstring = False
            if use_hex:
                the_value_value = hex(the_value_value)

            # self.add_line(f"**{the_value_name}**\= {the_value_value}", source_name)
            self.add_line("**{}**\= {}".format(
                the_value_name,
                the_value_value
            ), source_name)
            if the_docstring.strip():  # not a blank line
                indent = self.indent
                self.indent = indent + indent_str
                docstrings = the_docstring.splitlines()
                for i, line in enumerate(self.process_doc([docstrings])):
                    self.add_line(line, source_name, i)
                self.add_line('', source_name)
                self.indent = indent
                valid_docstring = True

            if not valid_docstring:
                # this is a bit of hack
                # when there is no enum doc string provided
                # this section will inject a non printing character
                # with an indent. This will result in the Name, Value having special formating applied
                # as the case when there is a doc string provided
                indent = self.indent
                self.indent = indent + indent_str
                self.add_line(u"\u007f", source_name)
                self.indent = indent

# endregion AutoEnumDocumenter

def setup(app):
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(AutoEnumDocumenter)
