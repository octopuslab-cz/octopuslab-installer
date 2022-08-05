URL="https://octopusengine.org/download/micropython/stable.tar"


def exists(path):
    import os
    try:
        os.stat(path)
        return True
    except OSError:
        return False
        
def create_missing_dir(save_path):
    import os
    if save_path.startswith('/'):
        save_path = save_path[1:]
    
    # create missing directories
    dir_name = ""
    for i in save_path.split('/')[:-1]:
        dir_name += '/' + i
        if not exists(dir_name):
            print('Creating directory', dir_name)
            os.mkdir(dir_name)

def connect(ssid=None, psk=None):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)
    
def download(source, target):
    import urequests
    import lib.shutil as shutil
    try:
        res = urequests.get(source)
        if not res.status_code == 200:
            print('Error, response status code', res.status_code)
            return
        if target.endswith('/'):
            print('Error, target must be filename not a directory')
            return
        if not target.startswith('/'):
            print('Error, target must start with /')
            return
        create_missing_dir(target)

        with open(target, 'wb') as f:
            print('Downloading', source, 'to', target)
            shutil.copyfileobj(res.raw, f)
    except OSError as e:
        print(e)
        print('Are you connected to wifi?')

def deploy(source=URL, save_path=None):
    import os
    import lib.shutil as shutil
    import upip_utarfile as utarfile

    def wipe_fs():
        print('TODO wipe filesystem')

    def extract_tar(file_content):
        t = utarfile.TarFile(fileobj=file_content)

        for f in t:
            print("Extracting {}: {}".format(f.type, f.name))
            if f.type == utarfile.DIRTYPE:
                if f.name[-1:] == '/':
                    name = f.name[:-1]
                else:
                    name = f.name

                if not exists(name):
                    os.mkdir(name)
            else:
                extracted = t.extractfile(f)

                with open(f.name, "wb") as fobj:
                    shutil.copyfileobj(extracted, fobj)

    print('Running deploy from', source)

    load_from_file = True
    if source.startswith('http://') or source.startswith('https://'):
        load_from_file = False        
        # download file online
        import urequests
        try:
            res = urequests.get(source)
            if not res.status_code == 200:
                print('Error, response status code', res.status_code)
                return
            if save_path:
                if not save_path.startswith('/'):
                    print('Error, save_path must start with /')
                    return
                
                create_missing_dir(save_path)

                with open(save_path, 'wb') as source_file:
                    print('Downloading image to', save_path)
                    shutil.copyfileobj(res.raw, source_file)
                    load_from_file = True
                    source = save_path
            else:
                wipe_fs()
                extract_tar(res.raw)

        except OSError as e:
            print(e)
            print('Are you connected to wifi?')

    if load_from_file:
        with open(source) as file_content:
            wipe_fs()
            extract_tar(file_content)


