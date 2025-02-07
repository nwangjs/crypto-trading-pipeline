.PHONY: build build_cpp install_cpp install_python test_cpp test_python test_integration clean lint_format_check_cpp lint_format_check_python format

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

build: build_cpp install_python

build_cpp: install_cpp
	cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) -G Ninja
	cd build && cmake --build .
	@cp -f build/*.so $(PY_SRC)

install_cpp:
	conan install . --build=missing

install_python:
	poetry install

test_cpp: build_cpp
	@cd build && ./intern_tests

test_python: build
	@poetry run pytest $(PY_SRC)/test/unit

test_integration: build
	@poetry run pytest $(PY_SRC)/test/integration

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so

lint_format_check_cpp: build
	find $(CPP_SRC) -name "*.cpp" -or -name "*.hpp" | xargs clang-tidy -p=build
	find $(CPP_SRC) -name "*.cpp" -or -name '*.hpp' | xargs clang-format --dry-run --Werror

lint_format_check_python: install_python
	poetry run mypy $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

format:
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)