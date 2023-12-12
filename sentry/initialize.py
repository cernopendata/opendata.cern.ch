# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2018 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Sentry initialization script.

Based on example code from: 'https://docs.sentry.io/server/faq/'

"""

# Bootstrap the Sentry environment
from sentry.models import Organization, OrganizationMember, OrganizationMemberTeam, \
    Project, ProjectKey, Team, User
from sentry.utils.runner import configure

configure()


# Make an assumption that if 'admin' -User exists Sentry has been initialized
if not User.objects.filter(username='admin').exists():
    user = User()
    user.username = 'admin'
    user.email = 'admin@example.org'
    user.is_superuser = True
    user.set_password('admin')
    user.save()

    organization = Organization.objects.filter(slug='sentry')[0]

    team = Team()
    team.name = 'COD'
    team.organization = organization
    team.save()

    project = Project()
    project.team = team
    project.add_team(team)
    project.name = 'Cern Open Data Portal'
    project.organization = organization
    project.save()

    ProjectKey.objects.get(project=project).delete()

    public_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    secret_key = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'

    key = ProjectKey.objects.create(project=project, public_key=public_key,
                                    secret_key=secret_key, roles=1)

    member = OrganizationMember.objects.create(
        organization=organization,
        user=user,
        role='owner',
    )

    OrganizationMemberTeam.objects.create(
        organizationmember=member,
        team=team,
    )

    print('SENTRY_DSN = "{}"').format(key.get_dsn())
