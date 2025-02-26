import cv2
def check_images():
    try:
        tharoor = cv2.imread('Dr_Shashi_Tharoor.jpg')
        plaksha = cv2.imread('Plaksha_Faculty.jpg')

        if tharoor is None or plaksha is None:
            raise Exception
        
    except:
        print("not found or unreadable")
