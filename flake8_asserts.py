import ast


class Flake8AssertsPlugin:
    name = 'flake8-asserts'
    version = '0.1.0'

    deprecated = {
        'failUnlessEqual': 'assertEqual',
        'assertEquals': 'assertEqual',
        'assertAlmostEquals': 'assertAlmostEqual',
        'assertNotAlmostEquals': 'assertNotAlmostEqual',
        'assertNotEquals': 'assertNotEqual',
        'assertNotRegexpMatches': 'assertNotRegex',
        'assertRaisesRegexp': 'assertRaisesRegex',
        'assertRegexpMatches': 'assertRegex',
        'failIf': 'assertFalse',
        'failIfAlmostEqual': 'assertNotAlmostEqual',
        'failIfEqual': 'assertNotEqual',
        'failUnless': 'assertTrue',
        'failUnlessAlmostEqual': 'assertAlmostEqual',
        'failUnlessRaises': 'assertRaises',
        'assert_': 'assertTrue',
    }

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                try:
                    func = self.deprecated[node.func.attr]
                except KeyError:
                    pass
                else:
                    yield (
                        node.func.lineno,
                        node.func.col_offset,
                        'A100 %s is deprecated, use %s instead' % (node.func.attr, func),
                        type(self),
                    )
