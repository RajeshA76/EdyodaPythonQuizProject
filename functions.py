#!/usr/bin/env python3
import base64

def decode(input):
    sample_string_bytes = input.encode("ascii") 
  
    base64_bytes = base64.b64encode(sample_string_bytes) 
    base64_string = base64_bytes.decode("ascii")
    return base64_string