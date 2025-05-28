from parsl import bash_app

from parsl_configs.parsl_executors_labels import GENERATE_EXECUTOR_LABEL
from tools.config_labels import ConfigKeys as CK


def cmd_gen_structures(config):
    """
    Construct the shell command used to run the generation script via Parsl.

    Prepares the working environment and generates the command to execute
    the CGCNN `cms_dir/gen_structure.py` script. This task generates
    hypothetical structures based on the initial crystal structures provided
    in `mpstrs`.

    Args:
        config (dict): ConfigManager. The following fields are used:
            - work_dir
            - cms_dir
            - num_workers
            - elements

            See :class:`~tools.config_manager.ConfigManager` for field descriptions.

    Returns:
        str: A formatted shell command string to execute `gen_structure.py`.

    Raises:
        Exception: If directory navigation or file operations fail.
    """
    import os
    try:
        dir_structures = os.path.join(config[CK.WORK_DIR], "structures")
        dir_mp_structures = os.path.join(config[CK.CMS_DIR], "mpstrs")
        dir_gen_structures = os.path.join(
            config[CK.CMS_DIR], "gen_structure.py")

        if not os.path.exists(dir_structures):
            os.makedirs(dir_structures)
        os.chdir(dir_structures)
    except Exception as e:
        raise

    return "python {} --num_workers {} --input_dir {} --elements {}".format(
        dir_gen_structures, config[CK.NUM_WORKERS], dir_mp_structures, config[CK.ELEMENTS])


@bash_app(executors=[GENERATE_EXECUTOR_LABEL])
def gen_structures(config):
    return cmd_gen_structures(config)
