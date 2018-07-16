from unittest import TestCase

from lazyclass import lazyclass


class LazyClassTests(TestCase):
    def test_lazyclass_register_decorator(self):
        @lazyclass.register
        class A(object):
            pass

        self.assertIn('A', lazyclass.classes)
        self.assertEqual(A, lazyclass.classes['A'])

    def test_lazyclass_get_attr(self):
        class A(object):
            pass
        lazyclass.classes['A'] = A

        self.assertEqual(A, lazyclass.get_class('A'))
