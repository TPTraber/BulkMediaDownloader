# BulkMediaDownloader

A simple wrapper for sk-zk's [streetlevel](https://github.com/sk-zk/streetlevel) package, providing a front end and simple CSV parsing.

## Getting Started

### Installing

* Download latest packaged project under [Releases](https://github.com/TPTraber/BulkMediaDownloader/releases)

### Using
- Input format for the csv file is currently very picky. It must contain two coloumns of information; The first column the name of the pano for the file to be saved, second is the link to the google streetview pano. ([See Example](https://github.com/TPTraber/BulkMediaDownloader/blob/main/example.csv)). If no title is added for a row, it will take the previous title with a incremental counter appened.
- I recommend you use a spreadsheet software like Google Sheets to build the table, then export to a csv file.
- Important Note:
    - The link must be the full **unshortened URL** such that it contatins "data=" and the pano ID to be extracted. 
    ```
    https://www.google.com/maps/place/Danilovsky+Market/@55.7119781,37.6208306,3a,75y,343.01h,98.06t/data=!3m8!1e1!3m6!1sCIHM0ogKEICAgIDUgYbgfg!2e10!3e11!6shttps:%2F%2Flh3.googleusercontent.com%2Fgpms-cs-s%2FAPRy3c9vUi7WTf-bmqbBwu5QZ4JXoZUkxsf0KfDxeutWADDBY2J6B8tY6m97Qbh-apwq7d0NzVYmLaDxvSeuxA4H6amklc3X8fCDAdHq1hMfXA1xOjOB2UufSNvFqU4UnoIG9PSK-TD-%3Dw900-h600-k-no-pi-8.056593522996863-ya343.0144261938121-ro0-fo100!7i7744!8i3872!4m9!3m8!1s0x46b54b4049352c55:0xb495381d43890bba!8m2!3d55.7121856!4d37.6205067!10e5!14m1!1BCgIgARICCAI!16s%2Fg%2F1vp6yw9p?entry=ttu&g_ep=EgoyMDI1MTAyMi4wIKXMDSoASAFQAw%3D%3D
    ```




## Package from Source

* Clone repo to local device
* Install dependencies
```
pip install -r requirements.txt
```
* Install pyinstaller
```
pip install pyinstaller
```
* Package into .EXE with pyinstaller
```
pyinstaller --windowed --onefile AppV2.py
```


## Version History

* 1.1
    * Updated streetlevel for Google API Change
    * See [release history]()
* 1.0
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE file for details

## Acknowledgments

* [streetlevel](https://github.com/sk-zk/streetlevel)
* [Sun-Valley-ttk-theme](https://github.com/rdbende/Sun-Valley-ttk-theme)