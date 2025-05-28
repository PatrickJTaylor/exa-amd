import parsl

from tools.config_manager import ConfigManager
from tools.logging_config import amd_logger
from parsl_configs.parsl_config_registry import get_parsl_config
from workflows.vasp_based import run_workflow
from tools.config_labels import ConfigKeys as CK

if __name__ == '__main__':
    # load global config
    config = ConfigManager()

    # load parsl config
    parsl.load(get_parsl_config(config))

    # configure logging
    amd_logger.configure(config[CK.OUTPUT_LEVEL])

    # run the workflow
    run_workflow(config)

    # cleanup
    parsl.dfk().cleanup()
