# MIT License
#
# Copyright (c) 2024 Daemyung Jang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Details and explanations for this example can be found at
https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
"""

from contextlib import AbstractContextManager, ExitStack


class ContextManager(AbstractContextManager):
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f'Enter {self.name}.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Exit {self.name}.')
        return False


with ExitStack() as stack:
    stack.enter_context(ContextManager('Python'))
    stack.enter_context(ContextManager('C'))
    stack.enter_context(ContextManager('C++'))
