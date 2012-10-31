from fabric.api import cd, prefix, run, task


### atomic commands

@task
def compile():
	with prefix('source ~/env/bin/activate'):
		with cd('~/repo'):
			run('pelican . -s settings.py -o ../htdocs -v')

@task
def pull():
	with cd('~/repo'):
		run('git pull')


### compound commands

@task
def deploy():
	pull()
	compile()

