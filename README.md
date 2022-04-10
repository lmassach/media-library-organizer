# Media library organizer
A script to automatically add new content from a directory to a Jellyfin-style media library folder structure.

**TODO** thorough explanation.

## Installation
Installation instruction for Ubuntu/Debian/RaspberryPiOS.
It should be fairly similar on other systems.
Python 3.9+ is assumed to be installed.

Install the required libraries.
```bash
pip3 install --user -r requirements.txt
```

Install [FFmpeg](https://ffmpeg.org/).
```bash
sudo apt install ffmpeg
```

Clone this repository in a directory of your choice.
```bash
git clone https://github.com/lmassach/media-library-organizer.git
```
**TODO switch to `release` branch when I create it.**

If you need to run medialiborg from outside this repo's directory, set the
`PYTHONPATH` environment variable.
```bash
export PYTHONPATH="$PYTHONPATH:/path/to/this/repo"
```

## Configuration
A file with the default configuration can be generated with
```bash
python3 -m medialiborg --write-default-config config.json
```
Explanation of the settings:
 - `scan_dirs` is a list of directories to scan for new media (**must be set manually**);
 - `lib_dir` is the directory of the media library (**must be set manually**);
 - `link` if true (default), the media files are symlinked to the media library, otherwise they are moved and renamed;

## Usage
**TODO Manual launching.**

**TODO Configuration of crontab.**

## License
This project is made by [lmassach](https://github.com/lmassach/) distributed under the GNU GPL v3 (see the `LICENSE` file).
No warranty given.
