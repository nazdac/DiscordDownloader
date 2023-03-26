import os
import sys
try:
    from requests import Session
except:
    os.system('pip install requests')
from threading import Thread as ThreadPooler
Threads = []
InstallName = input('Which Discord Client Do You Want To Install? (development, canary, ptb, stable):')


class Install:
    def ThreadPool(self):
        ThreadPooler(target=Install().DownloadOne()).start()

    def DownloadOne(self):
        with Session() as Pool:
            Downloader = Pool.get(
                f'https://discordapp.com/api/downloads/distributions/app/installers/latest?channel={InstallName}&platform=win&arch=x86',
                stream=True,
                allow_redirects=True)
            open(f'Downloads\\Client [{InstallName}].exe', 'wb').write(Downloader.content)
            if Downloader.status_code in (201, 200, 204, 203, 202):
                print(f'Successfully Downloaded Client: {InstallName}')
                os.system('pause')
                os.startfile(sys.argv[0])
                sys.exit()
            if Downloader.status_code in (400, 401, 402, 403, 404, 405):
                print(f'Unable To Install Client: {InstallName}, Reason: {Downloader.status_code}, {Downloader.text}')
                os.system('pause')
                os.startfile(sys.argv[0])
                sys.exit()


if __name__ == '__main__':
    Install().ThreadPool()
