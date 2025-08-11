

def saveImage():
    import requests as r
    url = "https://picsum.photos/800/600"
    response=r.get(url)
    for i in range(5):
        if response.status_code == 200:
            with open(f"image_{i}.jpg", "wb") as file:
                file.write(response.content)
            print(f"Image downloaded as image_{i}.jpg")
        else:
            print("Failed to download image")

saveImage()