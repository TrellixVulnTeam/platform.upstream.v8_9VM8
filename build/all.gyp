# Copyright 2011 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'All',
      'type': 'none',
      'variables': {
        'enable_test%': 1,
        'building_for_tizen%': 0,
      },
      'dependencies': [
        '../samples/samples.gyp:*',
        '../src/d8.gyp:d8',
      ],
      'conditions': [
        ['component!="shared_library"', {
          'dependencies': [
            '../tools/parser-shell.gyp:parser-shell',
          ],
        }],
        ['enable_test==1', {
          'dependencies': [
            '../test/cctest/cctest.gyp:*',
            '../test/unittests/unittests.gyp:*',
          ],
        }],
      ]
    }
  ]
}
