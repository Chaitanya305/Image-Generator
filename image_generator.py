import subprocess
from versions import python_versions
from versions import r_versions
from versions import base_images


def docker_cmd(docker_build_cmd, docker_push_cmd, docker_rmi_cmd, docker_prune_cmd):
    subprocess.run(docker_build_cmd, shell=True, check=True)
    subprocess.run(docker_push_cmd, shell=True, check=True)
    subprocess.run(docker_rmi_cmd, shell=True, check=True)
    subprocess.run(docker_prune_cmd, shell=True, check=True)


def python(p_v, base_image, name_pv):
    name_os = base_image   
    #cd_command=f'cd dockerfiles/{base_image}/python'
    docker_build_command = f'docker build dockerfiles/{base_image}/python --build-arg BASE_IMAGE={base_image} --build-arg PYTHON_VERSION={p_v} -t chaitanya305/dataflow-{name_os}-py{name_pv}'
    docker_push_cmd = f'docker push chaitanya305/dataflow-{name_os}-py{name_pv}'
    docker_rmi_cmd = f'docker rmi chaitanya305/dataflow-{name_os}-py{name_pv}'
    docker_prune_cmd = f'docker system prune -f'
    #print (f'{docker_build_command}\n{docker_push_cmd}\n{docker_rmi_cmd}\n{docker_prune_cmd}')
    docker_cmd(docker_build_command, docker_push_cmd, docker_rmi_cmd, docker_prune_cmd)

    
def r(r_v, base_image, name_rv):
    name_os = base_image
    docker_build_command = f'docker build dockerfiles/{base_image}/r_base --build-arg BASE_IMAGE={base_image} --build-arg R_VERSION={r_v} -t chaitanya305/dataflow-{name_os}-r{name_rv}'
    docker_push_cmd = f'docker push chaitanya305/dataflow-{name_os}-r{name_rv}'
    docker_rmi_cmd = f'docker rmi chaitanya305/dataflow-{name_os}-r{name_rv}'
    docker_prune_cmd = f'docker system prune -f'
    #print (f'{docker_build_command}\n{docker_push_cmd}\n{docker_rmi_cmd}\n{docker_prune_cmd}')
    docker_cmd(docker_build_command, docker_push_cmd, docker_rmi_cmd, docker_prune_cmd)


def python_r(p_v, r_v, base_image, name_rv, name_pv):
    name_os = base_image
    docker_build_command = f'docker build dockerfiles/{base_image}/python_r --build-arg BASE_IMAGE={base_image} --build-arg R_VERSION={r_v} --build-arg PYTHON_VERSION={p_v} -t chaitanya305/dataflow-{name_os}-r{name_rv}py{name_pv}'
    docker_push_cmd = f'docker push chaitanya305/dataflow-{name_os}-r{name_rv}py{name_pv}'
    docker_rmi_cmd = f'docker rmi chaitanya305/dataflow-{name_os}-r{name_rv}py{name_pv}'
    docker_prune_cmd = f'docker system prune -f'
    #print (f'{docker_build_command}\n{docker_push_cmd}\n{docker_rmi_cmd}\n{docker_prune_cmd}')
    docker_cmd(docker_build_command, docker_push_cmd, docker_rmi_cmd, docker_prune_cmd)


for base_image in base_images:
    for p_v in python_versions:
        name_pv = p_v
        name_pv = name_pv.split(".")
        name_pv = ("".join(name_pv[0:2]))
        python(p_v, base_image, name_pv)
    for r_v in r_versions:
        name_rv = r_v
        name_rv = name_rv.split(".")
        name_rv = ("".join(name_rv)).strip("0")
        r(r_v, base_image, name_rv)
    for p_v in python_versions:
        for r_v in r_versions:
            name_pv = p_v
            name_pv = name_pv.split(".")
            name_pv = ("".join(name_pv[0:2]))
            name_rv = r_v
            name_rv = name_rv.split(".")
            name_rv = ("".join(name_rv)).strip("0")
            python_r(p_v, r_v, base_image, name_rv, name_pv)