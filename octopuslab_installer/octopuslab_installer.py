URL="https://octopusengine.org/download/micropython/stable.tar"

def connect(ssid=None, psk=None):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)
    

def deploy(source=URL, save_path=None):
    import os
    import lib.shutil as shutil
    import upip_utarfile as utarfile

    def exists(path):
        try:
            os.stat(path)
            return True
        except:
            return False

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
                
                # create missing directories
                split_path = save_path[1:]
                dir_name = ""
                for i in split_path.split('/')[:-1]:
                    dir_name += '/' + i
                    if not exists(dir_name):
                        print('Creating directory', dir_name)
                        os.mkdir(dir_name)

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


