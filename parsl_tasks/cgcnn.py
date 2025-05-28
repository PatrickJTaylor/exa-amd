from parsl import python_app, bash_app

from parsl_configs.parsl_executors_labels import CGCNN_EXECUTOR_LABEL
from tools.config_labels import ConfigKeys as CK


def cmd_cgcnn_prediction(config):
    """
    Construct the shell command used to run a CGCNN prediction via Parsl.

    Prepares the working environment and generates the command to execute
    the CGCNN `cms_dir/predict.py` script.

    Args:
        config (dict): ConfigManager. The following fields are used:
            - work_dir
            - cms_dir
            - batch_size
            - num_workers

            See :class:`~tools.config_manager.ConfigManager` for full field descriptions.

    Returns:
        str: A formatted shell command string to execute `predict.py`.

    Raises:
        Exception: If directory navigation or file copying fails.
    """
    import os
    import shutil
    try:
        os.chdir(config[CK.WORK_DIR])

        predict_script_path = os.path.join(config[CK.CMS_DIR], "predict.py")
        model_path = os.path.join(config[CK.CMS_DIR], "form_1st.pth.tar")

        dir_structures = os.path.join(
            config[CK.WORK_DIR], "structures")
        atom_init_json = os.path.join(config[CK.CMS_DIR], "atom_init.json")

        shutil.copy(atom_init_json, dir_structures)
    except Exception as e:
        raise
    num_workers = config[CK.NUM_WORKERS]
    return "python {} {} {} --batch-size {} --workers {} ".format(
        predict_script_path, model_path, dir_structures, config[CK.BATCH_SIZE], num_workers)


@bash_app(executors=[CGCNN_EXECUTOR_LABEL])
def cgcnn_prediction(config):
    return cmd_cgcnn_prediction(config)
