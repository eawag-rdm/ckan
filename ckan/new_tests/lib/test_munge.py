from nose import tools as nose_tools

from ckan.lib.munge import (munge_filename, munge_name,
                            munge_title_to_name, munge_tag)


class TestMungeFilename(object):

    # (original, expected)
    munge_list = [
        ('unchanged', 'unchanged'),
        ('bad spaces', 'bad-spaces'),
        ('s', 's__'),  # too short
        ('random:other%character&', 'randomothercharacter'),
        (u'u with umlaut \xfc', 'u-with-umlaut-u'),
        ('2014-11-10 12:24:05.340603my_image.jpeg',
         '2014-11-10-122405.340603myimage.jpeg')
    ]

    def test_munge_filename(self):
        '''Munge a list of filenames gives expected results.'''
        for org, exp in self.munge_list:
            munge = munge_filename(org)
            nose_tools.assert_equal(munge, exp)

    def test_munge_filename_multiple_pass(self):
        '''Munging filename multiple times produces same result.'''
        for org, exp in self.munge_list:
            first_munge = munge_filename(org)
            nose_tools.assert_equal(first_munge, exp)
            second_munge = munge_filename(first_munge)
            nose_tools.assert_equal(second_munge, exp)


class TestMungeName(object):

    # (original, expected)
    munge_list = [
        ('unchanged', 'unchanged'),
        ('bad spaces', 'bad-spaces'),
        ('s', 's_'),  # too short
        ('random:other%character&', 'random-othercharacter'),
        (u'u with umlaut \xfc', 'u-with-umlaut-u'),
        ('2014-11-10 12:24:05.my_image', '2014-11-10-12-24-05-my_image')
    ]

    def test_munge_name(self):
        '''Munge a list of names gives expected results.'''
        for org, exp in self.munge_list:
            munge = munge_name(org)
            nose_tools.assert_equal(munge, exp)

    def test_munge_name_multiple_pass(self):
        '''Munging name multiple times produces same result.'''
        for org, exp in self.munge_list:
            first_munge = munge_name(org)
            nose_tools.assert_equal(first_munge, exp)
            second_munge = munge_name(first_munge)
            nose_tools.assert_equal(second_munge, exp)


class TestMungeTitleToName(object):

    # (original, expected)
    munge_list = [
        ('unchanged', 'unchanged'),
        ('some spaces  here', 'some-spaces-here'),
        ('s', 's_'),  # too short
        ('random:other%character&', 'random-othercharacter'),
        (u'u with umlaut \xfc', 'u-with-umlaut-u'),
        ('reallylong' * 12, 'reallylong' * 9 + 'reall'),
        ('reallylong' * 12 + ' - 2012', 'reallylong' * 9 + '-2012')
    ]

    def test_munge_title_to_name(self):
        '''Munge a list of names gives expected results.'''
        for org, exp in self.munge_list:
            munge = munge_title_to_name(org)
            nose_tools.assert_equal(munge, exp)

    def test_munge_title_to_name_multiple_pass(self):
        '''Munging title to name multiple times produces same result.'''
        for org, exp in self.munge_list:
            first_munge = munge_title_to_name(org)
            nose_tools.assert_equal(first_munge, exp)
            second_munge = munge_title_to_name(first_munge)
            nose_tools.assert_equal(second_munge, exp)


class TestMungeTag:

    # (original, expected)
    munge_list = [
        ('unchanged', 'unchanged'),
        ('s', 's_'),  # too short
        ('some spaces  here', 'some-spaces--here'),
        ('random:other%character&', 'randomothercharacter')
    ]

    def test_munge_tag(self):
        '''Munge a list of tags gives expected results.'''
        for org, exp in self.munge_list:
            munge = munge_tag(org)
            nose_tools.assert_equal(munge, exp)

    def test_munge_tag_muliple_pass(self):
        '''Munge a list of tags muliple times gives expected results.'''
        for org, exp in self.munge_list:
            first_munge = munge_tag(org)
            nose_tools.assert_equal(first_munge, exp)
            second_munge = munge_tag(first_munge)
            nose_tools.assert_equal(second_munge, exp)
