from setuptools import setup

setup(
    name='nyaka',
    version='0.1.0',    
    description='This program allows you to find and count the occurrences of specified words in a pdf file.',
    url='https://github.com/K4r4b0M0kg0th0/nyaka',
    author='K4r4b0 M0kg0th0',
    author_email='Mojurarecords@gmail.com',
    license='MIT',
    packages=['findr'],
    install_requires=['PyPDF2',
                      'argparse',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)