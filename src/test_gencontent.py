import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "Tolkien Fan Club"
        )

    def test_extract_title(self):
        md = """


![JRR Tolkien sitting](/images/tolkien.png)

# Test title

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "Test title"
        )