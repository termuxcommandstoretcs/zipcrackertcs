import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))