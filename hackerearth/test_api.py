

from hackerearth.parameters import SupportedLanguages
from hackerearth.parameters import RunAPIParameters

from hackerearth.api_handlers import HackerEarthAPI

client_secret = '0a7f0101e5cc06e4417a3addeb76164680ac83a4'
source = "print 23"
lang = SupportedLanguages.PYTHON
compressed = 1
html = 0
params = RunAPIParameters(client_secret=client_secret, source=source,
        lang='PYTHON', compressed=compressed, html=0)

api = HackerEarthAPI(params)

r = api.compile()
print r.async
print r.compile_status
print r.web_link
print r.code_id
print r.id
print r.__dict__

r = api.run()
print r.__dict__
