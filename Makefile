.PHONY: test
test:
	uv run pytest

.PHONY: shell
shell:
	uv run python -m manage shell

.PHONY: superuser
superuser:
	uv run python -m manage createsuperuser

.PHONY: build
build:
	docker-compose -f docker-compose.local.yml build

.PHONY: local-up
local-up:
	docker-compose -f docker-compose.local.yml up
