import deepmaldetect as dmd

dest = "sample.exe"
raw_data = open(dest, "rb").read()
pred = dmd.predict(raw_data) > 0.5

print(f"{dest}: {pred}")
