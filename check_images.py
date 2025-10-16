import urllib.request
import ssl

urls = [
    'https://cdn.pixabay.com/photo/2016/03/05/19/02/eggs-1238433_1280.jpg',
    'https://cdn.pixabay.com/photo/2017/01/06/19/15/frog-1959821_1280.jpg',
    'https://cdn.pixabay.com/photo/2013/07/12/15/55/giraffe-150325_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/21/07/hat-33610_1280.png',
    'https://cdn.pixabay.com/photo/2014/12/21/23/28/ice-cream-579693_1280.png',
    'https://cdn.pixabay.com/photo/2016/11/29/09/32/beverage-1869598_1280.jpg',
    'https://cdn.pixabay.com/photo/2013/07/12/18/39/kite-153641_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/lion-31245_1280.png',
    'https://cdn.pixabay.com/photo/2014/12/21/23/28/monkey-579693_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/nest-31244_1280.png',
    'https://cdn.pixabay.com/photo/2017/01/20/15/06/orange-1995056_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/parrot-31242_1280.png',
    'https://cdn.pixabay.com/photo/2013/07/13/12/46/queen-146331_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/rabbit-31241_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/sun-31240_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/tree-31239_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/umbrella-31238_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/violin-31237_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/whale-31236_1280.png',
    'https://cdn.pixabay.com/photo/2013/07/13/12/46/xylophone-146332_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/yacht-31235_1280.png',
    'https://cdn.pixabay.com/photo/2012/04/13/00/21/zebra-31234_1280.png'
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            ct = resp.getheader('Content-Type')
            print(f"OK\t{resp.status}\t{ct}\t{u}")
    except Exception as e:
        print(f"ERROR\t{e}\t{u}")
