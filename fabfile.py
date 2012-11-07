from fabric.api import cd, prefix, run, task


### atomic commands

@task
def clean():
	run('rm -fr htdocs/*')

@task
def compile():
	with prefix('source ~/env/bin/activate'):
		with cd('~/repo'):
			run('pelican . -s pelicanconf.py -o ../htdocs -v')

@task
def pull():
	with cd('~/repo'):
		run('git pull')

@task
def setup_requirements():
	run('pip install -r requirements.txt')

### compound commands

@task
def deploy():
	pull()
	compile()

@task
def rebuild():
	clean()
	deploy()

