# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_vhost is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_vhost is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_vhost components for simplification of gen_vhost bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_vhost.core.service.iservice import IService
from gen_vhost.core.service.isubprocessor import ISubProcessor
from gen_vhost.infrastructure.cli.icli import ICLI
from gen_vhost.setup.bundle import GenVhostBundle
from gen_vhost.setup.validator import GenVhostBundleValidator
from gen_vhost.setup.keys import GenVhostBundleKeys
from gen_vhost.setup.dependencies import GenVhostBundleDependencies
from gen_vhost.setup.dep_validator import GenVhostBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenVhostBundleRegistry:
    '''
        Encapsulates core gen_vhost components for simplification of gen_vhost bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_vhost bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenVhostBundleDependencies) -> GenVhostBundle:
        '''
            Creates the gen_vhost bundle.

            :param dependencies: The gen_vhost bundle dependencies.
            :return: The gen_vhost bundle.
            :exceptions:
                | ATSValueError: The gen_vhost bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_vhost bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_vhost bundle must be provided and have proper values.
                | ATSTypeError:  The gen_vhost bundle must be an instance of GenVhostBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenVhostBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenVhostBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenVhostBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenVhostBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenVhostBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenVhostBundle = GenVhostBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenVhostBundleValidator.validate(bundle)

        return bundle
