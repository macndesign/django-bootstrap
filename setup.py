from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.2.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

def gen_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results

setup(
    name='django-bootstrap',
    version=VERSION,
    description="Django class-based views working with Bootstrap, from Twitter.",
    long_description="Django class-based views ready to work with Twitter's Bootstrap toolkit, designed to kickstart development of webapps and sites.",
    author="Codasus Technologies",
    author_email="contact@codasus.com",
    url="http://github.com/codasus/django-bootstrap",
    license="MIT License",
    platforms=["any"],
    packages=['bootstrap'],
    data_files=gen_data_files(os.path.join('bootstrap', 'templates')),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
