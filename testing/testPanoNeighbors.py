"""
Currently Not working ;(
"""


from streetlevel import streetview
import time

url = "https://www.google.com/maps/@37.2814091,-76.6936657,3a,75y,293.49h,80.75t/data=!3m7!1e1!3m5!1suCgqBD6-AJ22Su1tpad7wA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D9.254850486564123%26panoid%3DuCgqBD6-AJ22Su1tpad7wA%26yaw%3D293.4900554585608!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MTExMC4wIKXMDSoASAFQAw%3D%3D"

id = url.split("!1s")[1].split("!2e")[0]
pano = streetview.find_panorama_by_id(id)

path = "C:/Users/VRLAB/Desktop/test"

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
    