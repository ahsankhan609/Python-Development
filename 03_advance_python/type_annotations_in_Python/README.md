# The essential guide to type annotations in Python for writing cleaner and more robust code.

This course is taught by [Indently.io](#)

There are many types to use type annotations, so we will learn such methods in this course.

**text annotation** is just a **hint** of what **type of variable** is -> `name:str = 'John'`. it means that we are 
telling code editor, that the variable `name` should be of type `string`. but if we change the variable `name` type to 
`int` the code editor will complaint.

it makes our code safe & reliable. this course is for some experienced developers, who know the basics of python.

---

## Course Resources:
- [Course Github](#)
- [Youtube](#)

---

## Check strict type annotation with `mypy` library:

```bash
uv run mypy lambda_function.py
```

---

🎓 سیکھنے کے اہم نکات

Sequence کیا guarantee کرتا ہے؟

- __len__() — length معلوم ہو سکتی ہے
- __getitem__() — index سے access ہو سکتا ہے
- Ordering — elements کی ترتیب مقرر ہوتی ہے

Iterable صرف کیا guarantee کرتا ہے؟

- __iter__() — صرف loop چلا سکتے ہیں، بس!

**-1 return** کرنا کیوں برا ہے؟

کیونکہ return type str ہے، اگر -1 (int) return کریں تو type contract ٹوٹ جاتا ہے۔ Empty کے لیے یا تو ValueError raise کریں یا Optional[str] return type رکھ کر None return کریں۔

---
