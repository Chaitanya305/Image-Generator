import subprocess
from versions import python_versions
from versions import r_versions
from versions import base_images

def docker_cmd(docker_build_cmd, docker_push_cmd):
    subprocess.run(docker_build_cmd, shell=True, check=True)
    subprocess.run(docker_push_cmd, shell=True, check=True)

def python(p_v, base_image):
    #cd_command=f'cd dockerfiles/{base_image}/python'
    docker_build_command= f'docker build dockerfiles/{base_image}/python --build-arg BASE_IMAGE={base_image} --build-arg PYTHON_VERSION={p_v} -t chaitanya305/dataflow-base-py{p_v}'
    docker_push_cmd=f'docker push chaitanya305/dataflow-base-py{p_v}'
    docker_cmd(docker_build_command, docker_push_cmd)
    
def r(r_v, base_image):
    docker_build_command= f'docker build dockerfiles/{base_image}/r_base --build-arg BASE_IMAGE={base_image} --build-arg R_VERSION={r_v} -t chaitanya305/dataflow-base-r{r_v}'
    docker_push_cmd=f'docker push chaitanya305/dataflow-base-r{r_v}'
    docker_cmd(docker_build_command, docker_push_cmd)

def python_r(p_v, r_v, base_image):
    docker_build_command= f'docker build dockerfiles/{base_image}/python_r --build-arg BASE_IMAGE={base_image} --build-arg R_VERSION={r_v} --build-arg PYTHON_VERSION={p_v} -t chaitanya305/dataflow-base-r{r_v}py{p_v}'
    docker_push_cmd=f'docker push chaitanya305/dataflow-base-r{r_v}py{p_v}'
    docker_cmd(docker_build_command, docker_push_cmd)

for base_image in base_images:
    for p_v in python_versions:
        python(p_v, base_image)
    for r_v in r_versions:
        r(r_v, base_image)
    for p_v in python_versions:
        for r_v in r_versions:
            python_r(p_v, r_v, base_image)
