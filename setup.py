from setuptools import setup

setup(
    name="mkhtml",
    version="0.1",
    description="A port of mkhtml tool",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    url="https://github.com/krerkkiat/cs2401-mkhtml-web",
    author="Krerkkiat Chusap",
    author_email="kc555014@ohio.edu",
    license="MIT",
    packages=["mkhtml"],
    install_requires=[
        "Flask",
        "gunicorn",
    ],
    zip_safe=False,
)
