from setuptools import setup, find_packages

setup(
    name='vk-language',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    author='Varun Krishna',
    author_email='beasovacompany@gmail.com',
    description='Vk programming language package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SVarunKrishna/vk-language',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
