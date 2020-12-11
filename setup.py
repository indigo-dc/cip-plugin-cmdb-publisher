from setuptools import find_packages
from setuptools import setup


setup(
    name='cip_plugin_cmdb_publisher',
    version='1.0',
    description='INDIGO CMDB publisher for the cloud-info-provider',
    license='Apache License 2.0',
    author='Pablo Orviz',
    author_email='orviz@ifca.unican.es',
    url='http://github.com/indigo-dc/cip-plugin-cmdb-publisher',
    classifiers=['License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.7',
                 'Intended Audience :: Information Technology',
                 'Intended Audience :: System Administrators',
                 'Intended Audience :: Developers',
                 'Operating System :: POSIX :: Linux',
                 'Environment :: Console',
                 'Topic :: System :: Monitoring'
                 ],
    packages=find_packages(),
    # install_requires=get_requirements(),
    entry_points={
        'cip.publishers': [
            'cmdb = cip_plugin_cmdb_publisher.cmdb:CMDBPublisher',
        ],
    },
    zip_safe=False,
)
