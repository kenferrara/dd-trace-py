from riot import Suite, Case

global_deps = [
    "mock",
    "pytest<4",
    "pytest-benchmark",
]

global_env = [("PYTEST_ADDOPTS", "--color=yes")]

suites = [
    Suite(
        name="tracer",
        command="pytest tests/tracer/",
        cases=[
            Case(
                pys=[
                    2.7,
                    3.5,
                    3.6,
                    3.7,
                    3.8,
                ],
                pkgs=[("msgpack", [""])],
            ),
        ],
    ),
    Suite(
        name="profiling",
        command="python -m tests.profiling.run pytest --capture=no --verbose tests/profiling/",
        env=[
            ("DD_PROFILE_TEST_GEVENT", lambda case: "1" if "gevent" in case.pkgs else None),
        ],
        cases=[
            Case(
                pys=[
                    2.7,
                    3.5,
                    3.6,
                    3.7,
                    3.8,
                    3.9,
                ],
                pkgs=[("gevent", [None, ""])],
            ),
            # Min reqs tests
            Case(
                pys=[2.7],
                pkgs=[
                    ("gevent", ["==1.1.0"]),
                    ("protobuf", ["==3.0.0"]),
                    ("tenacity", ["==5.0.1"]),
                ],
            ),
            Case(
                pys=[
                    3.5,
                    3.6,
                    3.7,
                    3.8,
                    3.9,
                ],
                pkgs=[
                    ("gevent", ["==1.4.0"]),
                    ("protobuf", ["==3.0.0"]),
                    ("tenacity", ["==5.0.1"]),
                ],
            ),
        ],
    ),
]
