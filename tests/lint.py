#!/usr/bin/env python

import os
import tempfile
import unittest


def create_hook():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write("""
#!/usr/bin/env python

import sys


class NullFile(object):

    def __init__(self, *args, **kwargs):
        pass

    def write(self, data):
        pass

    def read(self, n=0):
        return ""

    def readable(self):
        return True

    def writable(self):
        return True

    def seek(self, offset, whence):
        pass

    def close(self):
        pass

    def flush(self):
        pass

    def fileno(self):
        raise NotImplementedError()

    def isatty(self):
        return False

    def next(self):
        raise StopIteration()

    def readline(self, limit):
        return ""

    def readlines(self, hint):
        return []

    def tell(self):
        return 0

    def truncate(self, pos):
        pass

    def writelines(self, data):
        pass


sys.stderr = NullFile()
sys.stdout = NullFile()
    """)
    f.close()
    return f.name


def remove_hook(path):
    os.unlink(path)


class LintTest(unittest.TestCase):

    def test_lint(self):
        try:
            import pylint.lint
        except ImportError:
            return

        hook_path = create_hook()
        results = pylint.lint.Run(args=["--init-hook=execfile('" + hook_path + "')", "CraftProtocol"], exit=False)
        remove_hook(hook_path)

        self.assertGreaterEqual(results.linter.stats['global_note'], 7.0)


if __name__ == "__main__":
    unittest.main()
