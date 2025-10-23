import detector

dest = "sample.exe"
pe_data = open(dest, "rb").read()
pred = detector.predict(pe_data) > 0.5

print(f"{dest}: {pred}")
