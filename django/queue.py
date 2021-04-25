import uuid

from django_q.tasks import async_task, result

from mediamap_api.common.utils.datetime_helper import datetime_helper


class Job:

    def __init__(self, params, worker, group, completion_hook, job_id=uuid.uuid4()):
        self.job_id = job_id
        self.created_time = datetime_helper.get_timezone_aware_current_time()
        self.job_params = params
        self.worker = worker
        self.group = group
        self.completion_hook = completion_hook


class QueManager:

    def create_job(self, job):
        task_id = async_task(job.worker,
                             job.job_params,
                             group=job.group,
                             hook=job.completion_hook)
        return task_id

    def check_status(self, task_id):
        return result(task_id, -1)

# instance
que_manager = QueManager()
