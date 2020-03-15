import internetarchive as ia

class join(delegate.page):
    path = "/partner-with-us"

    def POST(self):
        import re
        i = web.input(email='', name='', isbns='', csv={})
        isbns = re.findall('([0-9X]{10,13})', i.isbns.upper())
        print(isbns)
        return isbns
        # create openlibraries item
        prefix = 'test_'
        {
            'mediatype': 'collection',
            'needs_overlap': True,
            'noindex': True,
            'access-restricted': True
        }
        


