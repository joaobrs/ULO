from setuptools import setup

setup(
    name = "ulo",
    version = "0.1",
    packages = ["ulo"],
    test_suite = "tests",
    author = "Pete Shadbolt",
    author_email = "hello@peteshadbolt.co.uk",
    url = "https://github.com/peteshadbolt/ulo",
    description = "Linear optics simulator",
    keywords = "quantum",
    setup_requires = ["numpy"],
    scripts = [],
    install_requires = ["numpy", "permanent"],
    package_data = {},
    include_package_data=False
)
