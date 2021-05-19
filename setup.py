import setuptools

config = {
        'name': "pcg_ppg_analysis",
        'version': "0.1",
        'author': "Davide Marzorati",
        'author_email': "davide.marzorati@polimi.it",
        'packages': setuptools.find_packages(),
}

setuptools.setup(**config)
