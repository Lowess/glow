#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TODO."""

import os
import time
import logging

from apscheduler.triggers.interval import IntervalTrigger

logger = logging.getLogger(__name__)


def scheduler_status(time):
    _time = time
    logger.info("Tracker is: {}".format(time=_time))


def init_jobs(scheduler):
    scheduler.add_job(
        scheduler_status,
        kwargs={"time": time.time()},
        trigger=IntervalTrigger(minutes=1),
    )


def init_scheduler(scheduler):
    """ NOTE: Really interesting finding. The scheduler does not kick off at all when
    ### There are no jobs registered in the job_store hence that dummy job by default
    ### to check on the scheduler_health periodically. This function could simply be
    ### a simple dummy(): pass function just so that there is always a job to run
    ### Might ne due to BackgroundScheduler going in a thread.join() state ?
    """

    logger.info("State of envvars {}".format(os.environ.get("WERKZEUG_WSGI")))
    # Flask werkzeug runtime (avoid double init)
    if os.environ.get("WERKZEUG_WSGI") == "true":
        if (
            os.environ.get("WERKZEUG_DEBUG") != "true"
            or os.environ.get("WERKZEUG_RUN_MAIN") == "true"  # noqa: W503
        ):
            init_jobs(scheduler)
            scheduler.start()
    # Other WSGI runtime like gunicorn which should not double init
    else:
        init_jobs(scheduler)
        scheduler.start()
