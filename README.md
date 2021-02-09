# Image_processing


# Download

Git clone or download the folder from git 

```

git clone https://github.com/dalindalz/Image_processing.git

```


# Directory Structure

Add a new folder called Data in the root folder and copy all the videos to the corresponding folder


```
├── Image_processing
    ├── _init_.py
    ├── config.py
    ├── video_processing.py
    ├── watch_folder.py
    ├── README.md
    ├── Data

```

# Installation

### Install the library with conda or pip:



```sh
$ pip install tqdm
$ pip install multiprocess
$ pip install opencv=3.2.0
$ pip install watchdog
$ pip install argparse

```
# Usage

Once the packages are installed go to the folder and run the _init_.py file as follows

```

python _init_.py -r -g -s

-r -> Optional flag to rotate the video
-g -> Optional flag to greyscale the video
-s -> Optional flag to Save the video

```


