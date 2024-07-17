import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy

# 1) Wczytanie obrazka z użyciem OpenCV
image = cv2.imread("nazwa_obrazka.jpg")

# 2) Wyświetlenie obrazka z użyciem OpenCV
cv2.imshow("Obrazek", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3) Wyświetlenie obrazka z użyciem matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# 4) Przekonwertowanie obrazka z użyciem OpenCV i ponowne wyświetlenie z użyciem matplotlib
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()





##################   2   ########################

# 1) Wczytanie obrazka z użyciem PIL
image = Image.open("nazwa_obrazka.jpg")

# 2) Wyświetlenie obrazka z użyciem OpenCV
image_cv = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
cv2.imshow("Obrazek", image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3) Wyświetlenie obrazka z użyciem matplotlib
plt.imshow(image)
plt.axis("off")
plt.show()

# 4) Przekonwertowanie obrazka z użyciem OpenCV i ponowne wyświetlenie z użyciem matplotlib
gray_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()






##################   3   ########################

# 1) Uruchomienie kamery z użyciem OpenCV
cap = cv2.VideoCapture(0)

while True:
    # Odczytanie klatki z kamery
    ret, frame = cap.read()

    # 2) Zapis obrazu po naciśnięciu klawisza 'x'
    if cv2.waitKey(1) & 0xFF == ord('x'):
        cv2.imwrite("zapisany_obraz.jpg", frame)
        print("Obraz zapisany.")
        break

    # Wyświetlenie klatki z kamery
    cv2.imshow("Kamera", frame)

# 3) Zamknięcie otwartych okienek
cv2.destroyAllWindows()

# 4) Zamknięcie połączenia z kamerką
cap.release()

# 5) Wyświetlenie zapisanego obrazu z użyciem matplotlib
saved_image = cv2.imread("zapisany_obraz.jpg")
plt.imshow(cv2.cvtColor(saved_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()






##################   4   ########################

# 1) Wczytanie obrazka z użyciem OpenCV
image = cv2.imread("pobrane.jpg")

# 2) Wykrywanie twarzy w okularach przy użyciu metody Haar Cascades
# Ścieżka do pliku XML zawierającego szablony Haar Cascades dla wykrywania twarzy w okularach
haar_cascade_file = "haarcascade_eye_tree_eyeglasses.xml"
face_cascade = cv2.CascadeClassifier(haar_cascade_file)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 3) Wypisanie liczby wykrytych obiektów
print("Liczba wykrytych twarzy w okularach:", len(faces))