

from hackerearth.parameters import SupportedLanguages
from hackerearth.parameters import RunAPIParameters

from hackerearth.api_handlers import HackerEarthAPI

client_secret = '0a7f0101e5cc06e4417a3addeb76164680ac83a4'
source = "print '1235'*10000"
lang = SupportedLanguages.PYTHON
compressed = 1
params = RunAPIParameters(client_secret=client_secret, source=source,
        lang='PYTHON', compressed=compressed)

api = HackerEarthAPI(params)

r = api.run()
print r
