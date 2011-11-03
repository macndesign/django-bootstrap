from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

master_file = open(os.path.join(root, ".git", "refs", "heads", "master"))
VERSION = '0.1.git-' + master_file.read().strip()
master_file.close()

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


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
