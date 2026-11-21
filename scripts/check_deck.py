#!/usr/bin/env python3
import os, sys
html = open(sys.argv[1], encoding="utf-8").read()
valid = {f[:-3] for r,_,fs in os.walk(sys.argv[2]) for f in fs if f.endswith(".md")}
needed = ["NVIDIA2024-MaxQ-Thermal","Williams2009-Roofline","Dao2022-FlashAttention","Frantar2023-GPTQ-Quantization","Kwon2023-PagedAttention"]
missing = [p for p in needed if p not in html or p not in valid]
print("Missing:", missing)
sys.exit(1 if missing else 0)
