# BulkMediaDownloader

A app for installing multiple types of online hosted content. Provides a front end and simple CSV parsing.

As of now it can download:
* Streetview panos
  * Uses sk-zk's [streetlevel](https://github.com/sk-zk/streetlevel) package
* jpgs and pngs 

## Getting Started

### Installing

* Download latest packaged project under [Releases](https://github.com/TPTraber/BulkMediaDownloader/releases)

### Using

#### CSV

* Input format for the csv file is currently very picky. It must contain two columns of information; The first column is used for the name the file to be saved, second is the link to the media. ([See Example](https://github.com/TPTraber/BulkMediaDownloader/blob/main/example.csv)). If no title is added for a row, it will take the previous title with a incremental counter appened.
* I recommend you use a spreadsheet software like Google Sheets to build the table, then export to a csv file.
* Important Note:
  * The link must be the full **unshortened URL** such that it contatins "data=" and the pano ID to be extracted or location the image is stored.

    ``` URL
    https://www.google.com/maps/place/Danilovsky+Market/@55.7119781,37.6208306,3a,75y,343.01h,98.06t/data=!3m8!1e1!3m6!1sCIHM0ogKEICAgIDUgYbgfg!2e10!3e11!6s
    ```
    ``` URL
    https://img.magnific.com/free-photo/closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head_488145-3540.jpg
    ```

#### URL List
* Provide URL list seperated by semicolons (;)
Example:
``` url
https://www.imagehostersite.com/images/image.png;https://www.google.com/maps/..data=STREETVIEWID
```

## Package from Source

* Clone repo to local device
* Install [Python (only tested on v3.14.8)](https://www.python.org/downloads/release/python-3148/)
* Create python venv

``` bash
cd path/to/repo
py -V:3.14.8 -m venv .venv
```
* Install dependencies

``` bash
pip install -r requirements.txt
```

* Install pyinstaller

``` bash
pip install pyinstaller
```

* Package into .EXE with pyinstaller

``` bash
pyinstaller winApp.spec
```

* or Package into app directory for Mac

``` bash
pyinstaller macApp.spec
```

## Version History
* 1.1.0
  * Added app info section
  * Added URL list functionality
  * Changed UI to Tabs
  * See [release history](https://github.com/TPTraber/BulkMediaDownloader/releases)
* 1.0.2
  * Added truststore for Mac Keychain SSL Authentication.
  * See [release history](https://github.com/TPTraber/BulkMediaDownloader/releases)
* 1.0.1
  * Updated streetlevel for Google API Change
  * See [release history](https://github.com/TPTraber/BulkMediaDownloader/releases)
* 1.0.0
  * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE file for details

## Acknowledgments

* [streetlevel](https://github.com/sk-zk/streetlevel)
* [Sun-Valley-ttk-theme](https://github.com/rdbende/Sun-Valley-ttk-theme)
