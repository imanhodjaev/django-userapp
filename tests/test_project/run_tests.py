#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import django

from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["django_userapp"])
    sys.exit(bool(failures))
