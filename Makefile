init:
	test -n "$(name)"
	find ./ -type f -not -path "./.git" -exec perl -pi -e 's/project_name/$(name)/g' *.* {} \;
	mv src/project_name src/$(name)
	mv config/nginx/project_name.conf config/nginx/$(name).conf
	mv config/nginx-dev/project_name.conf config/nginx-dev/$(name).conf

superuser:
	docker exec -it project_name ./manage.py createsuperuser

makemigrations:
	docker exec -it project_name ./manage.py makemigrations

migrate:
	docker exec -it project_name ./manage.py migrate

initialfixture:
	docker exec -it project_name ./manage.py loaddata initial

testfixture:
	docker exec -it project_name ./manage.py loaddata test

test:
	docker exec -it project_name ./manage.py test

statics:
	docker exec -it project_name ./manage.py collectstatic --noinput
