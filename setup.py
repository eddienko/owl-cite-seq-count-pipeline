from setuptools import find_packages, setup

readme = ""

requirements = [
    "dask",
    "distributed",
    "voluptuous",
    "owl-pipeline-develop",
    "CITE-seq-Count",
]

setup_requirements = ["pytest-runner", "flake8"]

test_requirements = ["coverage", "pytest", "pytest-cov", "pytest-mock"]


setup(
    author="Eduardo Gonzalez Solares",
    author_email="eglez@ast.cam.ac.uk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
    ],
    description="Owl CITE Seq Count Pipeline",
    entry_points={"owl.pipelines": "cite_seq_count = owl_cite_seq_count"},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords="owl",
    name="owl-cite-seq-count-pipeline",
    packages=find_packages(include=["owl_cite_seq_count*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/eddienko/owl-cite-seq-count-pipeline",
    version="0.1.0",
    zip_safe=False,
    python_requires=">=3.7",
)
