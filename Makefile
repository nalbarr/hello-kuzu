help:
	@echo make run
	@echo make docker-run
	@echo make run-ui

run: clean
	python main.py

clean:
	rm -fr ./demo_db

docker-run:
	docker run -p 8000:8000 \
           -v ./demo_db:/demo_db \
           -v ./data:/data \
           --rm kuzudb/explorer:latest
run-ui:
	open http://localhost:8000
