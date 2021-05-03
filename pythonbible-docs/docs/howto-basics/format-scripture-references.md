---
sidebar_position: 4
---

# Format Scripture References

Given a list of normalized references, this feature formats them into a human-readable scripture reference string.

It sorts the list so that the references appear in the order they would in the Bible.
It also combines verses into ranges when possible.

For example:

```python
import pythonbible as bible

text = "My favorite verses are Philippians 4:8, Isaiah 55:13, and Philippians 4:4-7."
references = bible.get_references(text)
formatted_reference = bible.format_scripture_references(references)
```

The resulting formatted reference should be:

```python
'Isaiah 55:13;Philippians 4:4-8'
```