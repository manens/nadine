import os
import time
import urllib
import sys
import datetime

from nadine import email
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Sends system emails to given user."
    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('message', type=str)

    def print_keys(self):
        print("Valid Message Keys: ")
        for key in email.valid_message_keys():
            print("   " + key)

    def handle(self, *labels, **options):
        # Make sure we have a valid user
        user = None
        try:
            user = User.objects.get(username=options['username'])
        except:
            raise CommandError("Invalid username '%s'" % options['username'])

        message = options['message'].lower()
        if not email.send_manual(user, message):
            self.print_keys()
            raise CommandError("Invalid message key '%s'" % options['message'])

        print("Sending %s..." % message)
        print("Email address: %s" % user.email)


# Copyright 2016 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.