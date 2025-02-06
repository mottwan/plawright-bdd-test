from setuptools import setup, find_packages

setup(
    name="playwright-bdd-test",
    version="0.1.0",
    packages=find_packages(include=["steps", "pages"]),  # ✅ Explicitly specify packages
    install_requires=[
        "playwright~=1.50.0",
        "pytest==8.3.4",
        "pytest-bdd==8.1.0",
        "pytest-xdist==3.6.1",
        "pytest-playwright==0.7.0",
    ],
)
