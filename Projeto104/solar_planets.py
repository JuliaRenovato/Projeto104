import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 2,
            color = (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (110,180),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,270),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.putText(img,
            "Terra",
            (300,270),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.putText(img,
            "Marte",
            (400,270),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (500,90),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 1,
            color = (255,255,255)
            )

cv2.putText(img,
            "Saturno",
            (720,110),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.putText(img,
            "Urano",
            (950,130),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.putText(img,
            "Netuno",
            (1080,130),
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.7,
            color = (255,255,255)
            )

cv2.imshow("resultado", img)
cv2.waitKey(0)