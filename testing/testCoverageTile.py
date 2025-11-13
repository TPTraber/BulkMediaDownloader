
from streetlevel import streetview
import time


path = "C:/Users/VRLAB/Desktop/test"

count = 0

coverageList = streetview.get_coverage_tile_by_latlon(37.27086667789827, -76.70740182177956)
time.sleep(.2)
testPano = streetview.find_panorama(37.27086667789827, -76.70740182177956)
time.sleep(.2)
streetview.download_panorama(testPano, f"{path}/test_{count}.jpg")

print(coverageList)

for pano in coverageList:
    count += 1
    print(pano.id)
    rePano = streetview.find_panorama_by_id(pano.id)
    time.sleep(.2)
    try:
        streetview.download_panorama(rePano, f"{path}/test_{count}.jpg")
    except Exception as e:
        print(e)