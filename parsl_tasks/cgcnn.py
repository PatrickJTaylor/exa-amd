from parsl import python_app, bash_app
from parsl_configs.parsl_executors_labels import CGCNN_EXECUTOR_LABEL

def cmd_cgcnn_prediction(config):
    """
    Construct the shell command used to run a CGCNN prediction via Parsl.

    Prepares the working environment and generates the command to execute
    the CGCNN `predict.py` script.

    Args:
        config (ConfigManager or dict): Configuration object. The following fields are used:
            - work_dir
            - cms_dir
            - batch_size
            - num_workers

            See :class:`~tools.config_manager.ConfigManager` for full field descriptions.

    Returns:
        str: The formatted shell command to execute.

    Raises:
        Exception: If directory navigation or file copying fails.
    """
    import os
    import shutil
    try:
        os.chdir(config["work_dir"])

        predict_script_path = os.path.join(config["cms_dir"], "predict.py")
        model_path = os.path.join(config["cms_dir"], "form_1st.pth.tar")

        dir_structures = os.path.join(
            config["work_dir"], "structures")
        atom_init_json = os.path.join(config["cms_dir"], "atom_init.json")

        shutil.copy(atom_init_json, dir_structures)
    except Exception as e:
        raise
    num_workers = config["num_workers"]
    return "python {} {} {} --batch-size {} --workers {} ".format(
        predict_script_path, model_path, dir_structures, config["batch_size"], num_workers)

@bash_app(executors=[CGCNN_EXECUTOR_LABEL])
def cgcnn_prediction(config):
    return cmd_cgcnn_prediction(config)
   