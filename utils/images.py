import imagehash

def compare_images(image1, image2, cutoff=5):
    image1 = imagehash.average_hash(image1)
    image2 = imagehash.average_hash(image2)
    if image1 - image2 < cutoff:
        return True
    return False
