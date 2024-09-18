from bs4 import BeautifulSoup as bs
import pip._vendor.requests as rq


def starting_code(url , head):

    qresp = rq.get(url=url, headers=head)

    bsoup = bs(qresp._content , 'html.parser')
    return bsoup