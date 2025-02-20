from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="assets_pandas_pyspark",
        packages=find_packages(exclude=["assets_pandas_pyspark_tests"]),
        install_requires=[
            "dagster",
            "dagit",
            "pytest",
            "pandas",
            "pyspark",
            # "pyarrow",
        ],
        extras_require={"test": ["pandas", "pyarrow; python_version < '3.9'", "pyspark"]},
    )
