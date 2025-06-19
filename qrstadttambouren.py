import qrcode

# Inhalt, der im QR-Code enthalten sein soll
data = "https://stadttambouren-wil.ch"

# QR-Code erstellen
qr = qrcode.make(data)

# Bild speichern
qr.save("qr_stadttambouren.png")