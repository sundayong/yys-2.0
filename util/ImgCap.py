from PIL import ImageGrab

def imgGrab(path):
    pic = ImageGrab.grab()
    pic.save(path)

if __name__=="__main__":
    imgGrab(1)