from sublime import find_resources

from phpunitkit.tests.utils import ViewTestCase
from phpunitkit.plugin import find_selected_test_methods


def _is_php_syntax_using_php_grammar():
    return 'php-grammar' in find_resources('PHP.sublime-syntax')[0]


class TestFindSelectedTestMethods(ViewTestCase):

    def test_empty(self):
        self.fixture('')
        self.assertEqual([], find_selected_test_methods(self.view))

    def test_none_when_plain_text(self):
        self.fixture('foo|bar')
        self.assertEqual([], find_selected_test_methods(self.view))

    def test_none_when_bof(self):
        self.fixture("""|<?php

            namespace User\Repository;

            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function testOne()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual([], find_selected_test_methods(self.view))

    def test_one(self):
        self.fixture("""<?php

            namespace User\Repository;

            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function testFoobar1()
                {
                    $this->assertTrue(true);
                }

                public function test|One()
                {
                    $this->assertTrue(true);
                }

                public function testFoobar2()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual(['testOne'], find_selected_test_methods(self.view))

    def test_underscore_test_methods(self):
        self.fixture("""<?php

            namespace User\Repository;

            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function test_one_un|derscore()
                {
                    $this->assertTrue(true);
                }

                public function testFoobar()
                {
                    $this->assertTrue(true);
                }

                public function test_two|_under_scored()
                {
                    $this->assertTrue(true);
                }

            }

        """)

        self.assertEqual(['test_one_underscore', 'test_two_under_scored'],
                         find_selected_test_methods(self.view))

    def test_annotated_test_methods(self):
        self.fixture("""<?php

            namespace User\Repository;

            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                /**
                 * @test
                 */
                public function o|ne()
                {
                    $this->assertTrue(true);
                }

                /** @test */
                public function tw|o()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual(['one', 'two'],
                         find_selected_test_methods(self.view))

    def test_many(self):
        self.fixture("""<?php

            namespace User\Repository;

            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function testFoobar()
                {
                    $this->assertTrue(true);
                }

                public function test|One()
                {
                    $this->assertTrue(true);
                }

                public function testFoobar()
                {
                    $this->assertTrue(true);
                }

                public function test|Two()
                {
                    $this->assertTrue(true);
                }

                public function testFoobar()
                {
                    $this->assertTrue(true);
                }

                public function test|Three()
                {
                    $this->assertTrue(true);
                }

                public function testFoobar()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual(['testOne', 'testTwo', 'testThree'],
                         find_selected_test_methods(self.view))

    def test_many_when_cursor_is_anywhere_on_method_declarations(self):
        self.fixture("""<?php
            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function foobar()
                {
                    $this->assertTrue(true);
                }

                pu|blic function testOne()
                {
                    $this->assertTrue(true);
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }

                public func|tion testTwo()
                {
                    $this->assertTrue(true);
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }

                public function testThree(|)
                {
                    $this->assertTrue(true);
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual(['testOne', 'testTwo', 'testThree'],
                         find_selected_test_methods(self.view))

    def test_many_when_cursor_is_anywhere_inside_method_declarations(self):
        if _is_php_syntax_using_php_grammar():
            # Skip because php-grammar does not support this feature
            return

        self.fixture("""<?php
            class ClassNameTest extends \PHPUnit_Framework_TestCase
            {
                public function foobar()
                {
                    $this->assertTrue(true);
                }

                public function testOne()
                {|
                    $this->assertTrue(true);
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }

                public function testTwo()
                {
                    $this->assert|True(true);
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }

                public function testThree()
                {
                    $this->assertTrue(true);
                    $this->assertTrue(true);
                    $this->assertTrue(true);
                    |
                }

                public function foobar()
                {
                    $this->assertTrue(true);
                }
            }

        """)

        self.assertEqual(['testOne', 'testTwo', 'testThree'],
                         find_selected_test_methods(self.view))