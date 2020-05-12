import unittest

from classes.point import Point


class PointTest(unittest.TestCase):
    """
          The class inherits from unittest
          """

    def setUp(self):
        """
        This method is called before each test
        """
        self.p= Point(2,3)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass
    # ---
    ## TESTS

    def test_initialise(self):
        self.assertEqual((self.p.x,self.p.y),(2,3))

    def setter(self):
        self.p.x=2

    def test_set_private(self):
        try:
            self.setter()
        except AttributeError:
            print("caught Attribute error")
            pass
        except Exception:
            self.fail("unexpected exception thrown")
        else:
            self.fail("Attribute exception not raised")
        finally:
            print("finally test completed")

if __name__=="__main__":
    unittest.main()