import unittest


class TestAssertions(unittest.TestCase):

    def test_equality(self) -> None:
        self.assertEqual(10, 10, "Values should be equal")
        self.assertNotEqual(10, 5, "Values should not be equal")

    def test_numeric_comparisons(self) -> None:
        self.assertGreater(10, 5, "10 should be greater than 5")
        self.assertLess(5, 10, "5 should be less than 10")
        self.assertGreaterEqual(10, 10)
        self.assertLessEqual(5, 5)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)

    def test_boolean(self) -> None:
        self.assertTrue(5 > 3)
        self.assertFalse(5 < 3)

    def test_none_values(self) -> None:
        self.assertIsNone(None)
        self.assertIsNotNone(42)

    def test_identity(self) -> None:
        a: list[int] = [1, 2, 3]
        b: list[int] = a
        self.assertIs(a, b, "Should refer to same object")

    def test_membership(self) -> None:
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
        self.assertIn("key", {"key": "value"})

    def test_type_checking(self) -> None:
        self.assertIsInstance("hello", str)
        self.assertNotIsInstance(42, str)

    def test_string_matching(self) -> None:
        self.assertRegex("test123", r"\d+", "Should contain digits")
        self.assertNotRegex("test", r"\d+")

    def test_collections(self) -> None:
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertTupleEqual((1, 2), (1, 2))
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})
        self.assertDictEqual({"a": 1}, {"a": 1})

    def test_exceptions(self) -> None:
        with self.assertRaises(ValueError):
            int("invalid")

    def test_exception_message(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid literal"):
            int("invalid")

    def test_with_subtest(self) -> None:
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0 if i % 2 == 0 else 1)


if __name__ == "__main__":
    unittest.main()
