"""
Fondre_lumiere
Creator: Lehag

Fondre est un outils python permettant de créer une image
fondu en se basant sur la luminosité a partir de deux image de même taille



"""
from PIL import Image
import os
# recuperation des nom de fichier
inp_dir = r"C:\Users\Lehag\OneDrive\Bureau\FondreImg\input"
out_dir = r"C:\Users\Lehag\OneDrive\Bureau\FondreImg\Output"

img1 = os.listdir(inp_dir)[0]
img2 = os.listdir(inp_dir)[1]

# ouverture des fichier
openimg1 = Image.open(inp_dir + "\\" + img1)
openimg2 = Image.open(inp_dir + "\\" + img2)
out_imag = Image.new(openimg1.mode,openimg1.size)

# Iterateur de boucle
x = 0
y = 0

# Boucle de fusion des pixel

    # Test de conformité des images
if openimg1.size == openimg2.size:
    print("Taille Image : OK " + str(openimg1.size))


    while x < openimg1.size[0]:
        while y < openimg1.size[1]:

            # recuperation des RGB du pixel x,y

            R1 = openimg1.getpixel((x,y))[0]
            R2 = openimg2.getpixel((x,y))[0]
            Rmoy = abs(int(round(R1-R2)))

            V1 = openimg1.getpixel((x,y))[1]
            V2 = openimg2.getpixel((x,y))[1]
            Vmoy = abs(int(round(V1-V2)))

            B1 = openimg1.getpixel((x,y))[2]
            B2 = openimg2.getpixel((x,y))[2]
            Bmoy = abs(int(round(B1-B2)))

            out_imag.putpixel((x,y),(Rmoy,Vmoy,Bmoy))

            y += 1
        y = 0
        x += 1

out_imag.save(out_dir +"\\Lumin_img.png","PNG")
out_imag.show()