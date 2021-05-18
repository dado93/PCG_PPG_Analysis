import setuptools

config = {
        'name': "PCG-PPG-Analysis",
        'version': "0.1",
        'author': "Davide Marzorati",
        'author_email': "davide.marzorati@polimi.it",
        'packages': setuptools.find_packages(),
}

setuptools.setup(**config)