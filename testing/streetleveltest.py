from streetlevel import streetview


url = "https://www.google.com/maps/@37.2705792,-76.7143899,3a,75y,62.75h,86.18t/data=!3m7!1e1!3m5!1sO_9gr1vROpXCiAa6ZzBwCw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D3.8213347364037418%26panoid%3DO_9gr1vROpXCiAa6ZzBwCw%26yaw%3D62.748188509694465!7i3328!8i1664?entry=ttu&g_ep=EgoyMDI1MDkxMC4wIKXMDSoASAFQAw%3D%3D"
id = url.split("!1s")[1].split("!2e")[0]
print(id)

pano = streetview.find_panorama_by_id(id)

print(pano)

streetview.download_panorama(pano, f"{pano.id}.jpg")