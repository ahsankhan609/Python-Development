# JSON Module — FAQ

## File Structure

**Q: Can a JSON file contain more than one object?**
No. JSON allows exactly one root value per file. To store multiple objects, wrap them in an array:
```json
[
    { "name": "Alice" },
    { "name": "Bob" }
]
```

---

## Appending Data

**Q: Why does opening a JSON file in append mode (`"a"`) break it?**
`"a"` mode writes raw text after whatever is already in the file. Two back-to-back `json.dump` calls produce:
```json
{"name": "Alice"}{"name": "Bob"}
```
This is not valid JSON — parsers expect a single root value and raise `JSONDecodeError`.

**Q: How do I correctly append a new record to a JSON file?**
Read → modify in memory → overwrite:
```python
json_file = Path(__file__).parent / "data.json"

existing: list[dict] = []
if json_file.exists() and json_file.stat().st_size > 0:
    with json_file.open("r") as f:
        loaded = json.load(f)
    existing = loaded if isinstance(loaded, list) else [loaded]

existing.append(new_record)

with json_file.open("w") as f:
    json.dump(existing, f, indent=4)
```
The `isinstance` check safely wraps a bare `{}` dict in a list before appending.

---

## File Paths

**Q: Why should I use `Path(__file__).parent` instead of a bare filename like `Path("data.json")`?**
A bare filename resolves relative to the **current working directory** (wherever the script is run from), not the script's location. If you run the script from a different folder, the file is created or read in the wrong place.

`Path(__file__).parent` always resolves to the directory containing the script itself, making the path reliable regardless of CWD:
```python
json_file = Path(__file__).parent / "data.json"
```

---

## Serialization

**Q: How does Python map its types to JSON?**

| Python       | JSON    |
|--------------|---------|
| `dict`       | `{}`    |
| `list, tuple`| `[]`    |
| `str`        | `"..."`  |
| `int, float` | number  |
| `True/False` | `true/false` |
| `None`       | `null`  |

**Q: How do I pretty-print JSON when writing to a file?**
Pass `indent=4` to `json.dump`:
```python
json.dump(data, f, indent=4)
```

**Q: How do I read a JSON file back into Python?**
```python
with Path("data.json").open("r") as f:
    data = json.load(f)   # file → Python object

# For a JSON string (not a file):
data = json.loads('{"name": "Alice"}')
```
