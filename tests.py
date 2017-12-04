def test_deprecated(flake8dir):
    flake8dir.make_example_py(
        """
        import unittest


        class MyTest(unittest.TestCase):
            def test_thing(self):
                self.assertEquals(1, 1)
        """
    )
    result = flake8dir.run_flake8()
    expected = [
        './example.py:6:9: A100 assertEquals is deprecated, use assertEqual instead',
    ]
    assert result.out_lines == expected
