#!/usr/bin/python3

import logging
import sys
import getpass

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream


LOGGER = logging.getLogger('support_bundles')

def init_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                                                  '%Y-%m-%dT%H:%M:%S'))
    LOGGER.addHandler(stream_handler)
    LOGGER.setLevel(logging.INFO)


class SupportBundles:
    __namespace = 'default'
    __label = 'app=filter-logs'
    __container = 'filter-logs'

    def __init__(self):
        self.__user_args = sys.argv[1:]
        SupportBundles.__setup_kube_configuration()
        self.__core_v1 = core_v1_api.CoreV1Api()

    @staticmethod
    def __get_ca_cert():
        try:
            secret_service = get_config_section('secret_service')
            return secret_service['ca_chain']['ca_chain_pem']
        except Exception as e:
            raise RuntimeError('Unable to retrieve CA Certificate information: %s', e)

    @staticmethod
    def __setup_kube_configuration():
        def get_config_file():
            if getpass.getuser() == 'oracle-support':
                return '/home/oracle-support/.kube/admin.conf'
            return '/root/.kube/admin.conf'

        config.load_kube_config(config_file=get_config_file())
        configuration = Configuration().get_default_copy()
        configuration.ssl_ca_cert = SupportBundles.__get_ca_cert()
        configuration.verify_ssl = True
        Configuration().set_default(configuration)

    def run(self):
        pod_name = self.__get_pod_name()
        self.__exec_command(pod_name)

    def __get_pod_name(self):
        try:
            LOGGER.info('Locating filter-logs Pod')

            pods = self.__core_v1.list_namespaced_pod(namespace=SupportBundles.__namespace,
                                                      label_selector=SupportBundles.__label)
            if len(pods.items) == 0:
                raise RuntimeError('filter-logs Pod not found')

            for pod in pods.items:
                if pod.status.phase == 'Running':
                    return pod.metadata.name

            raise RuntimeError('filter-logs Pod with "pod.status.phase == Running" not found')
        except ApiException as e:
            raise RuntimeError('Unable to locate filter-logs Kubernetes Pod: %s', e)

    def __exec_command(self, pod_name):
        exec_command = []
        if "triage" in self.__user_args:
            exec_command = ['python3', '/usr/lib/python3.6/site-packages/filter_logs/triage.py']
        elif "time_slice" in self.__user_args:
            exec_command = ['python3', '/usr/lib/python3.6/site-packages/filter_logs/time_slice.py']
        elif "smart" in self.__user_args:
            exec_command = ['python3', '/usr/lib/python3.6/site-packages/filter_logs/smart.py']
        elif "native" in self.__user_args:
            exec_command = ['python3', '/usr/lib/python3.6/site-packages/filter_logs/native.py']
        elif "-h" or "--help" in self.__user_args:
            exec_command = ['python3', '/usr/lib/python3.6/site-packages/filter_logs/help.py']
        exec_command.extend(self.__user_args[2:])
        try:
            LOGGER.info('Executing command - %s', exec_command)

            resp = stream(self.__core_v1.connect_get_namespaced_pod_exec,
                          pod_name,
                          SupportBundles.__namespace,
                          container=SupportBundles.__container,
                          command=exec_command,
                          stderr=True, stdin=False,
                          stdout=True, tty=False)
            LOGGER.info(resp)
        except Exception as e:
            raise RuntimeError('Unable to execute command %s: %s', exec_command, e)


if __name__ == '__main__':
    init_logging()

    try:
        LOGGER.info('Starting Support Bundles')
        SupportBundles().run()
        sys.exit(0)
    except Exception as ex:
        LOGGER.error('Encountered an exception: %s', ex)
        sys.exit(1)
    finally:
       LOGGER.info('Finished running Support Bundles')