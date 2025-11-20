"""
Currently Not working ;(
"""


from streetlevel import streetview
import time

url = "https://www.google.com/maps/place/Sweden/@62.2858159,14.7975707,3a,67.6y,139.68h,89.03t/data=!3m7!1e1!3m5!1s5lFl20_SnzxEHsXNblbI0g!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0.9656099192983163%26panoid%3D5lFl20_SnzxEHsXNblbI0g%26yaw%3D139.68083837114295!7i16384!8i8192!4m6!3m5!1s0x465cb2396d35f0f1:0x22b8eba28dad6f62!8m2!3d60.128161!4d18.643501!16zL20vMGQwdnFu?entry=ttu&g_ep=EgoyMDI1MTExMi4wIKXMDSoASAFQAw%3D%3D"

id = url.split("!1s")[1].split("!2e")[0]
pano = streetview.find_panorama_by_id(id)

path = "C:/Users/VRLAB/Desktop/testingg"

streetview.download_panorama(pano, f"{path}/test.jpg")


count = 0

time.sleep(0.01)

print(f"Pano has {len(pano.neighbors)} neighbors")

for neighbor in pano.neighbors:
    count += 1
    print(neighbor.id)

    time.sleep(0.01)
    rePano = streetview.find_panorama_by_id(neighbor.id)
    try:
        streetview.download_panorama(rePano, f"{path}/test_{count}.jpg")
    except Exception as e:
        print(e)
    