from fabric.api import cd, prefix, run, task


### atomic commands

@task
def build():
	with prefix('source ~/env/bin/activate'):
		with cd('~/repo'):
			run('pelican ./content -s pelicanconf.py -o ../htdocs -v')

@task
def clean():
	run('rm -fr htdocs/*')

@task
def pull():
	with cd('~/repo'):
		run('git pull')

@task
def setup_requirements():
	with prefix('source ~/env/bin/activate'):
		with cd('~/repo'):
			run('pip install -r requirements.txt')

### compound commands

@task
def deploy():
	pull()
	setup_requirements()
	build()

@task
def rebuild():
	clean()
	deploy()

