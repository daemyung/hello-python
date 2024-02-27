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
https://peps.python.org/pep-0544/#modules-as-implementations-of-protocols.
"""

import implementation

from arithmetic import Arithmetic

# A module object is accepted where a protocol is expected
# if the public interface of the given module is compatible with the expected protocol.
arithmetic: Arithmetic = implementation

print(f'3 + 4 = {arithmetic.add(3, 4)}')
print(f'8 - 2 = {arithmetic.sub(8, 2)}')
print(f'4 * 5 = {arithmetic.mul(4, 5)}')
print(f'9 / 3 = {arithmetic.div(9, 3)}')
