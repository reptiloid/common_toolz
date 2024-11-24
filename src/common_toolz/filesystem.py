from pathlib import Path
import platform


if platform.system() == 'Windows':
    temp_data_path    = Path('d:\MEDIA\TRADING\DATA_TEMP')
    ramdisk_data_path = Path('d:\MEDIA\TRADING\DATA_TEMP')
    # ramdisk_data_path = Path('x:\DATA')

elif platform.system() == 'Linux':
    temp_data_path    = Path('~/Documents/DATA_TEMP').expanduser()
    ramdisk_data_path = Path('~/Documents/DATA_TEMP').expanduser()

def nn(name=''):
    return str(temp_data_path.joinpath(name))

def ramnn(name=''):
    return str(ramdisk_data_path.joinpath(name))
