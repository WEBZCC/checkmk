#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
from cmk.base.plugins.agent_based.df_section import parse_df
from cmk.base.plugins.agent_based.utils.df import FILESYSTEM_DEFAULT_PARAMS

checkname = 'df'

parsed = parse_df([
    ['/dev/sda4', 'ext4', '143786696', '101645524', '34814148', '75%', '/'],
    ['/dev/sda2', 'ext4', '721392', '151120', '517808', '23%', '/boot'],
    ['[df_inodes_start]'],
    ['/dev/sda4', 'ext4', '9142272', '1654272', '7488000', '19%', '/'],
    ['/dev/sda2', 'ext4', '46848', '304', '46544', '1%', '/boot'],
    ['[df_inodes_end]'],
])

discovery = {
    '': [
        (
            '/',
            {
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
        (
            '/boot',
            {
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
    ]
}

checks = {
    '': [
        (
            '/',
            {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': False,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'subtract_reserved': True,
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    'Used: 74.49% - 96.9 GiB of 130 GiB, additionally reserved for root: 6.99 GiB',
                    [
                        ('fs_used', 99263.20703125, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 74.48759220233214, 80.0, 90.0, 0.0, 100.0),
                        ('fs_free', 33998.19140625, None, None, 0, 140416.6953125),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB, therein reserved for root: 5.10% (6.99 GiB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB, therein reserved for root: 5.10% (6.99 GiB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/home',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': False,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [],
        ),
        (
            '/',
            {
                **FILESYSTEM_DEFAULT_PARAMS,
                'show_inodes': 'onlow',
                'inodes_levels': (90.0, 5.0)
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    1,
                    ('Inodes used: 18.09% (warn/crit at 10.00%/95.00%), '
                     'Inodes available: 7,488,000 (81.91%)'),
                    [
                        ('inodes_used', 1654272, 914227.2000000001, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                **FILESYSTEM_DEFAULT_PARAMS,
                'show_inodes': 'onlow',
                'inodes_levels': (8542272, 8142272)
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    2,
                    'Inodes used: 1,654,272 (warn/crit at 600,000/1,000,000), Inodes available: 7,488,000 (81.91%)',
                    [
                        ('inodes_used', 1654272, 600000.0, 1000000.0, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            'all',
            {
                **FILESYSTEM_DEFAULT_PARAMS,
                'patterns': (['*'], []),
            },
            [
                (
                    0,
                    'Used: 75.55% - 104 GiB of 138 GiB',
                    [
                        ('fs_used', 106617.31640625, 112896.94375, 127009.06171875, 0,
                         141121.1796875),
                        ('fs_size', 141121.1796875, None, None, 0, None),
                        ('fs_used_percent', 75.55018788982939, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654576, 8270208.0, 8729664.0, 0.0, 9189120.0),
                    ],
                ),
                (
                    0,
                    '2 filesystems',
                    [],
                ),
            ],
        ),
        (
            'parts',
            {
                **FILESYSTEM_DEFAULT_PARAMS,
                'patterns': (['*oot', '/'], []),
            },
            [
                (
                    0,
                    'Used: 75.55% - 104 GiB of 138 GiB',
                    [
                        ('fs_used', 106617.31640625, 112896.94375, 127009.06171875, 0,
                         141121.1796875),
                        ('fs_size', 141121.1796875, None, None, 0, None),
                        ('fs_used_percent', 75.55018788982939, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654576, 8270208.0, 8729664.0, 0.0, 9189120.0),
                    ],
                ),
                (
                    0,
                    '2 filesystems',
                    [],
                ),
            ],
        ),
        (
            '/boot',
            {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            },
            [
                (
                    0,
                    'Used: 28.22% - 199 MiB of 704 MiB',
                    [
                        ('fs_used', 198.8125, 563.5875, 634.0359375, 0, 704.484375),
                        ('fs_size', 704.484375, None, None, 0, None),
                        ('fs_used_percent', 28.22099496528933, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 304, 42163.200000000004, 44505.6, 0.0, 46848.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False,
            },
            [
                (
                    0,
                    'Used: 75.79% - 104 GiB of 137 GiB',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, 0, None),
                        ('fs_used_percent', 75.78764310712029, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/boot',
            {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False,
            },
            [
                (
                    0,
                    'Used: 28.22% - 199 MiB of 704 MiB',
                    [
                        ('fs_used', 198.8125, 563.5875, 634.0359375, 0, 704.484375),
                        ('fs_size', 704.484375, None, None, 0, None),
                        ('fs_used_percent', 28.22099496528933, 80.0, 90.0, 0.0, 100.0),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 304, 42163.200000000004, 44505.6, 0.0, 46848.0),
                    ],
                ),
            ],
        )
    ]
}
