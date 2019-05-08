import wrapper
import sys


if sys.argv[1] is not None:
    wrap = wrapper.Wrapper(sys.argv[1])
    wrap.iterate_folder()
