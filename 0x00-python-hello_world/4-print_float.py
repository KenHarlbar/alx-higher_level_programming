#!/usr/bin/bash
python - <<END
number = 3.14159
num = "%.2f" % number
print(f"Float: {num}")
END
