all: build

build:
	# Create dynamically-linked binary
	mkdir -p /tmp/out
	mkdir -p /tmp/build/build-$$(uname -m)
	mkdir -p /tmp/spec/spec-$$(uname -m)
	pyinstaller -n consumatio-backend.linux-$$(uname -m) --distpath /tmp/out --workpath /tmp/build/build-$$(uname -m) --specpath /tmp/spec/spec-$$(uname -m) --onefile main.py --add-data $${PWD}/consumatio/external/api.graphql:consumatio/external/api.graphql --add-data $${PWD}/migrations:migrations --hidden-import logging.config

	# Stage dynamically-linked binaries
	mkdir -p out
	cp /tmp/out/consumatio-backend.linux-$$(uname -m) out

release: build
	# Create statically-linked binary
	mkdir -p /tmp/out/release
	staticx /tmp/out/consumatio-backend.linux-$$(uname -m) /tmp/out/release/consumatio-backend.linux-$$(uname -m)

	# Stage statically-linked binaries
	mkdir -p out/release
	cp /tmp/out/release/consumatio-backend.linux-$$(uname -m) out/release

install: release
	sudo install out/release/consumatio-backend.linux-$$(uname -m) /usr/local/bin/consumatio-backend
	
dev:
	DEBUG=true python3 main.py

clean:
	rm -rf out

depend:
	# Install dependencies
	pip3 install -r requirements.txt

	# Install python development dependencies
	pip3 install pyinstaller
	pip3 install staticx

migrations:
	flask db stamp head
	flask db migrate -m $$(MSG)
	flask db upgrade