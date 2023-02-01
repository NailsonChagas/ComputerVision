import cv2

cap = cv2.VideoCapture(0) # 0 : default camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('TESTE', gray)
    
    key = cv2.waitKey(10) #recebe a tecla clicada após 10ms
    if key != -1: print(key)
    if cv2.getWindowProperty("TESTE", cv2.WND_PROP_VISIBLE) < 1:
        break
    
cap.release()
cv2.destroyAllWindows()