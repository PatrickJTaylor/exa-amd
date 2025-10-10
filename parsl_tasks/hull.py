from parsl import bash_app, python_app
from tools.config_labels import ConfigKeys as CK
from parsl_configs.parsl_executors_labels import POSTPROCESSING_LABEL


def cmd_vasp_hull(config, work_subdir):
    """
    Using the total energies, computes the formation energies of each structure
    relative to reference elemental phases.

    Parameters
    ----------
    config : dict
        ConfigManager instance. The following fields are used:

        - ``CK.VASP_NTASKS_PER_RUN`` (*int*): Number of MPI ranks.
          ``1`` triggers a run with a single process; any other value results in
          ``srun -n <N>``.
        - ``CK.VASP_STD_EXE``: Path to the VASP executable.

        See :class:`~tools.config_manager.ConfigManager` for field descriptions.

    work_subdir : str
        Name of the working subdirectory where the hull calculation is run.

    Returns
    -------
    str
        A formatted shell command string to execute `run_single_vasp_hull_calculation.py`.

    Raises
    ------
    Exception
        If directory navigation or file operations fail.
    """
    import os
    try:
        os.chdir(work_subdir)
        exec_cmd_prefix = (
            "" if config[CK.VASP_NTASKS_PER_RUN] == 1
            else f"srun -n {config[CK.VASP_NTASKS_PER_RUN]}"
        )
        output_file = os.path.join(work_subdir, "output")
    except Exception as e:
        raise
    return f" {exec_cmd_prefix} {config[CK.VASP_STD_EXE]} > {output_file}"


@bash_app(executors=[POSTPROCESSING_LABEL])
def run_single_vasp_hull_calculation(config, work_subdir):
    return cmd_vasp_hull(config, work_subdir)
