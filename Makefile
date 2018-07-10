# Compilation output
.ONESHELL:
SHELL := /bin/bash

PWD = $(shell pwd)

SKYCOIN_DIR = gopath/src/github.com/skycoin/skycoin
SKYBUILD_DIR = $(SKYCOIN_DIR)/build
GOPATH_DIR = $(PWD)/gopath
BUILDLIBC_DIR = $(SKYBUILD_DIR)/libskycoin
LIBC_DIR = $(SKYCOIN_DIR)/lib/cgo
LIBSWIG_DIR = $(SKYCOIN_DIR)/lib/swig
BUILD_DIR = build
BIN_DIR = $(SKYCOIN_DIR)/bin
INCLUDE_DIR = $(SKYCOIN_DIR)/include
FULL_PATH_LIB = $(PWD)/$(BUILDLIBC_DIR)
FIND_COMMAND = find

ifeq ($(shell uname -s),Linux)
	TEMP_DIR = tmp
else ifeq ($(shell uname -o),Msys)
	GOPATH_DIR = "C:/projects/pyskycoin/gopath"
	FIND_COMMAND = /usr/bin/find
else ifeq ($(shell uname -s),Darwin)
	TEMP_DIR = $TMPDIR
endif

LIB_FILES = $(shell $(FIND_COMMAND) $(SKYCOIN_DIR)/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell $(FIND_COMMAND) $(SKYCOIN_DIR)/src -type f -name "*.go")
SWIG_FILES = $(shell $(FIND_COMMAND) $(LIBSWIG_DIR) -type f -name "*.i")

configure:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIBC_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIBC_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES)
	cd $(SKYCOIN_DIR) && GOPATH="$(GOPATH_DIR)" make build-libc-static
	echo "After building libskycoin"
	ls $(BUILDLIBC_DIR)
	rm -Rf swig/include/libskycoin.h
	mkdir -p swig/include
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h > swig/include/libskycoin.h

## Build libskycoin C client library
build-libc: configure $(BUILDLIBC_DIR)/libskycoin.a

build-swig:
	#Generate structs.i from skytypes.gen.h
	rm -Rf $(LIBSWIG_DIR)/structs.i
	cp $(INCLUDE_DIR)/skytypes.gen.h $(LIBSWIG_DIR)/structs.i
	#sed -i 's/#/%/g' $(LIBSWIG_DIR)/structs.i
	{ \
		if [[ "$$(uname -s)" == "Darwin" ]]; then \
			sed -i '.kbk' 's/#/%/g' $(LIBSWIG_DIR)/structs.i ;\
		else \
			sed -i 's/#/%/g' $(LIBSWIG_DIR)/structs.i ;\
		fi \
	}
	swig -python -Iswig/include -I$(INCLUDE_DIR) -outdir . -o swig/pyskycoin_wrap.c $(LIBSWIG_DIR)/skycoin.i
	
develop:
	python setup.py develop

build-libc-swig: build-libc build-swig

test: 
	tox

test27: build-swig develop
	python2.7 setup.py test	
	
test34: build-swig develop
	python3.4 setup.py test
	
test35: build-swig develop
	python3.5 setup.py test
	
