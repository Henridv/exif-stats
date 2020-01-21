all: run

build:
	docker build -f docker/Dockerfile -t exif-tool .

run:
	docker run --rm \
		-v $(PWD)/photos:/app/photos \
		exif-tool

watch: build
	docker run -it --rm \
		-v $(PWD)/:/app \
		exif-tool \
		bash
