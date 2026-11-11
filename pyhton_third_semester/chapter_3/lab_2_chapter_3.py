with open("source.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dst:
        while True:
            chunk = src.read(8192)
            if not chunk:
                break
            dst.write(chunk)