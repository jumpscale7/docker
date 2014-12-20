#BOOTSTRAP CODE
try:
    from urllib3.request import urlopen
except ImportError:
    from urllib import urlopen
import random
handle = urlopen("https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/InstallTools.py?%s"%random.randint(1, 10000000)) #this is to protect against caching proxy servers
exec(handle.read())


#look at methods in https://github.com/Jumpscale/jumpscale_core7/blob/master/install/InstallTools.py to see what can be used
#there are some easy methods to allow git manipulation, copy of files, execution of items 

#there are many more functions available in jumpscale

print "prepare jumpscale docker"

do.installDocker()

url="https://github.com/Jumpscale/docker"
do.pullGitRepo(url,dest=None,login=None,passwd=None,depth=None,ignorelocalchanges=False,reset=False,branch="master")

cmd="cd /opt/code/github/jumpscale/docker/image_js;docker build -t despiegk/js:1.0 ."
do.executeInteractive(cmd)


# from JumpScale import j

#j.system....