import os
from pathlib import Path 

__all__ = []

parent_path = Path(__file__).parent
for f in parent_path.iterdir():
	if f.name[0].isalpha() and f.is_file():
		m = f.name.split(".")[0]
		exec(f"from .{m} import {m}")
		__all__.append(m)
